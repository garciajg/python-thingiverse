from thingiverse.types.search import SearchResponse
from typing import Optional, Text
from requests.models import Response
from box import Box
import requests


class Thingiverse(object):
    def __init__(self, access_token=None):
        self.base_url = "https://api.thingiverse.com"
        self.oauth_url = "https://www.thingiverse.com/login/oauth/authorize"
        self.access_token = access_token

    def authorize(self,
                  client_id: Text,
                  redirect_uri: Optional[Text] = None,
                  response_type: Optional[Text] = None) -> Response:
        url = self.oauth_url + f"?client_id={client_id}"
        if redirect_uri:
            url += f"&redirect_url={redirect_uri}"
        if response_type:
            url += f"&response_type={response_type}"
        
        print(url)

        res = requests.get(url, allow_redirects=True)
        print("URL")
        print(res.url)
        if res.url != url:
            new_res = requests.get(res.url, allow_redirects=True)
            print("New res")
            print(new_res.url)

        return res


    def search(self, term: Text) -> Box:
        path = f"/search/{term}/?access_token={self.access_token}"
        url = self.base_url + path
        try:
            res = requests.get(url)
            res_json = res.json()
            search_box = Box(res_json)

            return search_box
        except Exception as e:
            print(e)
            raise e
