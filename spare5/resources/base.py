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

    def __init__(self, client, parent):
        self.client = client

    def __iter__(self):
        if not hasattr(self, '_resource_class'):
            raise NotImplementedError()

        if self._result is None:
            self.list()
        for result in self._result:
            yield self._resource_class(
                self.client, list_resource=self, result=result)

    def create(self, headers=None, data=None, **kwargs):
        if data is None:
            data = kwargs
        return self.client._post(self.url, headers=headers, data=data, **kwargs)

    def list(self, force_refresh=False):
        if self._result is None or force_refresh:
            self._result = self.client._get(self.url)['result']
        return self._result


class MethodNotAllowedException(StandardError):
    pass
