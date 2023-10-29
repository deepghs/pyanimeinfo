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

### Accessing Information from bangumi.tv

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

## Important Notes

1. The `pyanimeinfo` library is primarily designed for querying anime-related information and is not a full-fledged
   client for bangumi.tv or any other website. Therefore, we won't be considering support for operations like user
   authentication and user sessions in the short term. Please understand.

2. The reason this library is not named `pybangumitv` is that we don't intend to integrate only the bangumi.tv website.
   In the future, we plan to introduce support for more websites, such as myanimelist, fandom, and others. Stay tuned
   for updates.

