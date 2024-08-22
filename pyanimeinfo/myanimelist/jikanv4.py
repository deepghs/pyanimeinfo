from typing import Optional, Mapping, Literal, List, Union
from urllib.parse import urljoin

import requests

from ..utils import get_session

_DEFAULT_JIKAN_V4_WEBSITE = 'https://api.jikan.moe/v4/'

_SearchOrderByTyping = Literal[
    "mal_id", "title", "start_date", "end_date", "episodes", "score",
    "scored_by", "rank", "popularity", "members", "favorites"
]


class JikanV4Client:
    """
    Client for interacting with the Jikan API (v4) to retrieve anime and character information.

    :param session: Optional requests session. If not provided, a new session is created.
    :type session: Optional[requests.Session]
    :param website: Optional Jikan API website URL. Defaults to the official Jikan v4 API.
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
        self._website = website or _DEFAULT_JIKAN_V4_WEBSITE

    @classmethod
    def _post_process_resp(cls, resp: requests.Response):
        """
        Helper method to process the API response.

        :param resp: API response from the Jikan API.
        :type resp: requests.Response
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        resp.raise_for_status()
        return resp.json()['data']

    def _raw_get(self, url, params: Mapping[str, Optional[str]] = None):
        """
        Perform a raw GET request to the Jikan API.

        :param url: Relative URL for the API endpoint.
        :type url: str
        :param params: Optional parameters for the API request.
        :type params: Mapping[str, Optional[str]]
        :return: Raw response from the Jikan API.
        :rtype: requests.Response
        """
        url = urljoin(self._website, url)
        params = {key: str(value) for key, value in (params or {}).items() if value is not None}
        return self._session.get(url, params=params)

    def _get(self, url, params: Mapping[str, Optional[str]] = None):
        """
        Perform a GET request to the Jikan API and process the response.

        :param url: Relative URL for the API endpoint.
        :type url: str
        :param params: Optional parameters for the API request.
        :type params: Mapping[str, Optional[str]]
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._post_process_resp(self._raw_get(url, params))

    def search_anime(self, query: str,
                     type_: Optional[Literal["tv", "movie", "ova", "special", "ona", "music"]] = None,
                     status: Optional[Literal["airing", "complete", "upcoming"]] = None,
                     rating: Optional[Literal["g", "pg", "pg13", "r17", "r", "rx"]] = None,
                     order_by: Optional[_SearchOrderByTyping] = None,
                     sort_: Optional[Literal["desc", "asc"]] = None,
                     sfw: bool = False, unapproved: bool = False,
                     start_date: Optional[str] = None, end_date: Optional[str] = None,
                     page: Optional[int] = None, limit: Optional[int] = None):
        """
        Search for anime on the Jikan API.

        :param query: Search query.
        :type query: str
        :param type_: Type of anime (e.g., "tv", "movie").
        :type type_: Optional[Literal["tv", "movie", "ova", "special", "ona", "music"]]
        :param status: Anime status (e.g., "airing", "complete").
        :type status: Optional[Literal["airing", "complete", "upcoming"]]
        :param rating: Age rating of the anime.
        :type rating: Optional[Literal["g", "pg", "pg13", "r17", "r", "rx"]]
        :param order_by: Attribute to order the results by.
        :type order_by: Optional[_SearchOrderByTyping]
        :param sort_: Sort order ("desc" or "asc").
        :type sort_: Optional[Literal["desc", "asc"]]
        :param sfw: Whether to include safe-for-work content.
        :type sfw: bool
        :param unapproved: Whether to include unapproved content.
        :type unapproved: bool
        :param start_date: Start date filter for anime.
        :type start_date: Optional[str]
        :param end_date: End date filter for anime.
        :type end_date: Optional[str]
        :param page: Page number for paginated results.
        :type page: Optional[int]
        :param limit: Limit on the number of results per page.
        :type limit: Optional[int]
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._get(
            'anime',
            {
                'q': query,
                'page': page,
                'limit': limit,
                'sfw': '1' if sfw else None,
                'unapproved': '1' if unapproved else None,
                'type': type_,
                'status': status,
                'rating': rating,
                'order_by': order_by,
                'sort': sort_,
                'start_date': start_date,
                'end_date': end_date,
            }
        )

    def get_anime(self, anime_id):
        """
        Get information about a specific anime by ID.

        :param anime_id: ID of the anime.
        :type anime_id: int
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._get(f'anime/{anime_id}')

    def get_anime_full(self, anime_id):
        """
        Get full information about a specific anime by ID.

        :param anime_id: ID of the anime.
        :type anime_id: int
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._get(f'anime/{anime_id}/full')

    def get_anime_pictures(self, anime_id: int):
        """
        Get pictures information of a specific anime by ID.

        :param anime_id: ID of the anime
        :type: anime_id: int
        :return: Processed JSON data for the API response.
        :rtype: dict
        """
        return self._get(f'anime/{anime_id}/pictures')

    def get_anime_characters(self, anime_id):
        """
        Get information about characters in a specific anime by ID.

        :param anime_id: ID of the anime.
        :type anime_id: int
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._get(f'anime/{anime_id}/characters')

    def search_characters(self, query: str,
                          order_by: Optional[Literal["mal_id", "name", "favorites"]] = None,
                          sort_: Optional[Literal["desc", "asc"]] = None,
                          page: Optional[int] = None, limit: Optional[int] = None):
        """
        Search for characters on the Jikan API.

        :param query: Search query.
        :type query: str
        :param order_by: Attribute to order the results by.
        :type order_by: Optional[Literal["mal_id", "name", "favorites"]]
        :param sort_: Sort order ("desc" or "asc").
        :type sort_: Optional[Literal["desc", "asc"]]
        :param page: Page number for paginated results.
        :type page: Optional[int]
        :param limit: Limit on the number of results per page.
        :type limit: Optional[int]
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._get(
            'characters',
            {
                'q': query,
                'page': page,
                'limit': limit,
                'order_by': order_by,
                'sort': sort_,
            }
        )

    def get_character(self, character_id):
        """
        Get information about a specific character by ID.

        :param character_id: ID of the character.
        :type character_id: int
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._get(f'characters/{character_id}')

    def get_character_full(self, character_id):
        """
        Get full information about a specific character by ID.

        :param character_id: ID of the character.
        :type character_id: int
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._get(f'characters/{character_id}/full')

    def get_character_related_animes(self, character_id):
        """
        Get information about anime related to a specific character by ID.

        :param character_id: ID of the character.
        :type character_id: int
        :return: Processed JSON data from the API response.
        :rtype: dict
        """
        return self._get(f'characters/{character_id}/anime')

    def get_character_related_manga(self, character_id):
        """
        Get information about manga related to a specific character by ID.

        This method retrieves a list of manga titles that feature the specified character.

        :param character_id: ID of the character.
        :type character_id: int
        :return: Processed JSON data from the API response, containing information about related manga.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> related_manga = client.get_character_related_manga(1)
        >>> print(related_manga)
        """
        return self._get(f'characters/{character_id}/manga')

    def get_character_voice_actors(self, character_id):
        """
        Get information about voice actors for a specific character by ID.

        This method retrieves a list of voice actors who have portrayed the specified character in various anime adaptations.

        :param character_id: ID of the character.
        :type character_id: int
        :return: Processed JSON data from the API response, containing information about voice actors.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> voice_actors = client.get_character_voice_actors(1)
        >>> print(voice_actors)
        """
        return self._get(f'characters/{character_id}/voices')

    def get_character_pictures(self, character_id):
        """
        Get pictures of a specific character by ID.

        This method retrieves a collection of images associated with the specified character.

        :param character_id: ID of the character.
        :type character_id: int
        :return: Processed JSON data from the API response, containing links to character pictures.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> pictures = client.get_character_pictures(1)
        >>> print(pictures)
        """
        return self._get(f'characters/{character_id}/pictures')

    def get_manga(self, manga_id: int):
        """
        Get basic information about a specific manga by ID.

        This method retrieves basic details about the specified manga, such as title, author, and publication status.

        :param manga_id: ID of the manga.
        :type manga_id: int
        :return: Processed JSON data from the API response, containing basic manga information.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> manga_info = client.get_manga(1)
        >>> print(manga_info)
        """
        return self._get(f'manga/{manga_id}')

    def get_manga_full(self, manga_id: int):
        """
        Get full information about a specific manga by ID.

        This method retrieves comprehensive details about the specified manga, including synopsis, characters, and more.

        :param manga_id: ID of the manga.
        :type manga_id: int
        :return: Processed JSON data from the API response, containing full manga information.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> manga_full_info = client.get_manga_full(1)
        >>> print(manga_full_info)
        """
        return self._get(f'manga/{manga_id}/full')

    def get_manga_pictures(self, manga_id: int):
        """
        Get pictures associated with a specific manga by ID.

        This method retrieves a collection of images related to the specified manga, such as cover art and illustrations.

        :param manga_id: ID of the manga.
        :type manga_id: int
        :return: Processed JSON data from the API response, containing links to manga pictures.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> manga_pictures = client.get_manga_pictures(1)
        >>> print(manga_pictures)
        """
        return self._get(f'manga/{manga_id}/pictures')

    def search_manga(self, query: str,
                     order_by: Optional[
                         Literal["mal_id", "title", "start_date", "end_date", "chapters", "volumes", "score",
                         "scored_by", "rank", "popularity", "members", "favorites"]] = None,
                     sort_: Optional[Literal["desc", "asc"]] = None,
                     type_: Optional[
                         Literal["manga", "novel", "lightnovel", "oneshot", "doujin", "manhwa", "manhua"]] = None,
                     unapproved: bool = False, score: Optional[float] = None,
                     min_score: Optional[float] = None, max_score: Optional[float] = None,
                     status: Optional[Literal["publishing", "complete", "hiatus", "discontinued", "upcoming"]] = None,
                     sfw: bool = False, letter: Optional[str] = None,
                     magazines: Optional[List[Union[int, str]]] = None,
                     genres: Optional[List[Union[int, str]]] = None,
                     genres_exclude: Optional[List[Union[int, str]]] = None,
                     start_date: Optional[str] = None, end_date: Optional[str] = None,
                     page: Optional[int] = None, limit: Optional[int] = None):
        """
        Search for manga based on various criteria.

        This method allows for a comprehensive search of manga titles with multiple filtering options.

        :param query: Search query string.
        :type query: str
        :param order_by: Property to order the results by.
        :type order_by: Optional[Literal["mal_id", "title", "start_date", "end_date", "chapters", "volumes", "score", "scored_by", "rank", "popularity", "members", "favorites"]]
        :param sort_: Sort direction for the results.
        :type sort_: Optional[Literal["desc", "asc"]]
        :param type_: Type of manga to search for.
        :type type_: Optional[Literal["manga", "novel", "lightnovel", "oneshot", "doujin", "manhwa", "manhua"]]
        :param unapproved: Include unapproved entries in the results.
        :type unapproved: bool
        :param score: Filter by exact score.
        :type score: Optional[float]
        :param min_score: Filter by minimum score.
        :type min_score: Optional[float]
        :param max_score: Filter by maximum score.
        :type max_score: Optional[float]
        :param status: Filter by publication status.
        :type status: Optional[Literal["publishing", "complete", "hiatus", "discontinued", "upcoming"]]
        :param sfw: Filter out adult content.
        :type sfw: bool
        :param letter: Filter by starting letter of the title.
        :type letter: Optional[str]
        :param magazines: Filter by magazine IDs.
        :type magazines: Optional[List[Union[int, str]]]
        :param genres: Filter by genre IDs.
        :type genres: Optional[List[Union[int, str]]]
        :param genres_exclude: Exclude specific genre IDs.
        :type genres_exclude: Optional[List[Union[int, str]]]
        :param start_date: Filter by start date (format: YYYY-MM-DD).
        :type start_date: Optional[str]
        :param end_date: Filter by end date (format: YYYY-MM-DD).
        :type end_date: Optional[str]
        :param page: Page number for pagination.
        :type page: Optional[int]
        :param limit: Number of results per page.
        :type limit: Optional[int]
        :return: Processed JSON data from the API response, containing search results.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> search_results = client.search_manga("Naruto", order_by="popularity", sort_="desc", type_="manga", sfw=True)
        >>> print(search_results)
        """
        return self._get(
            'manga',
            params={
                'q': query,
                'unapproved': '1' if unapproved else None,
                'page': page,
                'limit': limit,
                'type': type_,
                'score': score,
                'min_score': min_score,
                'max_score': max_score,
                'status': status,
                'sfw': '1' if sfw else None,
                'genres': ','.join(map(str, genres)) if genres else None,
                'genres_exclude': ','.join(map(str, genres_exclude)) if genres_exclude else None,
                'order_by': order_by,
                'sort': sort_,
                'letter': letter,
                'magazines': ','.join(map(str, magazines)) if magazines else None,
                'start_date': start_date,
                'end_date': end_date,
            }
        )

    def get_people(self, people_id: int):
        """
        Get basic information about a specific person by ID.

        This method retrieves basic details about the specified person, such as name and role in the anime/manga industry.

        :param people_id: ID of the person.
        :type people_id: int
        :return: Processed JSON data from the API response, containing basic information about the person.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> person_info = client.get_people(1)
        >>> print(person_info)
        """
        return self._get(f'people/{people_id}')

    def get_people_full(self, people_id: int):
        """
        Get full information about a specific person by ID.

        This method retrieves comprehensive details about the specified person, including their works and biography.

        :param people_id: ID of the person.
        :type people_id: int
        :return: Processed JSON data from the API response, containing full information about the person.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> person_full_info = client.get_people_full(1)
        >>> print(person_full_info)
        """
        return self._get(f'people/{people_id}/full')

    def get_people_pictures(self, people_id: int):
        """
        Get pictures of a specific person by ID.

        This method retrieves a collection of images associated with the specified person.

        :param people_id: ID of the person.
        :type people_id: int
        :return: Processed JSON data from the API response, containing links to pictures of the person.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> person_pictures = client.get_people_pictures(1)
        >>> print(person_pictures)
        """
        return self._get(f'people/{people_id}/pictures')

    def search_people(self, query: str,
                      order_by: Optional[Literal["mal_id", "name", "birthday", "favorites"]] = None,
                      sort_: Optional[Literal["desc", "asc"]] = None,
                      letter: Optional[str] = None,
                      page: Optional[int] = None, limit: Optional[int] = None):
        """
        Search for people in the anime/manga industry based on various criteria.

        This method allows for searching people such as voice actors, directors, and manga artists.

        :param query: Search query string.
        :type query: str
        :param order_by: Property to order the results by.
        :type order_by: Optional[Literal["mal_id", "name", "birthday", "favorites"]]
        :param sort_: Sort direction for the results.
        :type sort_: Optional[Literal["desc", "asc"]]
        :param letter: Filter by starting letter of the name.
        :type letter: Optional[str]
        :param page: Page number for pagination.
        :type page: Optional[int]
        :param limit: Number of results per page.
        :type limit: Optional[int]
        :return: Processed JSON data from the API response, containing search results.
        :rtype: dict

        :Example:

        >>> client = JikanV4Client()
        >>> search_results = client.search_people("Miyazaki", order_by="favorites", sort_="desc")
        >>> print(search_results)
        """
        return self._get(
            'people',
            params={
                'q': query,
                'order_by': order_by,
                'sort': sort_,
                'letter': letter,
                'page': page,
                'limit': limit,
            }
        )
