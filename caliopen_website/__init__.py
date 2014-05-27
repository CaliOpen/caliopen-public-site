from pyramid.config import Configurator
from . import views


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
    if request.accept_language:
        locale = request.accept_language.best_match(LANGUAGES)
        locale = LANGUAGES.get(locale, 'en')
    return locale


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
                          root_factory='caliopen_website.security.RootContext',
                          locale_negotiator=locale_negotiator)

    views.use_less = settings['caliopen_ws.css'] == 'less'

    config.add_static_view('assets', 'assets', cache_max_age=3600)
    config.add_translation_dirs('locale/')
    config.add_route('home', '/')
    config.add_route('contact', '/contact')
    config.add_route('features', '/features')
    config.add_route('about', '/about')
    config.add_route('tour', '/tour')
    config.scan()

    return config.make_wsgi_app()
