import json
from typing import Optional, Mapping, Any, Literal
from urllib.parse import quote_plus, urljoin

import requests
from hbutils.encoding import auto_decode
from pyquery import PyQuery as pq

from .enums import SubjectType
from .exceptions import BangumiTVPageError, BangumiTVAPIError
from ..utils import get_session, load_text_from_enum

_BANGUMITV_WEBSITE = 'https://api.bgm.tv'


class BangumiTVClient:
    """
    A client class for accessing the Bangumi.tv API.

    The `BangumiTVClient` class provides methods for interacting with the Bangumi.tv API, allowing you to search for subjects, retrieve information about subjects, characters, persons, and more.

    :param session: An optional `requests.Session` object to be used for making HTTP requests.
    :type session: Optional[requests.Session]
    :param website: The base URL of the Bangumi.tv API. Default is ``https://api.bgm.tv``.
    :type website: Optional[str]
    :param user_agent: User agent to use in client. Defaults to `deepghs/pyanimeinfo`.
                       Keep the original UA when assigned to empty value.
    :type user_agent: Optional[str]
    """

    def __init__(self, session: Optional[requests.Session] = None, website: Optional[str] = None,
                 user_agent: Optional[str] = 'deepghs/pyanimeinfo'):
        self._session = session or get_session()
        self._session.headers.update({'Accept': 'application/json'})
        if user_agent:
            self._session.headers.update({'User-Agent': user_agent})
        self._website = website or _BANGUMITV_WEBSITE

    @classmethod
    def _post_process_resp(cls, resp: requests.Response):
        """
        Process the HTTP response and handle errors.

        This internal method is responsible for processing the HTTP response from the API and handling errors. It checks the response content and raises exceptions if errors are encountered.

        :param resp: The HTTP response from the API.
        :type resp: requests.Response

        :return: Parsed JSON response if the response is successful.
        :rtype: dict
        :raises BangumiTVPageError: If the response is an error displayed on a web page.
        :raises BangumiTVAPIError: If the response is an error returned in JSON format from the API.
        """
        try:
            json_ = resp.json()
            if resp.ok:
                return json_
            else:
                raise BangumiTVAPIError(
                    resp.status_code,
                    json_.get('title'),
                    json_.get('description'),
                    json_.get('details')
                )
        except json.JSONDecodeError:
            page = pq(auto_decode(resp.content))
            messagebox = page('#colunmNotice .message')
            message_title = messagebox('h2').text().strip()
            message_text = messagebox('.text').text().strip()
            raise BangumiTVPageError(resp.status_code, message_title, message_text)

    def _get(self, url, params: Mapping[str, Any] = None):
        """
        Perform a GET request to the Bangumi.tv API.

        This method performs a GET request to the Bangumi.tv API using the provided URL and parameters.

        :param url: The API endpoint URL.
        :type url: str
        :param params: Optional query parameters for the request.
        :type params: Mapping[str, Any]

        :return: Parsed JSON response if the request is successful.
        :rtype: dict
        """
        url = urljoin(self._website, url)
        params = {key: str(value) for key, value in (params or {}).items() if value is not None}
        resp = self._session.get(url, params=params)
        return self._post_process_resp(resp)

    def search_subjects(self, keywords: str, type_: Optional[SubjectType] = None,
                        response_group: Optional[Literal['small', 'medium', 'large']] = None,
                        offset: Optional[int] = None, limit: int = 25):
        """
        Search for subjects on Bangumi.tv.

        This method allows you to search for subjects on Bangumi.tv based on provided keywords and optional search parameters.

        :param keywords: The search keywords.
        :type keywords: str
        :param type_: The type of the subject (e.g., anime, manga).
        :type type_: Optional[SubjectType]
        :param response_group: The response group size (small, medium, large).
        :type response_group: Optional[Literal['small', 'medium', 'large']]
        :param offset: The offset for the search results (pagination).
        :type offset: Optional[int]
        :param limit: The maximum number of results to return.
        :type limit: int

        :return: The search results as a JSON response.
        :rtype: dict
        """
        return self._get(
            f'/search/subject/{quote_plus(keywords)}',
            {
                'type': load_text_from_enum(type_, SubjectType) if type_ is not None else None,
                'responseGroup': response_group,
                'start': offset,
                'max_results': limit,
            }
        )

    def get_subject(self, subject_id: int):
        """
        Get information about a specific subject.

        This method retrieves information about a subject on Bangumi.tv based on the provided subject ID.

        :param subject_id: The ID of the subject.
        :type subject_id: int

        :return: Information about the subject as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/subjects/{subject_id}')

    def get_subject_persons(self, subject_id: int):
        """
        Get information about persons related to a specific subject.

        This method retrieves information about persons related to a subject on Bangumi.tv based on the provided subject ID.

        :param subject_id: The ID of the subject.
        :type subject_id: int

        :return: Information about persons related to the subject as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/subjects/{subject_id}/persons')

    def get_subject_characters(self, subject_id: int):
        """
        Get information about characters related to a specific subject.

        This method retrieves information about characters related to a subject on Bangumi.tv based on the provided subject ID.

        :param subject_id: The ID of the subject.
        :type subject_id: int

        :return: Information about characters related to the subject as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/subjects/{subject_id}/characters')

    def get_subject_relations(self, subject_id: int):
        """
        Get information about related subjects to a specific subject.

        This method retrieves information about subjects related to a subject on Bangumi.tv based on the provided subject ID.

        :param subject_id: The ID of the subject.
        :type subject_id: int

        :return: Information about related subjects as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/subjects/{subject_id}/subjects')

    def get_character(self, character_id: int):
        """
        Get information about a specific character.

        This method retrieves information about a character on Bangumi.tv based on the provided character ID.

        :param character_id: The ID of the character.
        :type character_id: int

        :return: Information about the character as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/characters/{character_id}')

    def get_character_related_persons(self, character_id: int):
        """
        Get information about persons related to a specific character.

        This method retrieves information about persons related to a character on Bangumi.tv based on the provided character ID.

        :param character_id: The ID of the character.
        :type character_id: int

        :return: Information about persons related to the character as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/characters/{character_id}/persons')

    def get_character_related_subjects(self, character_id: int):
        """
        Get information about subjects related to a specific character.

        This method retrieves information about subjects related to a character on Bangumi.tv based on the provided character ID.

        :param character_id: The ID of the character.
        :type character_id: int

        :return: Information about subjects related to the character as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/characters/{character_id}/subjects')

    def get_person(self, person_id: int):
        """
        Get information about a specific person.

        This method retrieves information about a person on Bangumi.tv based on the provided person ID.

        :param person_id: The ID of the person.
        :type person_id: int

        :return: Information about the person as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/persons/{person_id}')

    def get_person_related_subjects(self, person_id: int):
        """
        Get information about subjects related to a specific person.

        This method retrieves information about subjects related to a person on Bangumi.tv based on the provided person ID.

        :param person_id: The ID of the person.
        :type person_id: int

        :return: Information about subjects related to the person as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/persons/{person_id}/subjects')

    def get_person_related_characters(self, person_id: int):
        """
        Get information about characters related to a specific person.

        This method retrieves information about characters related to a person on Bangumi.tv based on the provided person ID.

        :param person_id: The ID of the person.
        :type person_id: int

        :return: Information about characters related to the person as a JSON response.
        :rtype: dict
        """
        return self._get(f'/v0/persons/{person_id}/characters')
