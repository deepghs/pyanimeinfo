from typing import Optional


class BangumiTVPageError(Exception):
    def __init__(self, status_code: int, title: str, message: str):
        Exception.__init__(self, status_code, title, message)
        self.status_code = status_code
        self.title = title
        self.message = message


class BangumiTVAPIError(Exception):
    def __init__(self, status_code: int, title: str,
                 description: Optional[str] = None, details: Optional[str] = None):
        Exception.__init__(self, status_code, title, description, details)
        self.status_code = status_code
        self.title = title
        self.description = description
        self.details = details
