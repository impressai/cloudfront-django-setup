from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def static_cdn(url):
    if settings.CDN_ENABLED:
        return static(url).replace(settings.AWS_S3_CUSTOM_DOMAIN, settings.AWS_S3_DOMAIN)
    else:
        return static(url)
