from django import template
from django.utils.html import mark_safe
import re

register = template.Library()

@register.filter
def highlight_query(text, search_query):
    highlighted_text = re.sub(
        re.escape(search_query),
        lambda match: f'<span class="highlighted">{match.group(0)}</span>',
        text,
    )
    return mark_safe(highlighted_text)


