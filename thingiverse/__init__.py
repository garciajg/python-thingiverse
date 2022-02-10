__version__ = '0.1.0'

from thingiverse.types.exceptions import (
    SearchException, UnathenticatedException)
from thingiverse.types.search import SearchResponse
from typing import Text
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
