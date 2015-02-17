class Resource(object):
    def __init__(self, client):
        self.client = client


class ListResource(object):
    def __init__(self, client):
        self.client = client

    def __iter__(self):
        raise NotImplementedError()
