# pyanimeinfo

[![PyPI](https://img.shields.io/pypi/v/pyanimeinfo)](https://pypi.org/project/pyanimeinfo/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyanimeinfo)
![Loc](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/narugo1992/2be1fb0ad747c720587467bf6708063b/raw/loc.json)
![Comments](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/narugo1992/2be1fb0ad747c720587467bf6708063b/raw/comments.json)

[![Code Test](https://github.com/deepghs/pyanimeinfo/workflows/Code%20Test/badge.svg)](https://github.com/deepghs/pyanimeinfo/actions?query=workflow%3A%22Code+Test%22)
[![Package Release](https://github.com/deepghs/pyanimeinfo/workflows/Package%20Release/badge.svg)](https://github.com/deepghs/pyanimeinfo/actions?query=workflow%3A%22Package+Release%22)
[![codecov](https://codecov.io/gh/deepghs/pyanimeinfo/branch/main/graph/badge.svg?token=XJVDP4EFAT)](https://codecov.io/gh/deepghs/pyanimeinfo)

![GitHub Org's stars](https://img.shields.io/github/stars/deepghs)
[![GitHub stars](https://img.shields.io/github/stars/deepghs/pyanimeinfo)](https://github.com/deepghs/pyanimeinfo/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/deepghs/pyanimeinfo)](https://github.com/deepghs/pyanimeinfo/network)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/deepghs/pyanimeinfo)
[![GitHub issues](https://img.shields.io/github/issues/deepghs/pyanimeinfo)](https://github.com/deepghs/pyanimeinfo/issues)
[![GitHub pulls](https://img.shields.io/github/issues-pr/deepghs/pyanimeinfo)](https://github.com/deepghs/pyanimeinfo/pulls)
[![Contributors](https://img.shields.io/github/contributors/deepghs/pyanimeinfo)](https://github.com/deepghs/pyanimeinfo/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/deepghs/pyanimeinfo)](https://github.com/deepghs/pyanimeinfo/blob/master/LICENSE)

Python anime information grabber

## Installation

You can simply install it with `pip` command line from the official PyPI site.

```shell
pip install pyanimeinfo
```

For more information about installation, you can refer
to [Installation](https://deepghs.github.io/pyanimeinfo/main/tutorials/installation/index.html).

## Quick Start

### Accessing Information from Bangumi.tv

We can retrieve information from [Bangumi.tv](https://bangumi.tv/).

```python
from pyanimeinfo.bangumitv import BangumiTVClient

client = BangumiTVClient()

# search subject from bangumi.tv
client.search_subjects('Railgun')

# query specific subject from bangumi.tv
# e.g. Railgun
client.get_subject(2585)

# list characters in this subjects
client.get_subject_characters(2585)

# query specific character
client.get_character(3575)

# list character related persons
# e.g. CV, artists
client.get_character_related_persons(3575)

# list character related subjects
# e.g. Railgun series
client.get_character_related_subjects(3575)

# get person
client.get_person(4670)
```

### Accessing Information from MyAnimeList.net

We can access information from [MyAnimeList](https://myanimelist.net/). However, since the original MyAnimeList site
does not provide a useful API, we utilize the unofficial API [Jikan V4](https://jikan.moe/) to retrieve data from
MyAnimeList.

```python
from pyanimeinfo.myanimelist import JikanV4Client

client = JikanV4Client()

# search animes
client.search_anime('Railgun')

# get specific anime
client.get_anime(6213)

# get full information of specific anime
client.get_anime_full(6213)

# get characters in specific anime
client.get_anime_characters(6213)

# search characters
client.search_anime('misaka mikoto')

# get specific character
client.get_character(13701)

# get full information of specific character
client.get_character_full(13701)

# get character related information
client.get_character_related_animes(13701)
client.get_character_related_manga(13701)
client.get_character_voice_actors(13701)
client.get_character_pictures(13701)

```

## Important Notes

1. The `pyanimeinfo` library is primarily designed for querying anime-related information and is not a comprehensive
   client for bangumi.tv or any other website. Therefore, we currently do not plan to provide support for operations
   like user authentication and user sessions in the short term. Your understanding is appreciated.

2. The reason this library is not named `pybangumitv` is that our intention is not limited to integrating only the
   bangumi.tv website. In the future, we aim to introduce support for additional websites, including MyAnimeList,
   Fandom, and others. Stay tuned for updates.

