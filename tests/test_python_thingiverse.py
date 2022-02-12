from thingiverse.types.exceptions import (
    ResourceNotFound, SearchException,
    UnathenticatedException, ThingiverseException
)
from thingiverse import Thingiverse
from unittest import TestCase
from dotenv import load_dotenv
import os
load_dotenv()

ACCESS_TOKEN = os.getenv("THINGI_ACCESS_TOKEN")
assert ACCESS_TOKEN


class TestSearch(TestCase):

    def test_init_client(self):
        """Test Thigiverse() initialization with access_token"""
        # Testing without access token
        with self.assertRaises(UnathenticatedException) as raised:
            Thingiverse()
        exception = raised.exception
        self.assertEqual(exception.args[0],
                         "'access_token' not provided", "Access token was required")

    def test_fetching_thing_by_id(self):
        """Test get_thing_by_id() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # Searching without thing_id (Should fail)
        with self.assertRaises(ThingiverseException) as raised:
            thingy.get_thing_by_id()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'thing_id' is required", "thing_id was required")

        # Testing with invalid thing_id
        thing_id = -922740
        with self.assertRaises(ResourceNotFound) as raised:
            thingy.get_thing_by_id(thing_id=thing_id)
        exception = raised.exception
        self.assertEqual(exception.args[0],
                         f"Thing with id {thing_id} not found.",
                         "thing_id was not found")

        # Successfull requests
        thing_id = 922740
        thing_res = thingy.get_thing_by_id(thing_id=thing_id)

        assert thing_res
        assert thing_res.name
        assert thing_res.id == thing_id

    def test_fetching_images_by_thing(self):
        """Test get_images_by_thing() method"""
        thing_id = 922740
        thingy = Thingiverse(access_token=ACCESS_TOKEN)

        # Fetching without thing_id (Should fail)
        with self.assertRaises(ThingiverseException) as raised:
            thingy.get_images_by_thing()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'thing_id' is required", "thing_id was required")

        # Fetching with image_size and not image_type
        # based on their API, this should fail
        with self.assertRaises(ThingiverseException) as raised:
            thingy.get_images_by_thing(thing_id=thing_id,
                                       image_size="large")
        exception = raised.exception
        self.assertEqual(exception.args[0],
                         "'image_type' is required is 'image_size' is given",
                         "thing_id was required")

        # Testing with invalid id
        with self.assertRaises(ResourceNotFound) as raised:
            thing_res = thingy.get_images_by_thing(thing_id=-thing_id)
        exception = raised.exception
        self.assertEqual(exception.args[0],
                         f"Thing with id {-thing_id} not found.",
                         "thing_id was not found")

        # Successful requests
        thing_res = thingy.get_images_by_thing(thing_id=thing_id)

        assert thing_res
        assert thing_res[0]["name"]

        # Successful request with image_size and image_type
        thing_res = thingy.get_images_by_thing(thing_id=thing_id,
                                               image_size="large",
                                               image_type="preview")

        assert thing_res
        assert thing_res[0]["name"]

    def test_search_term(self):
        """Test search_term() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
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
        """Test search_tag() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # Searching without tag (Should fail)
        with self.assertRaises(SearchException) as raised:
            thingy.search_tag()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'tag' is required", "tag was required")

        search_res = thingy.search_tag("tag")
        assert search_res.total != 0
        assert search_res.hits
