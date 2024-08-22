import pytest
import responses
from hbutils.testing import isolated_directory
from imgutils.data import load_image
from requests import HTTPError

from pyanimeinfo.myanimelist import JikanV4Client
from pyanimeinfo.utils import download_file
from test.testings import get_testfile


@pytest.fixture()
def client() -> JikanV4Client:
    return JikanV4Client()


@pytest.mark.unittest
class TestJikanv4Client:
    @responses.activate
    def test_search_anime(self, client, jikanv4_search_anime):
        lst = client.search_anime('Railgun')
        assert isinstance(lst, list)
        assert len(lst) == 10
        assert lst[0] == {
            'aired': {'from': '2009-10-03T00:00:00+00:00',
                      'prop': {'from': {'day': 3, 'month': 10, 'year': 2009},
                               'to': {'day': 20, 'month': 3, 'year': 2010}},
                      'string': 'Oct 3, 2009 to Mar 20, 2010',
                      'to': '2010-03-20T00:00:00+00:00'},
            'airing': False,
            'approved': True,
            'background': None,
            'broadcast': {'day': 'Saturdays',
                          'string': 'Saturdays at 01:30 (JST)',
                          'time': '01:30',
                          'timezone': 'Asia/Tokyo'},
            'demographics': [],
            'duration': '24 min per ep',
            'episodes': 24,
            'explicit_genres': [],
            'favorites': 5933,
            'genres': [{'mal_id': 1,
                        'name': 'Action',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/1/Action'},
                       {'mal_id': 10,
                        'name': 'Fantasy',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/10/Fantasy'},
                       {'mal_id': 24,
                        'name': 'Sci-Fi',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/24/Sci-Fi'}],
            'images': {'jpg': {'image_url': 'https://cdn.myanimelist.net/images/anime/8/53581.jpg',
                               'large_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581l.jpg',
                               'small_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581t.jpg'},
                       'webp': {'image_url': 'https://cdn.myanimelist.net/images/anime/8/53581.webp',
                                'large_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581l.webp',
                                'small_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581t.webp'}},
            'licensors': [{'mal_id': 102,
                           'name': 'Funimation',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/102/Funimation'}],
            'mal_id': 6213,
            'members': 601336,
            'popularity': 349,
            'producers': [{'mal_id': 31,
                           'name': 'Geneon Universal Entertainment',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/31/Geneon_Universal_Entertainment'},
                          {'mal_id': 166,
                           'name': 'Movic',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/166/Movic'},
                          {'mal_id': 238,
                           'name': 'AT-X',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/238/AT-X'},
                          {'mal_id': 681,
                           'name': 'ASCII Media Works',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/681/ASCII_Media_Works'}],
            'rank': 1278,
            'rating': 'PG-13 - Teens 13 or older',
            'score': 7.66,
            'scored_by': 284981,
            'season': 'fall',
            'source': 'Manga',
            'status': 'Finished Airing',
            'studios': [{'mal_id': 7,
                         'name': 'J.C.Staff',
                         'type': 'anime',
                         'url': 'https://myanimelist.net/anime/producer/7/JCStaff'}],
            'synopsis': 'The student-filled Academy City is at the forefront of '
                        'scientific advancement and home to the esper development '
                        'program. The seven "Level 5" espers are the most powerful in '
                        'Academy City, and ranked third among them is middle schooler '
                        'Mikoto Misaka, an electricity manipulator known as "The '
                        'Railgun."\n'
                        ' \n'
                        'When strange incidents begin occurring throughout the city, she '
                        'finds each crime to be connected to the elusive "Level Upper," a '
                        'legendary device that allegedly increases the esper level of its '
                        'user. As the situation escalates, it becomes apparent that there '
                        'is more to the Level Upper than meets the eye, and that Academy '
                        'City may be a far more twisted place than the glamorous utopia '
                        'it appears to be.\n'
                        '\n'
                        'Toaru Kagaku no Railgun focuses on Mikoto and her friends—and '
                        'the dangerous situations they find themselves in—as they get '
                        'caught up in the matter of the Level Upper. As Mikoto says, '
                        '"There\'s never a dull moment in this city."\n'
                        '\n'
                        '[Written by MAL Rewrite]',
            'themes': [{'mal_id': 31,
                        'name': 'Super Power',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/31/Super_Power'}],
            'title': 'Toaru Kagaku no Railgun',
            'title_english': 'A Certain Scientific Railgun',
            'title_japanese': 'とある科学の超電磁砲',
            'title_synonyms': ['Toaru Kagaku no Choudenjihou'],
            'titles': [{'title': 'Toaru Kagaku no Railgun', 'type': 'Default'},
                       {'title': 'Toaru Kagaku no Choudenjihou', 'type': 'Synonym'},
                       {'title': 'とある科学の超電磁砲', 'type': 'Japanese'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'English'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'German'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'Spanish'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'French'}],
            'trailer': {
                'embed_url': 'https://www.youtube.com/embed/0YX5dkR4tpk?enablejsapi=1&wmode=opaque&autoplay=1',
                'images': {'image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/default.jpg',
                           'large_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/hqdefault.jpg',
                           'maximum_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/maxresdefault.jpg',
                           'medium_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/mqdefault.jpg',
                           'small_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/sddefault.jpg'},
                'url': 'https://www.youtube.com/watch?v=0YX5dkR4tpk',
                'youtube_id': '0YX5dkR4tpk'},
            'type': 'TV',
            'url': 'https://myanimelist.net/anime/6213/Toaru_Kagaku_no_Railgun',
            'year': 2009
        }

        lst = client.search_anime('Railgun', type_='ova')
        assert isinstance(lst, list)
        assert len(lst) == 3
        assert lst[0]['type'] == 'OVA'
        assert lst[0]['title'] == 'Toaru Kagaku no Railgun S: Daiji na Koto wa Zenbu Sentou ni Osowatta'
        assert lst[0]['title_japanese'] == 'とある科学の超電磁砲S 大事なことはぜんぶ銭湯に教わった'

        lst = client.search_anime('Rokudou no Onna-tachi')
        assert isinstance(lst, list)
        assert len(lst) == 25

    @responses.activate
    def test_get_anime(self, client, jikanv4_get_anime):
        info = client.get_anime(6213)
        assert info == {
            'aired': {'from': '2009-10-03T00:00:00+00:00',
                      'prop': {'from': {'day': 3, 'month': 10, 'year': 2009},
                               'to': {'day': 20, 'month': 3, 'year': 2010}},
                      'string': 'Oct 3, 2009 to Mar 20, 2010',
                      'to': '2010-03-20T00:00:00+00:00'},
            'airing': False,
            'approved': True,
            'background': None,
            'broadcast': {'day': 'Saturdays',
                          'string': 'Saturdays at 01:30 (JST)',
                          'time': '01:30',
                          'timezone': 'Asia/Tokyo'},
            'demographics': [],
            'duration': '24 min per ep',
            'episodes': 24,
            'explicit_genres': [],
            'favorites': 5933,
            'genres': [{'mal_id': 1,
                        'name': 'Action',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/1/Action'},
                       {'mal_id': 10,
                        'name': 'Fantasy',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/10/Fantasy'},
                       {'mal_id': 24,
                        'name': 'Sci-Fi',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/24/Sci-Fi'}],
            'images': {'jpg': {'image_url': 'https://cdn.myanimelist.net/images/anime/8/53581.jpg',
                               'large_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581l.jpg',
                               'small_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581t.jpg'},
                       'webp': {'image_url': 'https://cdn.myanimelist.net/images/anime/8/53581.webp',
                                'large_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581l.webp',
                                'small_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581t.webp'}},
            'licensors': [{'mal_id': 102,
                           'name': 'Funimation',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/102/Funimation'}],
            'mal_id': 6213,
            'members': 601336,
            'popularity': 349,
            'producers': [{'mal_id': 31,
                           'name': 'Geneon Universal Entertainment',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/31/Geneon_Universal_Entertainment'},
                          {'mal_id': 166,
                           'name': 'Movic',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/166/Movic'},
                          {'mal_id': 238,
                           'name': 'AT-X',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/238/AT-X'},
                          {'mal_id': 681,
                           'name': 'ASCII Media Works',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/681/ASCII_Media_Works'}],
            'rank': 1278,
            'rating': 'PG-13 - Teens 13 or older',
            'score': 7.66,
            'scored_by': 284981,
            'season': 'fall',
            'source': 'Manga',
            'status': 'Finished Airing',
            'studios': [{'mal_id': 7,
                         'name': 'J.C.Staff',
                         'type': 'anime',
                         'url': 'https://myanimelist.net/anime/producer/7/JCStaff'}],
            'synopsis': 'The student-filled Academy City is at the forefront of '
                        'scientific advancement and home to the esper development '
                        'program. The seven "Level 5" espers are the most powerful in '
                        'Academy City, and ranked third among them is middle schooler '
                        'Mikoto Misaka, an electricity manipulator known as "The '
                        'Railgun."\n'
                        ' \n'
                        'When strange incidents begin occurring throughout the city, she '
                        'finds each crime to be connected to the elusive "Level Upper," a '
                        'legendary device that allegedly increases the esper level of its '
                        'user. As the situation escalates, it becomes apparent that there '
                        'is more to the Level Upper than meets the eye, and that Academy '
                        'City may be a far more twisted place than the glamorous utopia '
                        'it appears to be.\n'
                        '\n'
                        'Toaru Kagaku no Railgun focuses on Mikoto and her friends—and '
                        'the dangerous situations they find themselves in—as they get '
                        'caught up in the matter of the Level Upper. As Mikoto says, '
                        '"There\'s never a dull moment in this city."\n'
                        '\n'
                        '[Written by MAL Rewrite]',
            'themes': [{'mal_id': 31,
                        'name': 'Super Power',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/31/Super_Power'}],
            'title': 'Toaru Kagaku no Railgun',
            'title_english': 'A Certain Scientific Railgun',
            'title_japanese': 'とある科学の超電磁砲',
            'title_synonyms': ['Toaru Kagaku no Choudenjihou'],
            'titles': [{'title': 'Toaru Kagaku no Railgun', 'type': 'Default'},
                       {'title': 'Toaru Kagaku no Choudenjihou', 'type': 'Synonym'},
                       {'title': 'とある科学の超電磁砲', 'type': 'Japanese'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'English'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'German'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'Spanish'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'French'}],
            'trailer': {'embed_url': 'https://www.youtube.com/embed/0YX5dkR4tpk?enablejsapi=1&wmode=opaque&autoplay=1',
                        'images': {'image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/default.jpg',
                                   'large_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/hqdefault.jpg',
                                   'maximum_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/maxresdefault.jpg',
                                   'medium_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/mqdefault.jpg',
                                   'small_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/sddefault.jpg'},
                        'url': 'https://www.youtube.com/watch?v=0YX5dkR4tpk',
                        'youtube_id': '0YX5dkR4tpk'},
            'type': 'TV',
            'url': 'https://myanimelist.net/anime/6213/Toaru_Kagaku_no_Railgun',
            'year': 2009
        }

        with pytest.raises(HTTPError) as ei:
            client.get_anime(621333333)
        assert ei.value.response.status_code == 404

    @responses.activate
    def test_get_anime_full(self, client, jikanv4_get_anime_full):
        info = client.get_anime_full(6213)
        assert info == {
            'aired': {'from': '2009-10-03T00:00:00+00:00',
                      'prop': {'from': {'day': 3, 'month': 10, 'year': 2009},
                               'to': {'day': 20, 'month': 3, 'year': 2010}},
                      'string': 'Oct 3, 2009 to Mar 20, 2010',
                      'to': '2010-03-20T00:00:00+00:00'},
            'airing': False,
            'approved': True,
            'background': None,
            'broadcast': {'day': 'Saturdays',
                          'string': 'Saturdays at 01:30 (JST)',
                          'time': '01:30',
                          'timezone': 'Asia/Tokyo'},
            'demographics': [],
            'duration': '24 min per ep',
            'episodes': 24,
            'explicit_genres': [],
            'external': [{'name': 'Official Site',
                          'url': 'http://toaru-project.com/railgun/'},
                         {'name': 'AniDB',
                          'url': 'https://anidb.net/perl-bin/animedb.pl?show=anime&aid=6460'},
                         {'name': 'ANN',
                          'url': 'https://www.animenewsnetwork.com/encyclopedia/anime.php?id=10706'},
                         {'name': 'Wikipedia',
                          'url': 'http://en.wikipedia.org/wiki/A_Certain_Scientific_Railgun'}],
            'favorites': 5933,
            'genres': [{'mal_id': 1,
                        'name': 'Action',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/1/Action'},
                       {'mal_id': 10,
                        'name': 'Fantasy',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/10/Fantasy'},
                       {'mal_id': 24,
                        'name': 'Sci-Fi',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/24/Sci-Fi'}],
            'images': {'jpg': {'image_url': 'https://cdn.myanimelist.net/images/anime/8/53581.jpg',
                               'large_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581l.jpg',
                               'small_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581t.jpg'},
                       'webp': {'image_url': 'https://cdn.myanimelist.net/images/anime/8/53581.webp',
                                'large_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581l.webp',
                                'small_image_url': 'https://cdn.myanimelist.net/images/anime/8/53581t.webp'}},
            'licensors': [{'mal_id': 102,
                           'name': 'Funimation',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/102/Funimation'}],
            'mal_id': 6213,
            'members': 601336,
            'popularity': 349,
            'producers': [{'mal_id': 31,
                           'name': 'Geneon Universal Entertainment',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/31/Geneon_Universal_Entertainment'},
                          {'mal_id': 166,
                           'name': 'Movic',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/166/Movic'},
                          {'mal_id': 238,
                           'name': 'AT-X',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/238/AT-X'},
                          {'mal_id': 681,
                           'name': 'ASCII Media Works',
                           'type': 'anime',
                           'url': 'https://myanimelist.net/anime/producer/681/ASCII_Media_Works'}],
            'rank': 1278,
            'rating': 'PG-13 - Teens 13 or older',
            'relations': [{'entry': [{'mal_id': 7776,
                                      'name': 'Toaru Majutsu no Index Gaiden: Toaru '
                                              'Kagaku no Railgun',
                                      'type': 'manga',
                                      'url': 'https://myanimelist.net/manga/7776/Toaru_Majutsu_no_Index_Gaiden__Toaru_Kagaku_no_Railgun'}],
                           'relation': 'Adaptation'},
                          {'entry': [{'mal_id': 4654,
                                      'name': 'Toaru Majutsu no Index',
                                      'type': 'anime',
                                      'url': 'https://myanimelist.net/anime/4654/Toaru_Majutsu_no_Index'}],
                           'relation': 'Parent story'},
                          {'entry': [{'mal_id': 8023,
                                      'name': 'Toaru Kagaku no Railgun: Motto Marutto '
                                              'Railgun',
                                      'type': 'anime',
                                      'url': 'https://myanimelist.net/anime/8023/Toaru_Kagaku_no_Railgun__Motto_Marutto_Railgun'}],
                           'relation': 'Spin-off'},
                          {'entry': [{'mal_id': 9047,
                                      'name': 'Toaru Kagaku no Railgun: Misaka-san wa Ima '
                                              'Chuumoku no Mato desu kara',
                                      'type': 'anime',
                                      'url': 'https://myanimelist.net/anime/9047/Toaru_Kagaku_no_Railgun__Misaka-san_wa_Ima_Chuumoku_no_Mato_desu_kara'},
                                     {'mal_id': 9063,
                                      'name': 'Toaru Kagaku no Railgun: Entenka no '
                                              'Satsuei Model mo Raku Ja Arimasen wa ne.',
                                      'type': 'anime',
                                      'url': 'https://myanimelist.net/anime/9063/Toaru_Kagaku_no_Railgun__Entenka_no_Satsuei_Model_mo_Raku_Ja_Arimasen_wa_ne'}],
                           'relation': 'Side story'},
                          {'entry': [{'mal_id': 16049,
                                      'name': 'Toaru Kagaku no Railgun S',
                                      'type': 'anime',
                                      'url': 'https://myanimelist.net/anime/16049/Toaru_Kagaku_no_Railgun_S'}],
                           'relation': 'Sequel'},
                          {'entry': [{'mal_id': 27509,
                                      'name': 'Toaru Majutsu no Index 10-shuunen Kinen PV',
                                      'type': 'anime',
                                      'url': 'https://myanimelist.net/anime/27509/Toaru_Majutsu_no_Index_10-shuunen_Kinen_PV'}],
                           'relation': 'Character'}],
            'score': 7.66,
            'scored_by': 284981,
            'season': 'fall',
            'source': 'Manga',
            'status': 'Finished Airing',
            'streaming': [{'name': 'Crunchyroll',
                           'url': 'http://www.crunchyroll.com/series-271889'},
                          {'name': 'Funimation',
                           'url': 'https://www.funimation.com/shows/a-certain-scientific-railgun'},
                          {'name': 'Netflix', 'url': 'https://www.netflix.com/'}],
            'studios': [{'mal_id': 7,
                         'name': 'J.C.Staff',
                         'type': 'anime',
                         'url': 'https://myanimelist.net/anime/producer/7/JCStaff'}],
            'synopsis': 'The student-filled Academy City is at the forefront of '
                        'scientific advancement and home to the esper development '
                        'program. The seven "Level 5" espers are the most powerful in '
                        'Academy City, and ranked third among them is middle schooler '
                        'Mikoto Misaka, an electricity manipulator known as "The '
                        'Railgun."\n'
                        ' \n'
                        'When strange incidents begin occurring throughout the city, she '
                        'finds each crime to be connected to the elusive "Level Upper," a '
                        'legendary device that allegedly increases the esper level of its '
                        'user. As the situation escalates, it becomes apparent that there '
                        'is more to the Level Upper than meets the eye, and that Academy '
                        'City may be a far more twisted place than the glamorous utopia '
                        'it appears to be.\n'
                        '\n'
                        'Toaru Kagaku no Railgun focuses on Mikoto and her friends—and '
                        'the dangerous situations they find themselves in—as they get '
                        'caught up in the matter of the Level Upper. As Mikoto says, '
                        '"There\'s never a dull moment in this city."\n'
                        '\n'
                        '[Written by MAL Rewrite]',
            'theme': {'endings': ['1: "only my railgun" by fripSide (eps 1)',
                                  '2: "Dear My Friend -Mada Minu Mirai he-" by ELISA (eps '
                                  '2-11, 13-14, 24)',
                                  '3: "Smile -You and Me-" by ELISA (eps 12)',
                                  '4: "Real Force" by ELISA (eps 15-23)'],
                      'openings': ['1: "only my railgun" by fripSide (eps 2-14)',
                                   '2: "LEVEL 5 -judgelight-" by fripSide (eps 15-23)']},
            'themes': [{'mal_id': 31,
                        'name': 'Super Power',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/31/Super_Power'}],
            'title': 'Toaru Kagaku no Railgun',
            'title_english': 'A Certain Scientific Railgun',
            'title_japanese': 'とある科学の超電磁砲',
            'title_synonyms': ['Toaru Kagaku no Choudenjihou'],
            'titles': [{'title': 'Toaru Kagaku no Railgun', 'type': 'Default'},
                       {'title': 'Toaru Kagaku no Choudenjihou', 'type': 'Synonym'},
                       {'title': 'とある科学の超電磁砲', 'type': 'Japanese'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'English'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'German'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'Spanish'},
                       {'title': 'A Certain Scientific Railgun', 'type': 'French'}],
            'trailer': {'embed_url': 'https://www.youtube.com/embed/0YX5dkR4tpk?enablejsapi=1&wmode=opaque&autoplay=1',
                        'images': {'image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/default.jpg',
                                   'large_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/hqdefault.jpg',
                                   'maximum_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/maxresdefault.jpg',
                                   'medium_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/mqdefault.jpg',
                                   'small_image_url': 'https://img.youtube.com/vi/0YX5dkR4tpk/sddefault.jpg'},
                        'url': 'https://www.youtube.com/watch?v=0YX5dkR4tpk',
                        'youtube_id': '0YX5dkR4tpk'},
            'type': 'TV',
            'url': 'https://myanimelist.net/anime/6213/Toaru_Kagaku_no_Railgun',
            'year': 2009
        }

        with pytest.raises(HTTPError) as ei:
            client.get_anime_full(621333333)
        assert ei.value.response.status_code == 404

    @responses.activate
    def test_get_anime_pictures(self, client, jikanv4_get_anime_pictures, image_diff):
        imgs = client.get_anime_pictures(6213)
        assert len(imgs) == 8
        with isolated_directory():
            for i, item in enumerate(imgs):
                download_file(item['jpg']['image_url'], f'{i}-test.jpg')
                # download_file(item['jpg']['image_url'], get_testfile('railgun_anime', f'{i}.jpg'))

                assert image_diff(
                    load_image(f'{i}-test.jpg'),
                    load_image(get_testfile('railgun_anime', f'{i}.jpg')),
                    throw_exception=False
                ) <= 1e-2

    @responses.activate
    def test_get_anime_characters(self, client, jikanv4_get_anime_characters):
        info = client.get_anime_characters(6213)
        lst = [(item['character']['mal_id'], item['character']['name']) for item in info]
        assert lst == [
            (13701, 'Misaka, Mikoto'),
            (20626, 'Saten, Ruiko'),
            (17017, 'Shirai, Kuroko'),
            (20622, 'Uiharu, Kazari'),
            (227071, 'Akemi'),
            (29090, 'Awatsuki, Maaya'),
            (30237, 'Daigo'),
            (31499, 'Edasaki, Banri'),
            (30455, 'Haruue, Erii'),
            (186090, 'Hazamaya, Kana'),
            (23513, 'Heaven Canceller'),
            (101995, 'Hebitani, Tsuguo'),
            (17179, 'Himegami, Aisa'),
            (13699, 'Index Librorum Prohibitorum'),
            (27016, 'Juufuku, Miho'),
            (41873, 'Kaitabi, Hatsuya'),
            (13700, 'Kamijou, Touma'),
            (42500, 'Kihara, Gensei'),
            (30481, 'Kihara Lifeline, Therestina'),
            (20620, 'Kiyama, Harumi'),
            (28986, 'Kongou, Mitsuko'),
            (26941, 'Konori, Mii'),
            (37890, 'Kounoe, Haruki'),
            (29827, 'Kurozuma, Wataru'),
            (31500, 'Ryoukan'),
            (29082, 'Tessou, Tsuzuri'),
            (124059, 'Trick'),
            (17785, 'Tsuchimikado, Maika'),
            (16222, 'Tsukuyomi, Komoe'),
            (29087, 'Wannai, Kinuho'),
            (31444, 'Woman Gang Boss'),
            (92069, 'Yanagisako, Aomi'),
            (29083, 'Yomikawa, Aiho')
        ]

    @responses.activate
    def test_search_characters(self, client, jikanv4_search_characters):
        info = client.search_characters('Misaka')
        lst = [
            (item['mal_id'], item['name'], item['name_kanji'])
            for item in info
        ]
        assert lst == [
            (69579, 'Misaka', None),
            (210826, 'Haruko Misaka', '御坂 春子'),
            (176077, 'Renji Misaka', None),
            (107027, 'Will of the Whole Misaka Network', 'ミサカネットワーク総体'),
            (40371, 'Tabikake Misaka', None),
            (161672, 'Inuhiko Misaka', '三坂 犬彦'),
            (82297, 'MISAKA 1', 'ミサカ1号'),
            (39990, 'Misaka Worst', 'ミサカ・ワースト'),
            (68429, 'MISAKA 10777', ' ミサカ10777号 '),
            (36875, 'Misuzu Misaka', '美坂 美鈴'),
            (135283, 'Kyouji Misaka', '御坂 矜持'),
            (40144, 'MISAKA 9982', 'ミサカ9982号'),
            (321, 'Kaori Misaka', '美坂 香里'),
            (317, 'Shiori Misaka', '美坂 栞'),
            (17729, 'MISAKA 10032', '御坂妹, ミサカ10032号'),
            (40143, 'MISAKA 10031', 'ミサカ10031号'),
            (13701, 'Mikoto Misaka', '御坂 美琴'),
            (124507, 'MISAKA 19090', 'ミサカ19090号'),
            (137778, 'MISAKA 10046', 'ミサカ10046号'),
            (237450, 'Gorou Misaki', '岬 悟郎'),
            (235860, 'Misaki Hotori', '畔 美岬'),
            (236518, 'Misaki Tadano', None),
            (236090, 'Misako Hara', None),
            (236107, 'Misaki', None),
            (234778, 'Akane Misaki', '美崎 茜')
        ]

    @responses.activate
    def test_get_character(self, client, jikanv4_get_character):
        info = client.get_character(13701)
        assert info['mal_id'] == 13701
        assert info['name'] == 'Mikoto Misaka'
        assert info['name_kanji'] == '御坂 美琴'
        assert 'voices' not in info

        info = client.get_character(20626)
        assert info['mal_id'] == 20626
        assert info['name'] == 'Ruiko Saten'
        assert info['name_kanji'] == '佐天 涙子'
        assert 'voices' not in info

    @responses.activate
    def test_get_character_full(self, client, jikanv4_get_character_full):
        info = client.get_character_full(13701)
        assert info['mal_id'] == 13701
        assert info['name'] == 'Mikoto Misaka'
        assert info['name_kanji'] == '御坂 美琴'
        assert 'voices' in info

        info = client.get_character_full(20626)
        assert info['mal_id'] == 20626
        assert info['name'] == 'Ruiko Saten'
        assert info['name_kanji'] == '佐天 涙子'
        assert 'voices' in info

    @responses.activate
    def test_get_character_related_animes(self, client, jikanv4_get_character_related_animes):
        lst = client.get_character_related_animes(13701)
        assert len(lst) == 16
        assert [
                   (item['anime']['mal_id'], item['role'], item['anime']['title'])
                   for item in lst
               ] == [
                   (4654, 'Supporting', 'Toaru Majutsu no Index'),
                   (5955, 'Main', 'Toaru Majutsu no Index-tan'),
                   (6213, 'Main', 'Toaru Kagaku no Railgun'),
                   (8023, 'Main', 'Toaru Kagaku no Railgun: Motto Marutto Railgun'),
                   (8937, 'Supporting', 'Toaru Majutsu no Index II'),
                   (9047, 'Main',
                    'Toaru Kagaku no Railgun: Misaka-san wa Ima Chuumoku no Mato desu kara'),
                   (9063, 'Main',
                    'Toaru Kagaku no Railgun: Entenka no Satsuei Model mo Raku Ja Arimasen wa '
                    'ne.'),
                   (10249, 'Supporting', 'Toaru Majutsu no Index-tan II'),
                   (11743, 'Supporting', 'Toaru Majutsu no Index Movie: Endymion no Kiseki'),
                   (16049, 'Main', 'Toaru Kagaku no Railgun S'),
                   (19697, 'Main', 'Toaru Kagaku no Railgun S: Motto Marutto Railgun'),
                   (20035, 'Supporting',
                    'Toaru Majutsu no Index-tan Movie: Endymion no Kiseki - Ga Attari Nakattari'),
                   (22759, 'Main',
                    'Toaru Kagaku no Railgun S: Daiji na Koto wa Zenbu Sentou ni Osowatta'),
                   (27509, 'Supporting', 'Toaru Majutsu no Index 10-shuunen Kinen PV'),
                   (36432, 'Supporting', 'Toaru Majutsu no Index III'),
                   (38481, 'Main', 'Toaru Kagaku no Railgun T')
               ]

    @responses.activate
    def test_get_character_related_manga(self, client, jikanv4_get_character_related_manga):
        lst = client.get_character_related_manga(13701)
        assert len(lst) == 22
        assert [
                   (item['manga']['mal_id'], item['role'], item['manga']['title'])
                   for item in lst
               ] == [
                   (7775, 'Supporting', 'Toaru Majutsu no Index'),
                   (7776, 'Main', 'Toaru Majutsu no Index Gaiden: Toaru Kagaku no Railgun'),
                   (12854, 'Supporting', 'Toaru Majutsu no Index'),
                   (24875, 'Supporting', 'Shinyaku Toaru Majutsu no Index'),
                   (27843, 'Main', 'Toaru Kagaku no Railgun SS'),
                   (28973, 'Main', 'Toaru Kagaku no Railgun SS2'),
                   (31649, 'Supporting', 'Toaru Majutsu no Index SP'),
                   (31651, 'Supporting', 'Toaru Majutsu no Index SS'),
                   (36561,
                    'Main',
                    'Toaru Kagaku no Railgun SS: Dasoku, Mata wa Toaru Jiken no Shuusoku'),
                   (47483, 'Main', 'Toaru Kagaku no Railgun: Giten Railgun'),
                   (48745, 'Supporting', 'Toaru Majutsu no Index: Road to Endymion'),
                   (48923, 'Supporting', 'Toaru Majutsu no Index: Endymion no Kiseki'),
                   (50715, 'Supporting', 'Toaru Majutsu no Index SS: Love Letter Soudatsusen'),
                   (70997, 'Supporting', 'Toaru Nichijou no Index-san'),
                   (79807, 'Supporting', 'Shinyaku Toaru Majutsu no Index SS'),
                   (85141,
                    'Main',
                    'Toaru Majutsu no Heavy na Zashiki Warashi ga Kantan na Satsujinki no '
                    'Konkatsu Jijou'),
                   (85471,
                    'Main',
                    'Toaru Majutsu no Heavy na Zashiki Warashi ga Kantan na Satsujinki no '
                    'Konkatsu Jijou'),
                   (93892, 'Supporting', 'Toaru Idol no Accelerator-sama'),
                   (105912, 'Supporting', 'Toaru Kagaku no Railgun Gaiden: Astral Buddy'),
                   (121693, 'Supporting', 'Toaru Kagaku no Railgun SS3'),
                   (124374, 'Supporting', 'Souyaku Toaru Majutsu no Index'),
                   (139100,
                    'Supporting',
                    'Toaru Majutsu no Index Gaiden: Toaru Kagaku no Mental Out')
               ]

    @responses.activate
    def test_get_character_voice_actors(self, client, jikanv4_get_character_voice_actors):
        info = client.get_character_voice_actors(13701)
        assert [
                   (item['language'], item['person']['mal_id'], item['person']['name'])
                   for item in info
               ] == [
                   ('Japanese', 241, 'Satou, Rina'),
                   ('English', 414, 'Karbowski, Brittney'),
                   ('Korean', 14773, 'Wu, Jeong Sin'),
                   ('German', 56866, 'Freund, Alina')
               ]

    @responses.activate
    def test_get_character_pictures(self, client, jikanv4_get_character_pictures, image_diff):
        imgs = client.get_character_pictures(13701)
        assert len(imgs) == 19
        with isolated_directory():
            for i, item in enumerate(imgs):
                download_file(item['jpg']['image_url'], f'{i}-test.jpg')
                assert image_diff(
                    load_image(f'{i}-test.jpg'),
                    load_image(get_testfile('misaka_mikoto', f'{i}.jpg')),
                    throw_exception=False
                ) <= 1e-2

    @responses.activate
    def test_get_manga(self, client, jikanv4_get_manga):
        info = client.get_manga(7776)
        assert info['mal_id'] == 7776
        assert info['title'] == 'Toaru Majutsu no Index Gaiden: Toaru Kagaku no Railgun'
        assert info['title_english'] == 'A Certain Scientific Railgun'
        assert info['title_japanese'] == 'とある魔術の禁書目録外伝 とある科学の超電磁砲〈レールガン〉'
        assert info['titles'] == [
            {'title': 'Toaru Majutsu no Index Gaiden: Toaru Kagaku no Railgun',
             'type': 'Default'},
            {'title': 'To Aru Kagaku no Choudenjihou', 'type': 'Synonym'},
            {'title': 'とある魔術の禁書目録外伝 とある科学の超電磁砲〈レールガン〉', 'type': 'Japanese'},
            {'title': 'A Certain Scientific Railgun', 'type': 'English'}
        ]
        assert 'relations' not in info

    @responses.activate
    def test_get_manga_full(self, client, jikanv4_get_manga_full):
        info = client.get_manga_full(7776)
        assert info['mal_id'] == 7776
        assert info['title'] == 'Toaru Majutsu no Index Gaiden: Toaru Kagaku no Railgun'
        assert info['title_english'] == 'A Certain Scientific Railgun'
        assert info['title_japanese'] == 'とある魔術の禁書目録外伝 とある科学の超電磁砲〈レールガン〉'
        assert info['titles'] == [
            {'title': 'Toaru Majutsu no Index Gaiden: Toaru Kagaku no Railgun',
             'type': 'Default'},
            {'title': 'To Aru Kagaku no Choudenjihou', 'type': 'Synonym'},
            {'title': 'とある魔術の禁書目録外伝 とある科学の超電磁砲〈レールガン〉', 'type': 'Japanese'},
            {'title': 'A Certain Scientific Railgun', 'type': 'English'}
        ]
        assert 'relations' in info

    @responses.activate
    def test_get_manga_pictures(self, client, jikanv4_get_manga_pictures, image_diff):
        imgs = client.get_manga_pictures(7776)
        assert len(imgs) == 9
        with isolated_directory():
            for i, item in enumerate(imgs):
                download_file(item['jpg']['image_url'], f'{i}-test.jpg')
                # download_file(item['jpg']['image_url'], get_testfile('railgun_manga', f'{i}.jpg'))

                assert image_diff(
                    load_image(f'{i}-test.jpg'),
                    load_image(get_testfile('railgun_manga', f'{i}.jpg')),
                    throw_exception=False
                ) <= 1e-2

    @responses.activate
    def test_search_manga(self, client, jikanv4_search_manga):
        infos = client.search_manga('railgun')
        assert len(infos) == 12
        assert infos[0]['mal_id'] == 28973

        info_selected = [ix for ix in infos if ix['mal_id'] == 7776]
        assert info_selected, 'No manga 7776 found.'
        info = info_selected[0]
        assert info['mal_id'] == 7776
        assert info['title'] == 'Toaru Majutsu no Index Gaiden: Toaru Kagaku no Railgun'
        assert info['title_english'] == 'A Certain Scientific Railgun'
        assert info['title_japanese'] == 'とある魔術の禁書目録外伝 とある科学の超電磁砲〈レールガン〉'
        assert info['titles'] == [
            {'title': 'Toaru Majutsu no Index Gaiden: Toaru Kagaku no Railgun',
             'type': 'Default'},
            {'title': 'To Aru Kagaku no Choudenjihou', 'type': 'Synonym'},
            {'title': 'とある魔術の禁書目録外伝 とある科学の超電磁砲〈レールガン〉', 'type': 'Japanese'},
            {'title': 'A Certain Scientific Railgun', 'type': 'English'}
        ]
