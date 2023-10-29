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
    def __init__(self, session: Optional[requests.Session] = None,
                 website: Optional[str] = None):
        self._session = session or get_session()
        self._session.headers.update({
            'User-Agent': 'deepghs/pyanimeinfo',
            'Accept': 'application/json',
        })
        self._website = website or _BANGUMITV_WEBSITE

    @classmethod
    def _post_process_resp(cls, resp: requests.Response):
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
        url = urljoin(self._website, url)
        params = {key: str(value) for key, value in (params or {}).items() if value is not None}
        resp = self._session.get(url, params=params)
        return self._post_process_resp(resp)

    def search_subjects(self, keywords: str, type_: Optional[SubjectType] = None,
                        response_group: Optional[Literal['small', 'medium', 'large']] = None,
                        offset: Optional[int] = None, limit: int = 25):
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
        return self._get(f'/v0/subjects/{subject_id}')

    def get_subject_persons(self, subject_id: int):
        return self._get(f'/v0/subjects/{subject_id}/persons')

    def get_subject_characters(self, subject_id: int):
        return self._get(f'/v0/subjects/{subject_id}/characters')

    def get_subject_relations(self, subject_id: int):
        return self._get(f'/v0/subjects/{subject_id}/subjects')

    def get_character(self, character_id):
        return self._get(f'/v0/characters/{character_id}')

    def get_character_related_persons(self, character_id):
        return self._get(f'/v0/characters/{character_id}/persons')

    def get_character_related_subjects(self, character_id):
        return self._get(f'/v0/characters/{character_id}/subjects')

    def get_person(self, person_id):
        return self._get(f'/v0/persons/{person_id}')

    def get_person_related_subjects(self, person_id):
        return self._get(f'/v0/persons/{person_id}/subjects')

    def get_person_related_characters(self, person_id):
        return self._get(f'/v0/persons/{person_id}/characters')
