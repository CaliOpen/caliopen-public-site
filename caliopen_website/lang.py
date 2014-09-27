
LANGUAGES = {
        'en-CA': 'en',
        'en-GB': 'en',
        'en-US': 'en',
        'en': 'en',
        'fr-FR': 'fr',
        'fr-BE': 'fr',
        'fr': 'fr',
        }


def locale_negotiator(request):
    """Locale negotiator base on the `Accept-Language` header"""
    locale = 'en'
    if 'lang' in request.params:
        return request.params['lang']
    if request.accept_language:
        locale = request.accept_language.best_match(LANGUAGES)
        locale = LANGUAGES.get(locale, 'en')
    return locale
