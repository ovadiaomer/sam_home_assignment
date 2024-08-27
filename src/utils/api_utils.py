import requests


class ApiUtils:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get(self, timeout=5):
        try:
            response = requests.get(self.url, headers=self.headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            raise e
