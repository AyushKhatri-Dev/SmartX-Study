from django.contrib import admin
from .models import Document, QASession, Test, TestAttempt


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_processed', 'uploaded_at']
    list_filter = ['is_processed', 'uploaded_at', 'user']
    search_fields = ['title', 'user__username']
    readonly_fields = ['id', 'uploaded_at', 'updated_at']


@admin.register(QASession)
class QASessionAdmin(admin.ModelAdmin):
    list_display = ['document', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['question', 'answer', 'document__title']
    readonly_fields = ['id', 'created_at']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'document', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'document__title']
    readonly_fields = ['id', 'created_at']


@admin.register(TestAttempt)
class TestAttemptAdmin(admin.ModelAdmin):
    list_display = ['test', 'user', 'score', 'total_questions', 'percentage', 'completed_at']
    list_filter = ['completed_at', 'user']
    search_fields = ['test__title', 'user__username']
    readonly_fields = ['id', 'completed_at', 'percentage']