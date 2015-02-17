from .base import ListResource


class Job(object):
    STAR_RATING = 'STARRATING'

    JOB_TYPES = (STAR_RATING,)


class Jobs(ListResource):
    REQUIRED_PARAMS = ('num_responders',)

    @property
    def url(self):
        return '/'.join((self.client.api_root, 'jobs'))

    def create(self, data):
        """
        Since the API for jobs is minimally defined, keep it flexible for now.
        """
        self.client._post(self.url, data)

    def list(self):
        self.client._get(self.url)

    def get(self, reference_id):
        pass
