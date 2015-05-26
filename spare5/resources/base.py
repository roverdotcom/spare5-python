class Resource(object):
    _result = None
    client = None
    resource_id = None
    list_resource = None

    def __init__(
            self, client, resource_id=None, list_resource=None, result=None):
        self.client = client
        if result is not None:
            self._result = result
        self.resource_id = resource_id
        self.list_resource = list_resource

    @property
    def url(self):
        if self._result is not None:
            return self._result['url']
        return '{}/{}'.format(self.list_resource.url, self.resource_id)

    def get(self, force_refresh=False):
        if self._result is None or force_refresh:
            self._result = self.client._get(self.url)['result']
        return self._result

    def update(self, **kwargs):
        return self.client._put(self.url, data=kwargs)


class ListResource(object):
    _result = None
    next_url = None

    def __init__(self, client, parent=None):
        self.client = client

    def __iter__(self):
        if not hasattr(self, '_resource_class'):
            raise NotImplementedError()

        if self._result is None:
            self.list()
        while True:
            for result in self._result:
                yield self._resource_class(
                    self.client, list_resource=self, result=result)
            if self.has_next:
                self.next_page()
            else:
                break
        # Reset to initial state for repeated iteration support
        self._result = None

    def create(self, headers=None, data=None, **kwargs):
        if data is None:
            data = kwargs
        return self.client._post(self.url, headers=headers, data=data)

    def _load_page(self, url):
        result = self.client._get(url)
        self._result = result['result']
        self.next_url = result.get('next')

    def list(self, force_refresh=False):
        if self._result is None or force_refresh:
            self._load_page(self.url)
        return self._result

    def next_page(self):
        if self.has_next:
            self._load_page(self.next_url)
        else:
            self._result = []
        return self._result

    @property
    def has_next(self):
        return self.next_url is not None


class MethodNotAllowedException(StandardError):
    pass
