from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    path('learn-more/', views.learn_more, name='learn_more'),
    
    # Authentication
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Dashboard and main features
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_document, name='upload_document'),
    path('document/<uuid:document_id>/', views.document_detail, name='document_detail'),
    path('document/<uuid:document_id>/qa/', views.qa_session, name='qa_session'),
    path('document/<uuid:document_id>/test/', views.generate_test, name='generate_test'),
    path('test/<uuid:test_id>/', views.take_test, name='take_test'),
    path('test/<uuid:test_id>/submit/', views.submit_test, name='submit_test'),
    path('test-result/<uuid:attempt_id>/', views.test_result, name='test_result'),
    path('progress/', views.progress_tracking, name='progress_tracking'),
]