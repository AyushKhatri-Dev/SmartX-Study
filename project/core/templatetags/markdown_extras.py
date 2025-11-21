from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    """
    Convert markdown-style text to HTML
    """
    if not text:
        return ''

    # Convert headers
    text = re.sub(r'^### (.*?)$', r'<h3 class="text-xl font-bold text-gray-900 mt-6 mb-3">\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1 class="text-3xl font-bold text-gray-900 mt-8 mb-4">\1</h1>', text, flags=re.MULTILINE)

    # Convert bold text
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong class="font-semibold text-gray-900">\1</strong>', text)

    # Convert italic text
    text = re.sub(r'\*(.*?)\*', r'<em class="italic">\1</em>', text)

    # Convert unordered lists
    text = re.sub(r'^\* (.*?)$', r'<li class="ml-6 mb-2 list-disc">\1</li>', text, flags=re.MULTILINE)

    # Wrap consecutive list items in <ul>
    text = re.sub(r'(<li class="ml-6 mb-2 list-disc">.*?</li>\n?)+', lambda m: f'<ul class="my-3">{m.group(0)}</ul>', text, flags=re.DOTALL)

    # Convert line breaks to <br> but preserve spacing
    text = re.sub(r'\n\n', '<br><br>', text)
    text = re.sub(r'\n', '<br>', text)

    # Convert horizontal rules
    text = re.sub(r'^---$', r'<hr class="my-6 border-gray-300">', text, flags=re.MULTILINE)

    return mark_safe(text)
