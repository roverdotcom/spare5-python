from .base import ListResource


class Job(object):
    STAR_RATING = 'STARRATING'

    JOB_TYPES = (STAR_RATING,)


class Jobs(ListResource):
    REQUIRED_PARAMS = ('num_responders',)

    @property
    def url(self):
        return '/'.join((self.client.api_root, 'jobs'))

    def get(self, reference_id):
        pass
