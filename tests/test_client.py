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
        thingy = Thingiverse()
        search_res = thingy.search("RPi 4")

        with open("search_res.json", "w") as f:
            json.dump(search_res, f)
