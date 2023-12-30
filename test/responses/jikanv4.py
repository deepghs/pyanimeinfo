from pyanimeinfo.myanimelist import JikanV4Client
from test.responses import resp_recorder


@resp_recorder()
def jikanv4_search_anime():
    client = JikanV4Client()
    client.search_anime('Railgun')
    client.search_anime('Railgun', type_='ova')
    client.search_anime('Rokudou no Onna-tachi')
