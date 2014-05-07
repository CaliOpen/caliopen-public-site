from pyramid.view import view_config
# from pyramid.i18n import TranslationString


@view_config(route_name='home', renderer='templates/layout/home.pt')
def my_view(request):
    return {
        'project': 'caliopen',
        'page_description': 'CaliOpen, be safe.',
        'page_title': 'CaliOpen, be safe.',
        'page_author': 'Gandi'
    }


@view_config(route_name='contact', renderer='templates/layout/contact.pt')
def contact(request):
    # ts = TranslationString('Add')

    return {
        'project': 'caliopen',
        'page_description': 'CaliOpen, be safe.',
        'page_title': 'CaliOpen, be safe.',
        'page_author': 'Gandi'
    }

@view_config(route_name='features', renderer='templates/layout/features.pt')
def features(request):
    return {
        'project': 'caliopen',
        'page_description': 'CaliOpen, be safe.',
        'page_title': 'CaliOpen, be safe.',
        'page_author': 'Gandi'
    }
