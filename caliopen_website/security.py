"""
The Root Context

used when a view did not declare it's own context.
"""
import logging

from pyramid.httpexceptions import HTTPMovedPermanently
from pyramid.settings import asbool

log = logging.getLogger(__name__)


class RootContext(object):
    """
    Force redirect to https
    """

    def __init__(self, request):
        settings = request.registry.settings
        if not asbool(settings.get('caliopen_ws.force_https', '0')):
            return
        if request.environ.get('REQUEST_SCHEME') != 'https':
            url = "https://" + request.host + request.path_qs
            log.debug('Redirect to %s' % url)
            raise HTTPMovedPermanently(location=url)
        self.request = request
