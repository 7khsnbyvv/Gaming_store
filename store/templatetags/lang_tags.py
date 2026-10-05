from django import template

from store.translations import DEFAULT_LANG, LANG_INDEX, get_text

register = template.Library()


def _lang(context):
    request = context.get('request')
    if request is None:
        return DEFAULT_LANG
    lang = request.session.get('lang', DEFAULT_LANG)
    return lang if lang in LANG_INDEX else DEFAULT_LANG


@register.simple_tag(takes_context=True)
def t(context, key):
    return get_text(_lang(context), key)


@register.simple_tag(takes_context=True)
def current_lang(context):
    return _lang(context)