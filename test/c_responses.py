import pytest

from .responses import mock_responses_from_hf


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
