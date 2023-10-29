from typing import Optional


class BangumiTVError(Exception):
    """
    Base exception class for Bangumi.tv API related errors.

    The :class:`BangumiTVError` is the base exception class for all exceptions
    related to interactions with the Bangumi.tv API.
    """


class BangumiTVPageError(BangumiTVError):
    """
    Exception for errors displayed on a Bangumi.tv web page.

    The :class:`BangumiTVPageError` class represents exceptions that are displayed on a Bangumi.tv web page.
    It typically includes information such as the HTTP status code, title, and message for the error.

    :param status_code: The HTTP status code associated with the error.
    :type status_code: int
    :param title: The title or summary of the error.
    :type title: str
    :param message: The detailed error message or description.
    :type message: str
    """

    def __init__(self, status_code: int, title: str, message: str):
        Exception.__init__(self, status_code, title, message)
        self.status_code = status_code
        self.title = title
        self.message = message


class BangumiTVAPIError(BangumiTVError):
    """
    Exception for errors returned in JSON format from the Bangumi.tv API.

    The :class:`BangumiTVAPIError` class represents exceptions that are returned in JSON format when the HTTP
    response status code is in the 4xx range. It typically includes information such as
    the HTTP status code, title, description, and details of the error.

    :param status_code: The HTTP status code associated with the error.
    :type status_code: int
    :param title: The title or summary of the error.
    :type title: str
    :param description: An optional description or additional information about the error.
    :type description: Optional[str]
    :param details: An optional string providing further details about the error.
    :type details: Optional[str]
    """

    def __init__(self, status_code: int, title: str,
                 description: Optional[str] = None, details: Optional[str] = None):
        Exception.__init__(self, status_code, title, description, details)
        self.status_code = status_code
        self.title = title
        self.description = description
        self.details = details
