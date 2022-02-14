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
