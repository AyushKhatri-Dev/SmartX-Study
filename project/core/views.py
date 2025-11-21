from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Count, Avg
import json

from .forms import CustomUserCreationForm, DocumentUploadForm, QAForm
from .models import Document, QASession, Test, TestAttempt
from .utils import extract_text_from_pdf, generate_summary, answer_question, generate_test_questions, calculate_test_score


def home(request):
    """Landing page."""
    return render(request, 'core/home.html')


def learn_more(request):
    """Learn more page with platform explanation."""
    return render(request, 'core/learn_more.html')


def signup(request):
    """User registration."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to SmartX Study.')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def dashboard(request):
    """Main dashboard after login."""
    documents = Document.objects.filter(user=request.user)[:5]
    recent_tests = TestAttempt.objects.filter(user=request.user)[:5]
    recent_qa = QASession.objects.filter(user=request.user)[:5]
    
    # Statistics
    total_documents = documents.count()
    total_tests = TestAttempt.objects.filter(user=request.user).count()
    avg_score = TestAttempt.objects.filter(user=request.user).aggregate(Avg('score'))['score__avg'] or 0
    
    context = {
        'documents': documents,
        'recent_tests': recent_tests,
        'recent_qa': recent_qa,
        'total_documents': total_documents,
        'total_tests': total_tests,
        'avg_score': round(avg_score, 1),
    }
    return render(request, 'core/dashboard.html', context)


@login_required
def upload_document(request):
    """Upload and process PDF documents."""
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            
            # Process PDF
            try:
                # Extract text from PDF
                pdf_content = extract_text_from_pdf(document.file)
                
                if pdf_content and not pdf_content.startswith("Error"):
                    document.content = pdf_content
                    
                    # Generate summary
                    summary = generate_summary(pdf_content)
                    document.summary = summary
                    document.is_processed = True
                    document.save()
                    
                    messages.success(request, 'Document uploaded and processed successfully!')
                else:
                    document.content = pdf_content  # This will contain the error message
                    document.summary = "Unable to process this PDF. Please ensure it contains readable text."
                    document.is_processed = False
                    document.save()
                    
                    messages.warning(request, 'Document uploaded but processing failed. Please check if the PDF contains readable text.')
                    
                return redirect('document_detail', document_id=document.id)
                
            except Exception as e:
                document.content = f"Processing error: {str(e)}"
                document.summary = "An error occurred while processing this document."
                document.is_processed = False
                document.save()
                
                messages.error(request, f'Error processing document: {str(e)}')
                return redirect('document_detail', document_id=document.id)
    else:
        form = DocumentUploadForm()
    
    return render(request, 'core/upload_document.html', {'form': form})


@login_required
def document_detail(request, document_id):
    """Display document details and summary."""
    document = get_object_or_404(Document, id=document_id, user=request.user)
    return render(request, 'core/document_detail.html', {'document': document})


@login_required
def qa_session(request, document_id):
    """Q&A session for a document."""
    document = get_object_or_404(Document, id=document_id, user=request.user)
    qa_sessions = QASession.objects.filter(document=document, user=request.user)
    
    if request.method == 'POST':
        form = QAForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            answer = answer_question(question, document.content)
            
            # Save Q&A session
            QASession.objects.create(
                user=request.user,
                document=document,
                question=question,
                answer=answer
            )
            
            messages.success(request, 'Question answered successfully!')
            return redirect('qa_session', document_id=document.id)
    else:
        form = QAForm()
    
    context = {
        'document': document,
        'form': form,
        'qa_sessions': qa_sessions,
    }
    return render(request, 'core/qa_session.html', context)


@login_required
def generate_test(request, document_id):
    """Generate test questions for a document."""
    document = get_object_or_404(Document, id=document_id, user=request.user)
    
    if request.method == 'POST':
        try:
            questions = generate_test_questions(document.content)
            if questions:
                test = Test.objects.create(
                    user=request.user,
                    document=document,
                    title=f"Test for {document.title}",
                    questions=questions
                )
                messages.success(request, 'Test generated successfully!')
                return redirect('take_test', test_id=test.id)
            else:
                messages.error(request, 'Unable to generate test questions. Please try again.')
        except Exception as e:
            messages.error(request, f'Error generating test: {str(e)}')
    
    # Show existing tests for this document
    existing_tests = Test.objects.filter(document=document, user=request.user)
    context = {
        'document': document,
        'existing_tests': existing_tests,
    }
    return render(request, 'core/generate_test.html', context)


@login_required
def take_test(request, test_id):
    """Take a test."""
    test = get_object_or_404(Test, id=test_id, user=request.user)
    context = {
        'test': test,
    }
    return render(request, 'core/take_test.html', context)


@login_required
@require_http_methods(["POST"])
def submit_test(request, test_id):
    """Submit test answers and calculate score."""
    test = get_object_or_404(Test, id=test_id, user=request.user)
    
    try:
        # Get user answers from POST data
        user_answers = {}
        for key, value in request.POST.items():
            if key.startswith('question_'):
                user_answers[key] = value
        
        # Calculate score
        correct_count, total_questions = calculate_test_score(test.questions, user_answers)
        
        # Save test attempt
        attempt = TestAttempt.objects.create(
            user=request.user,
            test=test,
            answers=user_answers,
            score=correct_count,
            total_questions=total_questions
        )
        
        return redirect('test_result', attempt_id=attempt.id)
        
    except Exception as e:
        messages.error(request, f'Error submitting test: {str(e)}')
        return redirect('take_test', test_id=test.id)


@login_required
def test_result(request, attempt_id):
    """Display test results."""
    attempt = get_object_or_404(TestAttempt, id=attempt_id, user=request.user)
    context = {
        'attempt': attempt,
    }
    return render(request, 'core/test_result.html', context)


@login_required
def progress_tracking(request):
    """Progress tracking page."""
    documents = Document.objects.filter(user=request.user)
    test_attempts = TestAttempt.objects.filter(user=request.user).order_by('-completed_at')
    
    # Calculate statistics
    total_documents = documents.count()
    total_tests = test_attempts.count()
    if test_attempts:
        avg_score = sum(attempt.percentage for attempt in test_attempts) / total_tests
        recent_scores = [attempt.percentage for attempt in test_attempts[:10]]
    else:
        avg_score = 0
        recent_scores = []
    
    context = {
        'documents': documents,
        'test_attempts': test_attempts,
        'total_documents': total_documents,
        'total_tests': total_tests,
        'avg_score': round(avg_score, 1),
        'recent_scores': recent_scores,
    }
    return render(request, 'core/progress_tracking.html', context)