from django import template

register = template.Library()

@register.filter
def test(value, arg):
    return ('hello ' + value + '<br>  ')*int(arg)