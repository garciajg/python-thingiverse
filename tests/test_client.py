from thingiverse.types.exceptions import SearchException, UnathenticatedException
from thingiverse import Thingiverse
from unittest import TestCase


class TestSearch(TestCase):

    def test_init_client(self):
        # Testing without access token
        with self.assertRaises(UnathenticatedException) as raised:
            Thingiverse()
        exception = raised.exception
        self.assertEqual(exception.args[0],
                         "'access_token' not provided", "Access token was required")

    def test_search_term(self):
        thingy = Thingiverse(access_token="bf62d0cf23790de6d78acd2657550be3")
        # Searching without term (Should fail)
        with self.assertRaises(SearchException) as raised:
            thingy.search_term()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'term' is required", "term was required")

        # Successfull requests
        search_res = thingy.search_term("RPi 4")
        assert search_res.total != 0
        assert search_res.hits

    def test_search_tag(self):
        thingy = Thingiverse(access_token="bf62d0cf23790de6d78acd2657550be3")
        # Searching without tag (Should fail)
        with self.assertRaises(SearchException) as raised:
            thingy.search_tag()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'tag' is required", "tag was required")

        search_res = thingy.search_tag("tag")
        assert search_res.total != 0
        assert search_res.hits

    def test_search_tag(self):
        thingy = Thingiverse(access_token="bf62d0cf23790de6d78acd2657550be3")
        search_res = thingy.search_tag("tag")

        with open("search_tag.json", "w") as f:
            json.dump(search_res, f)

        assert search_res.total != 0
        assert search_res.hits
