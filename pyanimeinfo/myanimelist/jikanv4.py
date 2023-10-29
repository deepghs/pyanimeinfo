from typing import Optional, Mapping, Literal
from urllib.parse import urljoin

import requests

from ..utils import get_session

_DEFAULT_JIKAN_V4_WEBSITE = 'https://api.jikan.moe/v4/'

_SearchOrderByTyping = Literal[
    "mal_id", "title", "start_date", "end_date", "episodes", "score",
    "scored_by", "rank", "popularity", "members", "favorites"
]


class JikanV4Client:
    def __init__(self, session: Optional[requests.Session] = None, website: Optional[str] = None):
        self._session = session or get_session()
        self._session.headers.update({
            'User-Agent': 'deepghs/pyanimeinfo',
            'Accept': 'application/json',
        })
        self._website = website or _DEFAULT_JIKAN_V4_WEBSITE

    @classmethod
    def _post_process_resp(cls, resp: requests.Response):
        resp.raise_for_status()
        return resp.json()['data']

    def _raw_get(self, url, params: Mapping[str, Optional[str]] = None):
        url = urljoin(self._website, url)
        params = {key: str(value) for key, value in (params or {}).items() if value is not None}
        return self._session.get(url, params=params)

    def _get(self, url, params: Mapping[str, Optional[str]] = None):
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
        return self._get(f'anime/{anime_id}')

    def get_anime_full(self, anime_id):
        return self._get(f'anime/{anime_id}/full')

    def get_anime_characters(self, anime_id):
        return self._get(f'anime/{anime_id}/characters')

    def search_characters(self, query: str,
                          order_by: Optional[Literal["mal_id", "name", "favorites"]] = None,
                          sort_: Optional[Literal["desc", "asc"]] = None,
                          page: Optional[int] = None, limit: Optional[int] = None):
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
        return self._get(f'characters/{character_id}')

    def get_character_full(self, character_id):
        return self._get(f'characters/{character_id}/full')

    def get_character_related_animes(self, character_id):
        return self._get(f'characters/{character_id}/anime')

    def get_character_related_manga(self, character_id):
        return self._get(f'characters/{character_id}/manga')

    def get_character_voice_actors(self, character_id):
        return self._get(f'characters/{character_id}/voices')

    def get_character_pictures(self, character_id):
        return self._get(f'characters/{character_id}/pictures')
