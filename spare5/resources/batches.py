from .base import Resource
from .base import ListResource
from .base import MethodNotAllowedException

from .jobs import Jobs


class Batch(Resource):

    @property
    def jobs(self):
        return Jobs(self.client, self)

    def update(self, **kwargs):
        raise MethodNotAllowedException()


class Batches(ListResource):
    REQUIRED_PARAMS = ('name', 'reward', 'job_type')
    _resource_class = Batch

    @property
    def url(self):
        return '{}/{}'.format(self.client.api_root, 'job_batches')

    def batch(self, batch_id):
        return Batch(self.client, batch_id, self)
