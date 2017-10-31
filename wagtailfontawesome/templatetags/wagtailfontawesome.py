from django import template
from django.conf import settings
from django.utils.html import format_html, mark_safe

register = template.Library()


@register.simple_tag
def fontawesome_css():
    """
    Return the URL to the Font Awesome CSS.
    """
    return format_html(
        mark_safe(
            '<link rel="stylesheet" href="{static}wagtailfontawesome/css/fontawesome.css">'.format(
                static=settings.STATIC_URL,
            )
        )
    )
