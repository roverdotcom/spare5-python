from .base import Resource
from .base import ListResource

from .jobs import Jobs


class Batch(Resource):
    def __init__(self):
        self.jobs = Jobs()


class Batches(ListResource):
    REQUIRED_PARAMS = ('name', 'reward', 'job_type')

    @property
    def url(self):
        return '/'.join((self.client.api_root, 'job_batches'))
