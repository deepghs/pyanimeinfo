import os.path
import pathlib

import pytest
import responses
from hbutils.encoding import sha1
from hbutils.system import TemporaryDirectory
from hbutils.testing import capture_output

from pyanimeinfo.utils import download_file as _func_download_file


@pytest.fixture()
def url_to_download():
    return 'https://huggingface.co/datasets/deepghs/game_character_skins/resolve/main/arknights/NM01/%E4%B9%90%E9%80%8D%E9%81%A5.png'


@pytest.mark.unittest
class TestUtilsDownload:
    @responses.activate
    def test_download_file(self, download_file, url_to_download):
        with TemporaryDirectory() as td, capture_output() as co:
            file = os.path.join(td, 'image.png')
            _func_download_file(url_to_download, file)

            assert os.path.getsize(file) == 3832280
            assert sha1(pathlib.Path(file).read_bytes()) == '6047119e9dab0d4d0ba6c390831b1f85153c5099'

        assert not co.stdout.strip()
        assert co.stderr.strip()

    @responses.activate
    def test_download_file_to_directory(self, download_file, url_to_download):
        with TemporaryDirectory() as td, capture_output() as co:
            _func_download_file(url_to_download, output_directory=td)

            assert os.listdir(td) == ['乐逍遥.png']
            assert os.path.getsize(os.path.join(td, '乐逍遥.png')) == 3832280
            assert sha1(pathlib.Path(os.path.join(td, '乐逍遥.png')).read_bytes()) \
                   == '6047119e9dab0d4d0ba6c390831b1f85153c5099'

        assert not co.stdout.strip()
        assert co.stderr.strip()

    @responses.activate
    def test_download_file_silent(self, download_file, url_to_download):
        with TemporaryDirectory() as td, capture_output() as co:
            file = os.path.join(td, 'image.png')
            _func_download_file(url_to_download, file, silent=True)

            assert os.path.getsize(file) == 3832280
            assert sha1(pathlib.Path(file).read_bytes()) == '6047119e9dab0d4d0ba6c390831b1f85153c5099'

        assert not co.stdout.strip()
        assert not co.stderr.strip()
