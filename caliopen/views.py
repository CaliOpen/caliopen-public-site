from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/layout/home.pt')
def my_view(request):
    return {'project': 'caliopen',
			'page_description': 'Description de Caliopen',
			'page_title': 'Site vitrine de Caliopen',
			'page_author': 'Gandi'}
