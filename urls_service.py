from constants import BASE_URL
import requests
from Singleton import Singleton
from credentials import CSRF_TOKEN, COOKIE

@Singleton
class UrlService:
    HEADERS = {
        'x-csrf-token': CSRF_TOKEN,
        'cookie': COOKIE
    }
    FILTERS = {
        'status': 'solved'
    }
    def __init__(self):
        return

    def get_track_request(self, track):
        URL = BASE_URL + "tracks/" + track + "/challenges"
        PARAMS = {
            'offset': 0,
            'limit': 500,
            'filters': self.FILTERS,
        }
        try:
            get_track = requests.get(url=URL, params=PARAMS, headers=self.HEADERS)
        except Exception as e:
            e.track = track
            raise e
        return get_track

    def get_submissions_request(self, chal_slug):
        PARAMS = {
            'offset': '0',
            'limit': '20'
        }
        URL = BASE_URL + "challenges/" + chal_slug + "/submissions/?offset=" + PARAMS.get(
            'offset') + "&limit=" + PARAMS.get('limit')
        try:
            submissions = requests.get(url=URL, headers=self.HEADERS)
        except Exception as e:
            e.track = chal_slug
            raise e
        return submissions

    def get_particular_submission(self, chal_slug, sub_id):
        URL = BASE_URL + "challenges/" + chal_slug + "/submissions/" + str(sub_id)
        try:
            code_res = requests.get(url=URL, headers=self.HEADERS)
        except Exception as e:
            e.track = chal_slug
            raise e
        return code_res