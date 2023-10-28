import requests

from .base import resp_recorder


@resp_recorder()
def download_file():
    resp = requests.get(
        'https://huggingface.co/datasets/deepghs/game_character_skins/resolve/main/arknights/NM01/%E4%B9%90%E9%80%8D%E9%81%A5.png')
    resp.raise_for_status()
