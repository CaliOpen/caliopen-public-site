from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'caliopen')

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_translation_dirs('locale/')
    config.add_route('home', '/')
    config.add_route('contact', '/contact')
    config.add_route('features', '/features')
    config.add_route('about', '/about')
    config.add_route('tour', '/tour')
    config.scan()

    return config.make_wsgi_app()
