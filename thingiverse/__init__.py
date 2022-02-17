__version__ = "0.0.7.dev"

from thingiverse.types.exceptions import (
    ResourceNotFound, SearchException,
    ThingiverseException, UnathenticatedException, UserException)
from thingiverse.types.search import SearchResponse
from thingiverse.types.users import ThingiverseUser
from typing import Dict, List, Optional, Text, Union
from box import Box
import requests
import logging


logging.basicConfig(format='%(asctime)s |%(levelname)s|%(message)s')


class Thingiverse(object):
    def __init__(self, access_token=None):
        """A user-created :class:`Thingiverse <Thingiverse>` object.

        Parameters
        ----------
        access_token : str
            Thingiverse access_token after OAuth2

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thingy.search_term("Raspberry Pi", term_library=False, autocomplete=True)
        <SearchResult   >
        """
        if not access_token:
            exception = UnathenticatedException("'access_token' not provided")
            logging.exception(exception)
            raise exception
        self.base_url = "https://api.thingiverse.com"
        self.oauth_url = "https://www.thingiverse.com/login/oauth/authorize"
        self.access_token = access_token
        logging.info("Thingiverse initialized.")

    # TODO
    # def authorize(self,
    #               client_id: Text,
    #               redirect_uri: Optional[Text] = None,
    #               response_type: Optional[Text] = None):
    #     """Authorizes the client given a clientId

    #     :param client_id: The Thingiverse App Client ID
    #     :param redirect_url: The Thingiverse App redirect URL
    #     :param response_type: The OAuth response type. Defaults to 'code' by Thingiverse API

    #     Usage:
    #     >>> from thingiverse import Thingiverse
    #     >>> thingy = Thingiverse(access_token="abc")
    #     >>> thingy.authorize(client_id="abc",
    #                          redirect_uri="https://example.com",
    #                          response_type="token")
    #     """
    #     url = self.oauth_url + f"?client_id={client_id}"
    #     if redirect_uri:
    #         url += f"&redirect_url={redirect_uri}"
    #     if response_type:
    #         url += f"&response_type={response_type}"

    #     print(url)

    #     res = requests.get(url, allow_redirects=True)
    #     print("URL")
    #     print(res.url)
    #     if res.url != url:
    #         new_res = requests.get(res.url, allow_redirects=True)
    #         print("New res")
    #         print(new_res.url)

    #     return res

    def handle_response_error(self, response: requests.Response, message: Text):
        """Simply checks for invalid response and raises errors if any"""
        if response.status_code == 404:
            exception = ResourceNotFound(message)
            logging.exception(exception)
            raise exception
        elif response.status_code != 200:
            exception = ThingiverseException(f"Unknown error: {response.json()}")
            logging.error(f"Error requesting url:\n\t{response.url}")
            logging.exception(exception)
            raise exception

    def get_user_by_username(self, username: Text = "me") -> ThingiverseUser:
        """Get user personal information by `username`

        Parameters
        ----------
        username : str, default="me"
            Username to fetch for.

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> user = thingy.get_user_by_username(username="me")
        """
        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get user by username: {username}")
        res = requests.get(url)

        self.handle_response_error(res, f"User with username {username} not found.")

        res_json = res.json()
        user_box = Box(res_json)
        logging.info(f"Successfully retrieved user with username {username}")

        return user_box

    def get_users_data(self, username: Text = None, term: Text = None):
        """Get user things data by `username`

        Parameters
        -----------
        username: str
            Username to fetch for
        term: str
            The search query to perform

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> user = thingy.get_users_data(username="m4t0n", term="RPi")
        """
        if not username:
            exception = UserException("'username' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/search"
        if term:
            path += f"/{term}"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get username data: {username}; term: {term}")
        res = requests.get(url)

        self.handle_response_error(res, f"Username with username {username} not found.")

        res_json = res.json()
        thing_box = Box(res_json)
        logging.info(f"Successfully retrieved user data with username {username}")

        return thing_box

    def get_username_things(self, username: Text = None):
        """Gets a list of things by `username`

        Parameters
        ----------
        username: str
            username to search things for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.get_things_by_username(username="m4t0n")
        """
        if not username:
            exception = UserException("'username' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/things"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get things for username: {username}")
        res = requests.get(url)

        self.handle_response_error(res, f"Username with username {username} not found.")

        res_json = res.json()
        # thing_box = Box(res_json)
        logging.info(f"Successfully retrieved things for username {username}")

        return res_json

    def get_username_collected_things(self, username: Text = None):
        """Gets a list of collected things by `username`

        Parameters
        ----------
        username: str
            username to search things for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.get_username_collected_things(username="m4t0n")
        """
        if not username:
            exception = UserException("'username' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/all-collected-things"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get collected things for username: {username}")
        res = requests.get(url)

        self.handle_response_error(res, f"Username with username {username} not found.")

        res_json = res.json()
        things_box = Box(res_json)

        logging.info(f"Successfully retrieved collected things for username {username}")

        return things_box

    def get_username_unread_message_count(self, username: Text = None):
        """Gets unread message count

        Parameters
        ----------
        username: str
            username to search things for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.get_username_unread_message_count()
        """

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/unread-message-count"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get message count for username {username}")
        res = requests.get(url)

        error_msg = f"Something went wrong while fetching message count for username {username}."
        self.handle_response_error(res, error_msg)

        res_json = res.json()
        # message_count_box = Box(res_json)
        logging.info(f"Successfully retrieved message count for username {username}")
        print("Unread messages")
        print(res_json)
        return res_json

    def get_username_favorites(self, username: Text = None):
        """Gets a list of favorites by `username`

        Parameters
        ----------
        username: str
            username to search favorites for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.get_username_favorites(username="m4t0n")
        """
        if not username:
            exception = UserException("'username' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/favorites"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get favorites for username: {username}")
        res = requests.get(url)

        self.handle_response_error(res, f"Username with username {username} not found.")

        res_json = res.json()
        # favorites_box = Box(res_json)
        logging.info(f"Successfully retrieved favorites for username {username}")

        return res_json

    def get_username_likes(self, username: Text = None):
        """Gets a list of likes by `username`

        Parameters
        ----------
        username: str
            username to search likes for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.get_username_likes(username="m4t0n")
        """
        if not username:
            exception = UserException("'username' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/likes"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get likes for username: {username}")
        res = requests.get(url)

        self.handle_response_error(res, f"Username with username {username} not found.")

        res_json = res.json()
        # likes_box = Box(res_json)
        logging.info(f"Successfully retrieved likes for username {username}")

        return res_json

    def get_username_copies(self, username: Text = None):
        """Gets a list of copies by `username`

        Parameters
        ----------
        username: str
            username to search copies for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.get_username_copies(username="m4t0n")
        """
        if not username:
            exception = UserException("'username' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/copies"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get copies for username: {username}")
        res = requests.get(url)

        self.handle_response_error(res, f"Username with username {username} not found.")

        res_json = res.json()
        # copies_box = Box(res_json)
        logging.info(f"Successfully retrieved copies for username {username}")

        return res_json

    def get_username_collections(self, username: Text = None, paginate: bool = True):
        """Gets a list of copies by `username`

        Parameters
        ----------
        username: str
            username to search copies for

        paginate: bool, default=True
            return a paginated response, if `False`, a full list will be returned

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.get_username_collections(username="m4t0n", paginate=False)
        """
        if not username:
            exception = UserException("'username' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/collections"

        if paginate:
            path += "/all"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get collections for username: {username}")
        res = requests.get(url)

        self.handle_response_error(res, f"Username with username {username} not found.")

        res_json = res.json()
        # collections_box = Box(res_json)
        logging.info(f"Successfully retrieved collections for username {username}")

        return res_json

    def get_username_downloads(self, username: Text = None):
        """Gets a list of downloads by `username`

        Parameters
        ----------
        username: str
            username to search downloads for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.get_username_downloads(username="m4t0n")
        """
        if not username:
            exception = UserException("'username' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/users/{username}/downloads"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get copies for username: {username}")
        res = requests.get(url)

        self.handle_response_error(res, f"Username with username {username} not found.")

        res_json = res.json()
        # downloads_box = Box(res_json)
        logging.info(f"Successfully retrieved copies for username {username}")

        return res_json

    def get_thing_by_id(self, thing_id: int = None):
        """Gets a thing by `thing_id`

        Parameters
        ----------
        thing_id: int
            id of the thing to get

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thing = thingy.thing_by_id(thing_id=123)
        """

        if not thing_id:
            exception = ThingiverseException("'thing_id' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/things/{thing_id}/"

        url = self.base_url + path + access_token_param
        logging.info(f"Making request to get thing by id: {thing_id}")
        res = requests.get(url)

        self.handle_response_error(res, f"Thing with id {thing_id} not found.")

        res_json = res.json()
        thing_box = Box(res_json)
        logging.info(f"Successfully retrieved thing with id {thing_id}")

        return thing_box

    def get_images_by_thing(self,
                            thing_id: int = None,
                            image_id: Optional[int] = None,
                            image_type: Optional[Text] = None,
                            image_size: Optional[Text] = None) -> Union[Dict, List]:
        """Gets image(s) for a thing

        Parameters
        ----------
        thing_id: int
            Thing to fetch images for

        image_id: int, optional
            If not given, an array of images will be returned

        image_type: str, optional
            Image type to look for

        image_size: str, optional
            Image size to look for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> images = thingy.get_images_for_thing(thing_id=1234)
        >>> image = thingy.get_images_for_thing(thing_id=1234, image_id=4321)
        """
        if not thing_id:
            exception = ThingiverseException("'thing_id' is required")
            logging.exception(exception)
            raise exception

        if image_size and not image_type:
            # based on their API Docs `type` is required if umage_size is given
            # https://www.thingiverse.com/developers/rest-api-reference#things
            exception = ThingiverseException("'image_type' is required is 'image_size' is given")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/things/{thing_id}/images/"

        if image_id:
            path += str(image_id)

        path += access_token_param
        if image_size:
            path + f"&size={image_size}"

        if image_type:
            path += f"&type={image_type}"

        url = self.base_url + path
        logging.info(f"Making request to get thing by id: {thing_id}")
        res = requests.get(url)

        self.handle_response_error(res, f"Thing with id {thing_id} not found.")

        res_json = res.json()
        # images_box = Box(res_json)
        logging.info(f"Successfully images for thing with id {thing_id}")

        return res_json

    # Search endpoints
    def search_term(self,
                    term: Text = None) -> SearchResponse:
        """Searches for a term on Thingiverse

        Parameters
        ----------
        term: str
            Term to search for

        term_library: bool
            Will be requesting libraries for term

        autocomplete: bool
            Will be requesting autocomplete endpoint

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thingy.search_term(term="Raspberry Pi",
                               term_library=False,
                               autocomplete=True)
        """
        if not term:
            exception = SearchException("'term' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/search/{term}"

        url = self.base_url + path + access_token_param
        logging.info(f"Making search term request to {url}")
        res = requests.get(url)
        res_json = res.json()
        search_box = Box(res_json)
        logging.info(f"Successfully retrieved search results for term {term}")

        return search_box

    def search_tag(self, tag: Text = None) -> SearchResponse:
        """Searches for a tag on Thingiverse

        Parameters
        ----------

        tag: str
            Tag to search for

        Usage:
        >>> from thingiverse import Thingiverse
        >>> thingy = Thingiverse(access_token="abc")
        >>> thingy.search_tag(tag="Raspberry Pi")
        """
        if not tag:
            exception = SearchException("'tag' is required")
            logging.exception(exception)
            raise exception

        access_token_param = f"?access_token={self.access_token}"
        path = f"/search/{tag}/tag"

        url = self.base_url + path + access_token_param
        logging.info(f"Making search tag request to {url}")
        res = requests.get(url)
        res_json = res.json()
        search_box = Box(res_json)
        logging.info(f"Successfully retrieved search results for term {tag}")

        return search_box
