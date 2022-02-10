from unittest import TestCase
from thingiverse import Thingiverse
import json


class TestSearch(TestCase):

    def test_search_term(self):
        thingy = Thingiverse(access_token="bf62d0cf23790de6d78acd2657550be3")
        search_res = thingy.search_term("RPi 4")

        with open("search_term.json", "w") as f:
            json.dump(search_res, f)
        assert search_res.total != 0
        assert search_res.hits

    def test_search_tag(self):
        thingy = Thingiverse(access_token="bf62d0cf23790de6d78acd2657550be3")
        search_res = thingy.search_tag("tag")

        with open("search_tag.json", "w") as f:
            json.dump(search_res, f)

        assert search_res.total != 0
        assert search_res.hits
