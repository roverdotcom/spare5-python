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

    def _make_request(self, verb, *args, **kwargs):
        kwargs.update({
            'auth': (self.username, self.token),
            'headers': {
                'content-type': 'application/json',
            },
        })
        response = requests.request(verb, *args, **kwargs)
        return response.json()

    def _get(self, url, **kwargs):
        return self._make_request('get', url, **kwargs)

    def _post(self, url, data, **kwargs):
        return self._make_request('post', url, data=data, **kwargs)

    def _put(self, url, data, **kwargs):
        return self._make_request('put', url, data=data, **kwargs)

    def _delete(self, url, **kwargs):
        return self._make_request('delete', url, **kwargs)
