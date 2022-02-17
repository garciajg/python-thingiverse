from thingiverse.types.exceptions import UserException
from thingiverse import Thingiverse
from unittest import TestCase
from dotenv import load_dotenv
import os
load_dotenv()

ACCESS_TOKEN = os.getenv("THINGI_ACCESS_TOKEN")
assert ACCESS_TOKEN


class TestThingiverseUsers(TestCase):

    def test_get_user_by_username(self):
        """Test get_user_by_username() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing fetching without `username` param
        # It should default to `me`
        user = thingy.get_user_by_username()

        assert user
        assert user.id

        # Successfull requests with username
        user = thingy.get_user_by_username(username=username)

        assert user
        assert user.id
        assert user.name == username

    def test_get_users_data(self):
        """test get_users_data() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing failing request
        with self.assertRaises(UserException) as raised:
            thingy.get_users_data()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'username' is required", "username was required")

        # Successfull requests with username
        user = thingy.get_users_data(username=username)

        assert user
        assert isinstance(user.total, int)
        assert isinstance(user.hits, list)

        # Successfull request with username and term
        user = thingy.get_users_data(username=username, term="RPi")

        assert user
        assert isinstance(user.total, int)
        assert isinstance(user.hits, list)

    def test_get_users_things(self):
        """test get_username_things() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing failing request
        with self.assertRaises(UserException) as raised:
            thingy.get_username_things()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'username' is required", "username was required")

        # Successfull requests with username
        things = thingy.get_username_things(username=username)

        assert isinstance(things, list)

    def test_get_users_favorites(self):
        """test get_username_favorites() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing failing request
        with self.assertRaises(UserException) as raised:
            thingy.get_username_favorites()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'username' is required", "username was required")

        # Successfull requests with username
        favorites = thingy.get_username_favorites(username=username)

        assert isinstance(favorites, list)

    def test_get_users_likes(self):
        """test get_username_likes() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing failing request
        with self.assertRaises(UserException) as raised:
            thingy.get_username_likes()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'username' is required", "username was required")

        # Successfull requests with username
        likes = thingy.get_username_likes(username=username)

        assert isinstance(likes, list)

    def test_get_users_copies(self):
        """test get_username_copies() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing failing request
        with self.assertRaises(UserException) as raised:
            thingy.get_username_copies()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'username' is required", "username was required")

        # Successfull requests with username
        copies = thingy.get_username_copies(username=username)

        assert isinstance(copies, list)

    def test_get_users_collections(self):
        """test get_username_collections() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing failing request
        with self.assertRaises(UserException) as raised:
            thingy.get_username_collections()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'username' is required", "username was required")

        # Successfull requests with username
        collections = thingy.get_username_collections(username=username)

        assert isinstance(collections, list)

    def test_get_users_downloads(self):
        """test get_username_downloads() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing failing request
        with self.assertRaises(UserException) as raised:
            thingy.get_username_downloads()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'username' is required", "username was required")

        # Successfull requests with username
        downloads = thingy.get_username_downloads(username=username)

        assert isinstance(downloads, list)

    def test_get_users_collected_things(self):
        """test get_username_collected_things() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)
        # username to search for
        username = "m4t0n"

        # Testing failing request
        with self.assertRaises(UserException) as raised:
            thingy.get_username_collected_things()
        exception = raised.exception
        self.assertEqual(exception.args[0], "'username' is required", "username was required")

        # Successfull requests with username
        collected_things_res = thingy.get_username_collected_things(username=username)

        assert isinstance(collected_things_res.collected_things, list)

    def test_get_users_unread_messages(self):
        """test get_username_collected_things() method"""
        thingy = Thingiverse(access_token=ACCESS_TOKEN)

        # Successfull requests with username
        message_count = thingy.get_username_unread_message_count(username="m4t0n")
        assert message_count
        # assert isinstance(message_count, list)
