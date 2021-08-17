from django import template
from ..models import Cat

register = template.Library()

@register.inclusion_tag('root/nav.html')
def nav():
  return {
    "nav": Cat.objects.all()
  }