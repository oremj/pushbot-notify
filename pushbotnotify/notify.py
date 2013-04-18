import requests


class Notifier:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key

    def notify(self, msg, timeout=2, raise_exceptions=False):
        try:
            requests.post(self.endpoint,
                          data={'api_key': self.api_key,
                                'msg': msg},
                          timeout=timeout)
        except Exception:
            if raise_exceptions:
                raise
