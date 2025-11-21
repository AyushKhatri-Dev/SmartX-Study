import PyPDF2
import google.generativeai as genai
from django.conf import settings
import json
import logging

logger = logging.getLogger(__name__)

# Configure Gemini API
def configure_gemini():
    """Configure Gemini API with proper error handling"""
    api_key = getattr(settings, 'GEMINI_API_KEY', None)
    if api_key and api_key.strip():
        try:
            genai.configure(api_key=api_key)
            return genai.GenerativeModel('gemini-2.5-flash')
        except Exception as e:
            logger.error(f"Error configuring Gemini API: {str(e)}")
            return None
    else:
        logger.warning("GEMINI_API_KEY not found or empty in settings")
        return None

# Initialize model
model = configure_gemini()

def get_model():
    """Get Gemini model with lazy initialization"""
    global model
    if model is None:
        model = configure_gemini()
    return model


def extract_text_from_pdf(pdf_file):
    """Extract text content from PDF file with better error handling."""
    try:
        # Reset file pointer to beginning
        pdf_file.seek(0)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text_content = ""
        
        for page_num, page in enumerate(pdf_reader.pages):
            try:
                page_text = page.extract_text()
                if page_text:
                    text_content += page_text + "\n"
            except Exception as e:
                logger.warning(f"Error extracting text from page {page_num}: {str(e)}")
                continue
        
        # Clean up the text
        text_content = text_content.strip()
        
        if not text_content:
            logger.warning("No text content extracted from PDF")
            return "No readable text found in the PDF. Please ensure the PDF contains text content."
        
        return text_content
        
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        return f"Error reading PDF file: {str(e)}"


def generate_summary(text_content):
    """Generate summary using Gemini API with better error handling."""
    model = get_model()
    
    if not model:
        return "AI summarization is currently unavailable. Please check your API configuration."
    
    if not text_content or len(text_content.strip()) < 50:
        return "Document content is too short to generate a meaningful summary."
    
    try:
        # Limit text length to avoid token limits
        max_chars = 8000
        if len(text_content) > max_chars:
            text_content = text_content[:max_chars] + "..."
        
        prompt = f"""
        Please provide a comprehensive summary of the following text. 
        Focus on key concepts, main ideas, and important details that would be useful for studying.
        Make the summary clear, well-structured, and easy to understand.

        Text to summarize:
        {text_content}
        
        Please provide a detailed summary:
        """
        
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text.strip()
        else:
            return "Unable to generate summary. The AI service returned an empty response."
            
    except Exception as e:
        logger.error(f"Error generating summary: {str(e)}")
        error_msg = str(e).lower()
        
        if "api_key" in error_msg or "authentication" in error_msg:
            return "API authentication failed. Please check your Gemini API key configuration."
        elif "quota" in error_msg or "limit" in error_msg:
            return "API quota exceeded. Please try again later or check your API limits."
        elif "safety" in error_msg:
            return "Content was filtered for safety reasons. Please try with different content."
        else:
            return f"Error generating summary: {str(e)}"


def answer_question(question, context):
    """Answer question based on document context using Gemini API."""
    model = get_model()
    
    if not model:
        return "AI Q&A is currently unavailable. Please check your API configuration."
    
    if not question or not context:
        return "Please provide both a question and document context."
    
    try:
        # Limit context length
        max_chars = 8000
        if len(context) > max_chars:
            context = context[:max_chars] + "..."
        
        prompt = f"""
        Based on the following document content, please answer the user's question accurately and comprehensively.
        If the answer is not clearly available in the document, please indicate that.

        Document Content:
        {context}

        Question: {question}

        Please provide a detailed answer based on the document content:
        """
        
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text.strip()
        else:
            return "Unable to generate an answer. Please try rephrasing your question."
            
    except Exception as e:
        logger.error(f"Error answering question: {str(e)}")
        return f"Sorry, I couldn't process your question: {str(e)}"


def generate_test_questions(text_content, num_questions=5):
    """Generate test questions based on document content."""
    model = get_model()
    
    if not model:
        logger.error("Gemini model not available for test generation")
        return []
    
    if not text_content or len(text_content.strip()) < 100:
        logger.warning("Text content too short for test generation")
        return []
    
    try:
        # Limit text length
        max_chars = 8000
        if len(text_content) > max_chars:
            text_content = text_content[:max_chars] + "..."
        
        prompt = f"""
        Based on the following text content, generate {num_questions} multiple choice questions for a quiz.
        Each question should have 4 options (A, B, C, D) with only one correct answer.
        Focus on key concepts, important facts, and main ideas from the text.
        
        Please format your response as a JSON array with this exact structure:
        [
            {{
                "question": "Question text here",
                "options": {{
                    "A": "Option A text",
                    "B": "Option B text", 
                    "C": "Option C text",
                    "D": "Option D text"
                }},
                "correct_answer": "A"
            }}
        ]

        Text Content:
        {text_content}
        """
        
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            logger.error("Empty response from Gemini API")
            return []
        
        response_text = response.text.strip()
        
        # Try to find JSON in the response
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']') + 1
        
        if start_idx >= 0 and end_idx > start_idx:
            json_text = response_text[start_idx:end_idx]
            try:
                questions = json.loads(json_text)
                
                # Validate the structure
                valid_questions = []
                for q in questions:
                    if (isinstance(q, dict) and 
                        'question' in q and 
                        'options' in q and 
                        'correct_answer' in q and
                        isinstance(q['options'], dict) and
                        len(q['options']) == 4):
                        valid_questions.append(q)
                
                return valid_questions
                
            except json.JSONDecodeError as e:
                logger.error(f"JSON decode error: {str(e)}")
                return []
        else:
            logger.error("No valid JSON found in response")
            return []
            
    except Exception as e:
        logger.error(f"Error generating test questions: {str(e)}")
        return []


def calculate_test_score(questions, user_answers):
    """Calculate test score based on user answers."""
    if not questions or not user_answers:
        return 0, 0
    
    correct_count = 0
    total_questions = len(questions)
    
    for i, question in enumerate(questions):
        question_key = f"question_{i}"
        if question_key in user_answers:
            if user_answers[question_key] == question['correct_answer']:
                correct_count += 1
    
    return correct_count, total_questions