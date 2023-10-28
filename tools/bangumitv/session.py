from pyanimeinfo.utils import get_session


def _get_bangumitv_session():
    session = get_session()
    session.headers.update({'User-Agent': 'deepghs/pyanimeinfo'})
    return session
