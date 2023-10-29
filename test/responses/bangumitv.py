from pyanimeinfo.bangumitv import BangumiTVClient, SubjectType, BangumiTVPageError, BangumiTVAPIError
from .base import resp_recorder


@resp_recorder()
def bangumitv_search():
    client = BangumiTVClient()
    _ = client.search_subjects('Railgun')
    _ = client.search_subjects('Railgun', response_group='large')
    _ = client.search_subjects('Railgun', response_group='large', type_=SubjectType.ANIME)
    try:
        _ = client.search_subjects('Railgunksdjflksdjflsdjflsdjflsdjfl')
    except BangumiTVPageError:
        pass


@resp_recorder()
def bangumitv_subject():
    client = BangumiTVClient()
    _ = client.get_subject(2585)
    try:
        _ = client.get_subject(25852585)
    except BangumiTVAPIError:
        pass

    _ = client.get_subject_persons(2585)
    _ = client.get_subject_characters(2585)
    _ = client.get_subject_relations(2585)
