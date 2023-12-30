import pytest

from .responses import mock_responses_from_hf


@pytest.fixture()
def bangumitv_character():
    with mock_responses_from_hf('bangumitv_character'):
        yield


@pytest.fixture()
def bangumitv_person():
    with mock_responses_from_hf('bangumitv_person'):
        yield


@pytest.fixture()
def bangumitv_search():
    with mock_responses_from_hf('bangumitv_search'):
        yield


@pytest.fixture()
def bangumitv_subject():
    with mock_responses_from_hf('bangumitv_subject'):
        yield


@pytest.fixture()
def download_file():
    with mock_responses_from_hf('download_file'):
        yield


@pytest.fixture()
def jikanv4_get_anime():
    with mock_responses_from_hf('jikanv4_get_anime'):
        yield


@pytest.fixture()
def jikanv4_get_anime_characters():
    with mock_responses_from_hf('jikanv4_get_anime_characters'):
        yield


@pytest.fixture()
def jikanv4_get_anime_full():
    with mock_responses_from_hf('jikanv4_get_anime_full'):
        yield


@pytest.fixture()
def jikanv4_get_character():
    with mock_responses_from_hf('jikanv4_get_character'):
        yield


@pytest.fixture()
def jikanv4_get_character_full():
    with mock_responses_from_hf('jikanv4_get_character_full'):
        yield


@pytest.fixture()
def jikanv4_get_character_pictures():
    with mock_responses_from_hf('jikanv4_get_character_pictures'):
        yield


@pytest.fixture()
def jikanv4_get_character_related_animes():
    with mock_responses_from_hf('jikanv4_get_character_related_animes'):
        yield


@pytest.fixture()
def jikanv4_get_character_related_manga():
    with mock_responses_from_hf('jikanv4_get_character_related_manga'):
        yield


@pytest.fixture()
def jikanv4_get_character_voice_actors():
    with mock_responses_from_hf('jikanv4_get_character_voice_actors'):
        yield


@pytest.fixture()
def jikanv4_search_anime():
    with mock_responses_from_hf('jikanv4_search_anime'):
        yield


@pytest.fixture()
def jikanv4_search_characters():
    with mock_responses_from_hf('jikanv4_search_characters'):
        yield
