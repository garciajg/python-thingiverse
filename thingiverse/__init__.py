__version__ = "0.0.5"

from thingiverse.types.exceptions import (
    ResourceNotFound, SearchException,
    ThingiverseException, UnathenticatedException)
from thingiverse.types.search import SearchResponse
from typing import Dict, List, Optional, Text, Union
from box import Box
import requests
import logging

logging.basicConfig(format='%(asctime)s |%(levelname)s|%(message)s')


class Thingiverse(object):
    def __init__(self, access_token=None):
        """A user-created :class:`Thingiverse <Thingiverse> object.

        :param access_token: Thingiverse access_token after OAuth2

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

    def get_thing_by_id(self, thing_id: int = None):
        """Gets a thing by {thing_id}

        :param thing_id: id of the thing to get

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

        if res.status_code == 404:
            exception = ResourceNotFound(f"Thing with id {thing_id} not found.")
            logging.exception(exception)
            raise exception
        elif res.status_code != 200:
            exception = ThingiverseException(f"Unknown error: {res.json()}")
            logging.error(f"Error requesting url:\n\t{url}")
            logging.exception(exception)
            raise exception

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

        :param thing_id: thing to fetch images for
        :param image_id: optional - if not given, an array of images will be returned
        :param image_type: optional - image type to look for
        :param image_size: optional - image size to look for

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

        if res.status_code == 404:
            exception = ResourceNotFound(f"Thing with id {thing_id} not found.")
            logging.exception(exception)
            raise exception
        elif res.status_code != 200:
            exception = ThingiverseException(f"Unknown error: {res.json()}")
            logging.error(f"Error requesting url:\n\t{url}")
            logging.exception(exception)
            raise exception

        res_json = res.json()
        # images_box = Box(res_json)
        logging.info(f"Successfully images for thing with id {thing_id}")

        return res_json

    # Search endpoints
    def search_term(self,
                    term: Text = None) -> SearchResponse:
        """Searches for a term on Thingiverse

        :param term: term to search for
        :param term_library: will be requesting libraries for term
        :param autocomplete: will be requesting autocomplete endpoint

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

        :param tag: tag to search for

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
