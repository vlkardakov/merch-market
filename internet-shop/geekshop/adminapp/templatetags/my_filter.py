from django import template

register = template.Library()


@register.filter(name="admin_title")
def sample_text(string):
    return f"Aдминка {string}"
