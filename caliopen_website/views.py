import os

from pyramid.view import view_config
from .lang import locale_negotiator

project = 'caliopen'
page_description = 'CaliOpen, be safe.'
page_title = 'CaliOpen, be safe.'
page_author = 'Gandi'
use_less = False

_here = os.path.dirname(__file__)


@view_config(route_name='home', renderer='templates/layout/home.jinja2')
def home(request):
    return {
        'project': project,
        'page_author': page_author,
        'use_less': use_less
    }


@view_config(route_name='contact', renderer='templates/layout/contact.jinja2')
def contact(request):
    return {
        'project': project,
        'page_author': page_author,
        'active_nav': 'contact',
        'use_less': use_less
    }


@view_config(route_name='features', renderer='templates/layout/features.jinja2')
def features(request):
    return {
        'project': project,
        'page_author': page_author,
        'active_nav': 'features',
        'use_less': use_less
    }


@view_config(route_name='about', renderer='templates/layout/about.jinja2')
def about(request):
    return {
        'project': project,
        'page_author': page_author,
        'active_nav': 'about',
        'use_less': use_less
    }


@view_config(route_name='tour', renderer='templates/layout/tour.jinja2')
def tour(request):
    return {
        'project': project,
        'page_author': page_author,
        'active_nav': 'take_a_tour',
        'use_less': use_less
    }


@view_config(route_name='faq', renderer='templates/layout/faq.jinja2')
def faq(request):
    # Well faq is not in .po file, use raw html
    lang = locale_negotiator(request)
    f_name = os.path.join(
             _here, 'assets', 'data', 'faq_%s.html' % lang)
    if not os.path.isfile(f_name):
        # default to fr for the moment
        f_name = os.path.join(
             _here, 'assets', 'data', 'faq_fr.html')
    content = open(f_name).read().decode('utf-8')
    return {
        'project': project,
        'page_author': page_author,
        'active_nav': 'faq',
        'use_less': use_less,
        'faq_content': content
    }
