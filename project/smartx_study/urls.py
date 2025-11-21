"""
URL configuration for smartx_study project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Simple view to return empty response for sw.js and favicon.ico
def empty_response(request):
    return HttpResponse(status=204)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sw.js', empty_response),  # Handle service worker request
    path('favicon.ico', empty_response),  # Handle favicon request
    path('', include('core.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)