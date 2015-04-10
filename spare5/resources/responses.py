from .base import ListResource


class Responses(ListResource):
    def __init__(self, client, job):
        super(Responses, self).__init__(client)
        self.job = job

    @property
    def url(self):
        return '{}/{}'.format(self.job.url, 'responses')
