from pyramid.config import Configurator
from . import views
from .lang import locale_negotiator


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
    config.add_route('faq', '/faq')
    config.scan()

    return config.make_wsgi_app()
