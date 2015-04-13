import json
from .base import Resource
from .base import ListResource
from .base import MethodNotAllowedException

from .responses import Responses


class Job(Resource):
    STAR_RATING = 'STARRATING'

    JOB_TYPES = (STAR_RATING,)

    def update(self, **kwargs):
        raise MethodNotAllowedException()

    @property
    def responses(self):
        return Responses(self.client, self)


class Jobs(ListResource):
    REQUIRED_PARAMS = ('num_responders',)
    _resource_class = Job

    def __init__(self, client, batch, result=None):
        super(Jobs, self).__init__(client)
        self.batch = batch

    @property
    def url(self):
        return '{}/{}'.format(self.batch.url, 'jobs')

    def job(self, job_id):
        return Job(self.client, job_id, self)

    def create(self, num_responders, questions, **kwargs):
        data = {
            'num_responders': num_responders,
            'questions': questions,
        }
        data.update(kwargs)
        return super(Jobs, self).create(
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'},
        )
