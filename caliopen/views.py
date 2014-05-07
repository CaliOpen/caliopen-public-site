from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/layout/home.pt')
def my_view(request):
    return {
        'project': 'caliopen',
		'page_description': 'CaliOpen, be safe.',
		'page_title': 'CaliOpen, be safe.',
		'page_author': 'Gandi'
    }
