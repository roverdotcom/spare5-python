from .base import Resource
from .base import ListResource
from .base import MethodNotAllowedException

from .jobs import Jobs


class Batch(Resource):
    
    def __init__(self, client, batch_id, batches):
        super(Batch, self).__init__(client)
        self.batch_id = batch_id
        self.batches = batches
        self.jobs = Jobs(client, self)

    @property
    def url(self):
        return '{}/{}'.format(self.batches.url, self.batch_id)

    def update(self, **kwargs):
        raise MethodNotAllowedException()


class Batches(ListResource):
    REQUIRED_PARAMS = ('name', 'reward', 'job_type')

    @property
    def url(self):
        return '{}/{}'.format(self.client.api_root, 'job_batches')

    def batch(self, batch_id):
        return Batch(self.client, batch_id, self)
