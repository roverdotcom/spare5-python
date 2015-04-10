class Resource(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        return self.client._get(self.url)['result']

    def update(self, **kwargs):
        return self.client._put(self.url, data=kwargs)


class ListResource(object):
    def __init__(self, client):
        self.client = client

    def __iter__(self):
        raise NotImplementedError()

    def create(self, **kwargs):
        return self.client._post(self.url, data=kwargs)

    def list(self):
        response = self.client._get(self.url)['result']
        return response
