from pyramid.view import view_config
# from pyramid.i18n import TranslationString

project = 'caliopen'
page_description = 'CaliOpen, be safe.'
page_title = 'CaliOpen, be safe.'
page_author = 'Gandi'


@view_config(route_name='home', renderer='templates/layout/home.pt')
def home(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author
    }


@view_config(route_name='contact', renderer='templates/layout/contact.pt')
def contact(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author
    }


@view_config(route_name='features', renderer='templates/layout/features.pt')
def features(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author
    }


@view_config(route_name='about', renderer='templates/layout/about.pt')
def about(request):
    return {
        'project': project,
        'page_description': page_description,
        'page_title': page_title,
        'page_author': page_author
    }


@view_config(route_name='tour', renderer='templates/layout/tour.pt')
def tour(request):
    return {
        'project': 'caliopen',
        'page_description': 'CaliOpen, be safe.',
        'page_title': 'CaliOpen, be safe.',
        'page_author': 'Gandi'
    }
