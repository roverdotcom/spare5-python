from .base import Resource
from .base import ListResource

from .responses import Responses


class Job(Resource):
    STAR_RATING = 'STARRATING'

    JOB_TYPES = (STAR_RATING,)

    def __init__(self, client, job_id, jobs):
        super(Job, self).__init__(client)
        self.job_id = job_id
        self.jobs = jobs
        self.responses = Responses(client, self)

    @property
    def url(self):
        return '{}/{}'.format(self.jobs.url, self.job_id)


class Jobs(ListResource):
    REQUIRED_PARAMS = ('num_responders',)

    def __init__(self, client, batch):
        super(Jobs, self).__init__(client)
        self.batch = batch

    @property
    def url(self):
        return '{}/{}'.format(self.batch.url, 'jobs')

    def job(self, job_id):
        return Job(self.client, job_id, self)
