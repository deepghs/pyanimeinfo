import pytest
import responses

from pyanimeinfo.myanimelist import JikanV4Client


@pytest.fixture()
def client():
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
