import pytest

from .responses import mock_responses_from_hf


@pytest.fixture()
def download_file():
    with mock_responses_from_hf('download_file'):
        yield
