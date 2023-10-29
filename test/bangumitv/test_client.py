import pytest
import responses

from pyanimeinfo.bangumitv import BangumiTVClient, SubjectType, BangumiTVPageError, BangumiTVAPIError


@pytest.fixture()
def client():
    return BangumiTVClient()


@pytest.mark.unittest
class TestBangumitvClient:
    @responses.activate
    def test_search_bangumi(self, client, bangumitv_search):
        data = client.search_subjects('Railgun')
        assert data['results'] == 23

        # I don't know what the fxxk with this API neither,
        # so I opened an issue: https://github.com/bangumi/api/issues/195
        assert len(data['list']) == 15

        for item in data['list']:
            assert 'id' in item
            assert 'url' in item
            assert 'type' in item
            assert 'name' in item
            assert 'name_cn' in item
            assert 'images' in item
            assert 'collection' not in item

    @responses.activate
    def test_search_bangumi_large(self, client, bangumitv_search):
        data = client.search_subjects('Railgun', response_group='large')
        assert data['results'] == 23

        # I don't know what the fxxk with this API neither,
        # so I opened an issue: https://github.com/bangumi/api/issues/195
        assert len(data['list']) == 15

        for item in data['list']:
            assert 'id' in item
            assert 'url' in item
            assert 'type' in item
            assert 'name' in item
            assert 'name_cn' in item
            assert 'images' in item
            assert 'collection' in item

    @responses.activate
    def test_search_bangumi_large_anime(self, client, bangumitv_search):
        data = client.search_subjects('Railgun', response_group='large', type_=SubjectType.ANIME)
        assert data['results'] == 8

        # I don't know what the fxxk with this API neither,
        # so I opened an issue: https://github.com/bangumi/api/issues/195
        assert len(data['list']) == 4

        for item in data['list']:
            assert 'id' in item
            assert 'url' in item
            assert item['type'] == SubjectType.ANIME
            assert 'name' in item
            assert 'name_cn' in item
            assert 'images' in item
            assert 'rating' in item
            assert 'collection' in item

    @responses.activate
    def test_search_bangumi_not_found(self, client, bangumitv_search):
        with pytest.raises(BangumiTVPageError) as ei:
            _ = client.search_subjects('Railgunksdjflksdjflsdjflsdjflsdjfl')

        err = ei.value
        assert isinstance(err, BangumiTVPageError)
        assert err.status_code == 200
        assert err.title == '呜咕，出错了'
        assert err.message == '对不起，您在 秒内只能进行一次搜索，请返回。'

    @responses.activate
    def test_get_subject(self, client, bangumitv_subject):
        data = client.get_subject(2585)
        assert data['id'] == 2585
        assert data['name'] == 'とある科学の超電磁砲'
        assert data['name_cn'] == '某科学的超电磁炮'

    @responses.activate
    def test_get_subject_not_found(self, client, bangumitv_subject):
        with pytest.raises(BangumiTVAPIError) as ei:
            _ = client.get_subject(25852585)

        err = ei.value
        assert isinstance(err, BangumiTVAPIError)
        assert err.status_code == 404
        assert err.title == 'Not Found'
        assert err.description == 'resource can\'t be found in the database or has been removed'
        assert err.details == {'method': 'GET', 'path': '/v0/subjects/25852585'}

    @responses.activate
    def test_get_subject_persons(self, client, bangumitv_subject):
        data = client.get_subject_persons(2585)
        assert isinstance(data, list)
        assert len(data) == 237
        for item in data:
            assert 'id' in item
            assert 'career' in item
            assert 'images' in item
            assert 'name' in item
            assert 'relation' in item
            assert 'type' in item

    @responses.activate
    def test_get_subject_characters(self, client, bangumitv_subject):
        data = client.get_subject_characters(2585)
        assert isinstance(data, list)
        assert len(data) == 74
        for item in data:
            assert 'id' in item
            assert 'actors' in item
            assert 'images' in item
            assert 'name' in item
            assert 'relation' in item
            assert 'type' in item

    @responses.activate
    def test_get_subject_relations(self, client, bangumitv_subject):
        data = client.get_subject_relations(2585)
        assert isinstance(data, list)
        assert len(data) == 21
        for item in data:
            assert 'id' in item
            assert 'images' in item
            assert 'name' in item
            assert 'name_cn' in item
            assert 'relation' in item
            assert 'type' in item
