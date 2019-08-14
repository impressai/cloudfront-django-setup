from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def static_cdn(url):
    if settings.CDN_ENABLED:
        return static(url).replace("/static/", "/")
    else:
        return static(url)
