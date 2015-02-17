import requests

from .resources.batches import Batches
from .resources.jobs import Jobs

DEFAULT_API_ROOT = 'http://app.spare5.com/partner/v2'


class Spare5Client(object):
    def __init__(self, username, token, api_root=DEFAULT_API_ROOT):
        super(Spare5Client, self).__init__()

        self.api_root = api_root
        self.username = username
        self.token = token

        self.batches = Batches(self)
        self.jobs = Jobs(self)

    def _make_request(self, verb, *args, **kwargs):
        kwargs.update({
            'auth': (self.username, self.token)
        })
        response = getattr(requests, verb)(*args, **kwargs)
        return response.json()

    def _get(self, url):
        return self._make_request('get', url)

    def _post(self, url, data):
        return self._make_request('post', url, data=data)

    def _put(self, url, data):
        return self._make_request('put', url, data=data)

    def _delete(self, url):
        return self._make_request('delete', url)
