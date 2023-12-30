import pytest
import requests
from requests import HTTPError
from tqdm.auto import tqdm

from pyanimeinfo.myanimelist import JikanV4Client
from test.responses import resp_recorder


@resp_recorder()
def jikanv4_search_anime():
    client = JikanV4Client()
    client.search_anime('Railgun')
    client.search_anime('Railgun', type_='ova')
    client.search_anime('Rokudou no Onna-tachi')


@resp_recorder()
def jikanv4_get_anime():
    client = JikanV4Client()
    client.get_anime(6213)
    with pytest.raises(HTTPError):
        client.get_anime(621333333)


@resp_recorder()
def jikanv4_get_anime_full():
    client = JikanV4Client()
    client.get_anime_full(6213)
    with pytest.raises(HTTPError):
        client.get_anime_full(621333333)


@resp_recorder()
def jikanv4_get_anime_characters():
    client = JikanV4Client()
    client.get_anime_characters(6213)


@resp_recorder()
def jikanv4_search_characters():
    client = JikanV4Client()
    client.search_characters('Misaka')


@resp_recorder()
def jikanv4_get_character():
    client = JikanV4Client()
    client.get_character(13701)
    client.get_character(20626)


@resp_recorder()
def jikanv4_get_character_full():
    client = JikanV4Client()
    client.get_character_full(13701)
    client.get_character_full(20626)


@resp_recorder()
def jikanv4_get_character_related_animes():
    client = JikanV4Client()
    client.get_character_related_animes(13701)


@resp_recorder()
def jikanv4_get_character_related_manga():
    client = JikanV4Client()
    client.get_character_related_manga(13701)


@resp_recorder()
def jikanv4_get_character_voice_actors():
    client = JikanV4Client()
    client.get_character_voice_actors(13701)


@resp_recorder()
def jikanv4_get_character_pictures():
    client = JikanV4Client()
    for item in tqdm(client.get_character_pictures(13701)):
        requests.get(item['jpg']['image_url'])
