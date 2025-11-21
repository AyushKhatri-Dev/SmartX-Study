"""
WSGI config for smartx_study project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartx_study.settings')

application = get_wsgi_application()