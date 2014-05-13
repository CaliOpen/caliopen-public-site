from pyramid.view import view_config
# from pyramid.i18n import TranslationString

project = 'caliopen'
page_description = 'CaliOpen, be safe.'
page_title = 'CaliOpen, be safe.'
page_author = 'Gandi'


@view_config(route_name='home', renderer='templates/layout/home.jinja2')
def home(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author
    }


@view_config(route_name='contact', renderer='templates/layout/contact.jinja2')
def contact(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author,
        'active_nav': 'contact'
    }


@view_config(route_name='features', renderer='templates/layout/features.jinja2')
def features(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author,
        'active_nav': 'features'
    }


@view_config(route_name='about', renderer='templates/layout/about.jinja2')
def about(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author,
        'active_nav': 'about'
    }


@view_config(route_name='tour', renderer='templates/layout/tour.jinja2')
def tour(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author,
        'active_nav': 'take_a_tour'
    }
