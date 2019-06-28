from django import template
import os

register = template.Library()

@register.filter('imgnames')
def imgnames(value):
    path, filename = os.path.split(str(value))
    basename, extension = os.path.splitext(filename)
    return basename