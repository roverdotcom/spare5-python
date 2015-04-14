from .base import ListResource
from .base import Resource
from .base import MethodNotAllowedException


class Response(Resource):
    def update(self, **kwargs):
        raise MethodNotAllowedException()


class Responses(ListResource):
    _resource_class = Response

    def __init__(self, client, parent):
        super(Responses, self).__init__(client)
        self.job = parent

    @property
    def url(self):
        return '{}/{}'.format(self.job.url, 'responses')

    def create(self, **kwargs):
        raise MethodNotAllowedException()


class BatchResponses(ListResource):
    _resource_class = Response

    def __init__(self, client, parent):
        super(BatchResponses, self).__init__(client)
        self.batch = parent

    @property
    def url(self):
        return '{}/{}'.format(self.batch.url, 'responses')

    def create(self, **kwargs):
        raise MethodNotAllowedException()
