from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value, args):
    """
    This cut function cuts all the values of "args" from the string!
    """
    return value.replace(args, " ")

# register.filter('cut', cut)

