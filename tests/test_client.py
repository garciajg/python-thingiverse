from unittest import TestCase
from thingiverse import Thingiverse
import json

class TestAuth(TestCase):

    def test_oauth_endpoint(sekf):
        # TODO
        # thingy = Thingiverse()
        # auth = thingy.authorize(client_id="1fc790755dcd79c17305", response_type="token")
        # print(auth.url)
        # print(auth.json())
        pass

    def test_search(self):
        thingy = Thingiverse(access_token="bf62d0cf23790de6d78acd2657550be3")
        search_res = thingy.search("RPi 4")

        with open("search_res_two.json", "w") as f:
            json.dump(search_res, f)
        assert search_res.total != 0
        assert search_res.hits
