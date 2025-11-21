# SmartX Study - Your Smart Assistant

SmartX Study is an AI-powered learning platform that helps students enhance their study experience through intelligent document analysis, automated summarization, interactive Q&A, and personalized testing.

## Features

### Core Functionality
- **PDF Document Upload & Analysis**: Upload study materials and get AI-powered text extraction and analysis
- **Intelligent Summaries**: Get comprehensive summaries highlighting key concepts and important details
- **Interactive Q&A**: Ask questions about your documents and receive detailed, contextual answers
- **Smart Testing**: Generate personalized tests with automatic scoring and progress tracking
- **Progress Tracking**: Monitor your learning journey with detailed analytics and performance insights

### User Experience
- **Modern UI/UX**: Clean, responsive design optimized for all devices
- **Secure Authentication**: Django's built-in authentication system with form validation
- **Real-time Processing**: Instant feedback and processing status updates
- **Progress Visualization**: Track performance trends and study statistics

## Technology Stack

- **Backend**: Django 4.2.7 (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **AI Integration**: Google Gemini API for text analysis and generation
- **Database**: SQLite (easily upgradeable to PostgreSQL)
- **File Processing**: PyPDF2 for PDF text extraction
- **Authentication**: Django's built-in authentication system

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Google Gemini API key

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd smartx-study
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file and add your configuration:
   ```
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   GEMINI_API_KEY=your-gemini-api-key
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser** (Optional)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to access the application.

## Getting Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

## Usage Guide

### Getting Started
1. **Sign Up**: Create a new account with your email and password
2. **Dashboard**: Access your personalized dashboard after login
3. **Upload Documents**: Upload PDF study materials (max 10MB)
4. **AI Processing**: Wait for automatic text extraction and summarization

### Core Features
1. **Document Analysis**:
   - Upload PDF files with study materials
   - Get AI-generated summaries of key concepts
   - View processing status and document details

2. **Q&A Sessions**:
   - Ask specific questions about your documents
   - Receive contextual answers based on document content
   - Review previous Q&A history

3. **Testing System**:
   - Generate multiple-choice tests from document content
   - Take tests with immediate scoring
   - Track performance and view detailed results

4. **Progress Tracking**:
   - Monitor study statistics and performance trends
   - View test history and improvement over time
   - Access detailed analytics dashboard

## Project Structure

```
smartx_study/
├── core/                   # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Form definitions
│   ├── utils.py           # Utility functions (AI integration)
│   └── urls.py            # URL routing
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── core/             # App-specific templates
│   └── registration/     # Authentication templates
├── static/               # Static files
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript files
├── media/               # User uploaded files
├── smartx_study/        # Django project settings
└── manage.py           # Django management script
```

## Database Models

- **Document**: Stores uploaded PDF files and processed content
- **QASession**: Manages question-answer pairs for each document
- **Test**: Contains AI-generated test questions
- **TestAttempt**: Records user test attempts and scores

## API Integration

The application integrates with Google's Gemini API for:
- **Text Summarization**: Creating intelligent summaries of document content
- **Question Answering**: Providing contextual answers based on document content
- **Test Generation**: Creating relevant multiple-choice questions

## Security Features

- CSRF protection on all forms
- User authentication and session management
- File upload validation and size limits
- SQL injection protection through Django ORM
- XSS protection through template escaping

## Future Enhancements

### Planned Features
- **Topic Visualization**: Interactive diagrams and mind maps
- **Voice-over Explanations**: AI-powered audio explanations
- **Multi-format Support**: Support for additional file formats
- **Collaborative Study**: Shared documents and group studies
- **Advanced Analytics**: Detailed learning insights and recommendations

### Technical Improvements
- PostgreSQL database integration
- Redis caching for improved performance
- Celery for background task processing
- Docker containerization
- AWS/Azure deployment options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, questions, or feedback:
- Create an issue on GitHub
- Contact the development team
- Check the documentation and FAQ

## Acknowledgments

- Google Gemini API for AI capabilities
- Django community for the excellent framework
- Tailwind CSS for the styling framework
- Font Awesome for icons