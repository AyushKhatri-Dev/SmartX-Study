# SmartX Study 📚

> An intelligent educational SaaS platform powered by AI that transforms how students learn, practice, and track their progress.

[![Django](https://img.shields.io/badge/Django-4.2.7-darkgreen)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue)]()
[![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

---

## 🎯 Overview

SmartX Study is a full-stack Django web application that leverages **Google Gemini AI** to provide intelligent PDF analysis and learning assistance. Students can upload study materials, get AI-generated summaries, ask questions, take auto-generated tests, and track their learning progress—all in one platform.


---

## ✨ Key Features

### 📄 Smart PDF Upload & Processing
- Upload PDF files up to 10MB
- Automatic text extraction using PyPDF2
- Instant file processing and storage
- Support for multiple document uploads

### 🤖 AI-Powered Summarization
- Generate intelligent summaries using Google Gemini AI
- Understand complex topics in seconds
- Markdown-formatted summaries for better readability
- Context-aware analysis of document content

### 💬 Interactive Q&A System
- Ask unlimited questions about your documents
- Get accurate, context-aware answers from AI
- View conversation history
- Real-time answer generation (3-5 seconds)
- Persistent storage of all Q&A sessions

### 📝 Auto-Generated Test Creation
- Automatically generate 5 multiple-choice questions
- Questions based on document content
- Instant test submission and evaluation
- Detailed results with correct/incorrect answers

### 📊 Progress Tracking Dashboard
- View all test attempts and scores
- Track performance metrics:
  - Total tests taken
  - Average score
  - Recent test history
- Visual analytics and insights
- Performance trends over time

### 🔐 User Authentication & Security
- Secure login/registration system
- User data isolation and privacy
- CSRF and XSS protection
- Input validation and sanitization
- Session management

### 🎨 Modern, Responsive UI
- Built with Tailwind CSS
- Mobile-friendly design
- Smooth animations and transitions
- Intuitive user interface
- Dark mode ready

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Django 4.2.7 |
| **Language** | Python 3.10+ |
| **AI Model** | Google Gemini AI (gemini-2.5-flash) |
| **PDF Processing** | PyPDF2 |
| **Frontend** | HTML, CSS, Tailwind CSS |
| **Database** | SQLite (Django ORM) |
| **Authentication** | Django Built-in |
| **API Integration** | google-generativeai==0.3.2 |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Google Gemini API key
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ayushkhatri-Dev/SmartX-Study.git
cd project
python manage.py runserver
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
GEMINI_API_KEY=your-google-gemini-api-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Get Gemini API Key:**
1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy and paste in `.env`

### Step 5: Run Migrations
```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🚀 Usage Guide

### 1. Register & Login
- Visit the homepage
- Click "Sign Up"
- Create your account with email and password
- Login with your credentials

### 2. Upload a Document
```
Dashboard → Upload Document → Select PDF → Submit
```
- Choose a PDF file (max 10MB)
- System automatically extracts text and generates summary
- View your document in the dashboard

### 3. Get AI Summary
```
Document Detail Page → AI Generated Summary Section
```
- Automatic summary generated on upload
- Formatted with markdown for readability
- Perfect for quick revision

### 4. Ask Questions
```
Document Detail Page → Ask Questions → Type Question → Submit
```
- Ask any question about the document
- Get answers in 3-5 seconds
- View previous Q&As
- Ask unlimited questions

### 5. Take Practice Tests
```
Document Detail Page → Generate Test → Answer Questions → Submit
```
- Generate 5 multiple-choice questions
- Answer all questions
- Submit for instant evaluation
- View detailed results

### 6. Track Progress
```
Dashboard → View Progress → See Analytics
```
- View all test attempts
- Check performance metrics
- Analyze learning trends
- Identify weak areas

---

## 📊 Database Models

### Document Model
- Stores uploaded PDF documents
- Contains extracted text and AI-generated summary
- Links to user account
- Tracks upload timestamp

### QASession Model
- Stores question-answer pairs
- Linked to specific document
- Maintains conversation history
- Timestamps for each interaction

### Test Model
- Stores generated MCQ questions
- Contains question, options, correct answer
- JSON field for flexible storage
- Associated with document

### TestAttempt Model
- Records user test attempts
- Stores user answers and scores
- Calculates performance metrics
- Enables progress tracking

---

## 🔄 User Journeys

### Journey 1: Upload & Summarize
```
Login → Dashboard → Upload PDF → AI Summary Generated → View Summary
```

### Journey 2: Ask Questions
```
Document Page → Ask Question → Get AI Answer → View History
```

### Journey 3: Take Test
```
Document Page → Generate Test → Answer Questions → View Results
```

### Journey 4: Track Progress
```
Dashboard → View Progress → Analyze Performance → Set Goals
```

---

## 💰 API Usage & Costs

### Gemini API Integration
- **Summary Generation:** 1 API call per document
- **Q&A:** 1 API call per question
- **Test Generation:** 1 API call per test

### Pricing
- **Free Tier:** 60 requests/minute
- **Cost:** Starts at $0.075 per 1M input tokens
- **Average Cost per User:** ~$0.50-$1.00/month

---

## 🔒 Security Features

- ✅ CSRF Protection
- ✅ XSS Prevention
- ✅ Input Validation & Sanitization
- ✅ Secure Password Hashing
- ✅ Session Management
- ✅ User Data Isolation
- ✅ Login Required Decorators
- ✅ File Upload Validation

---

## 📈 Project Status

### ✅ Fully Functional
- Authentication system
- PDF upload & processing
- AI summary generation
- Q&A system
- Test generation
- Progress tracking
- Responsive UI

### 🔄 Development Mode
- `DEBUG = True` (for development only)
- SQLite database (upgrade to PostgreSQL for production)
- No caching (can add Redis)
- Synchronous AI calls (can add Celery for background tasks)

---

## 🚀 Deployment Guide

### Deploying to Render

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy to production"
   git push origin main
   ```

2. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Connect GitHub repository

3. **Configure Environment**
   - Set `DEBUG=False`
   - Use PostgreSQL instead of SQLite
   - Add environment variables in Render dashboard

4. **Deploy**
   ```bash
   # Render auto-deploys on git push
   ```

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Use PostgreSQL database
- [ ] Enable Redis caching
- [ ] Add Celery for background tasks
- [ ] Set up email backend
- [ ] Configure ALLOWED_HOSTS
- [ ] Use environment variables
- [ ] Enable HTTPS
- [ ] Set up monitoring & logging

---


## 🎓 Use Cases

### For Students 👨‍🎓
- Upload lecture notes and textbooks
- Generate quick summaries for revision
- Ask doubts and get instant answers
- Practice with AI-generated tests
- Track learning progress

### For Professionals 💼
- Summarize long reports and documentation
- Extract key information quickly
- Self-assessment and skill development
- Knowledge management

### For Researchers 🔬
- Analyze research papers
- Quick literature reviews
- Generate study questions
- Organize research materials

---

## 🐛 Troubleshooting

### Issue: Gemini API Error
**Solution:** Check API key in `.env` file and verify quota limits

### Issue: PDF Upload Fails
**Solution:** Ensure file size < 10MB and format is valid PDF

### Issue: Static Files Not Loading
**Solution:** Run `python manage.py collectstatic`

### Issue: Database Errors
**Solution:** Run `python manage.py migrate` again

---

## 📝 Requirements

```
Django==4.2.7
google-generativeai==0.3.2
PyPDF2==3.0.1
python-dotenv==1.0.0
Pillow==10.0.0
```

Full `requirements.txt` available in repository.

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/smartx-study.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   ```

4. **Push to branch**
   ```bash
   git push origin feature/amazing-feature
   ```

5. **Open Pull Request**

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 💬 Support & Feedback

- 📧 Email: ayushkhatri505@example.com
- 🐦 Twitter: [@yourhandle](https://twitter.com/)
- 💼 LinkedIn: [Your Profile](www.linkedin.com/in/ayushkhatri-dev)
- 🐛 Issues: [GitHub Issues](https://github.com/Ayushkhatri-Dev/SmartX-Study/issues)

---

## 🙏 Acknowledgments

- Google Gemini AI for powerful language model
- Django community for excellent framework
- PyPDF2 for PDF processing
- Tailwind CSS for modern styling

---

## 📊 Stats

- **Total Models:** 4
- **Total Views:** 14
- **Templates:** 13 HTML files
- **Database Size:** 872KB (with demo data)
- **API Integration:** Google Gemini (gemini-2.5-flash)
- **Development Time:** Production-ready code

---

## 🎯 Roadmap

### Phase 1 ✅ (Current)
- Basic upload & summarization
- Q&A system
- Test generation
- Progress tracking

### Phase 2 (Planned)
- Video lecture support
- Audio note transcription
- Collaborative study groups
- Advanced analytics dashboard

### Phase 3 (Future)
- Mobile app (React Native)
- Real-time collaboration
- AI-powered study recommendations
- Integration with learning management systems

---

## 📸 Screenshots

[Add your screenshots here]

- Dashboard Overview
- PDF Upload Interface
- AI-Generated Summary
- Q&A Interaction
- Test Generation
- Progress Dashboard

---

**Built with ❤️ by [Ayush khatri]**

⭐ If you find this useful, please star the repository!

---
