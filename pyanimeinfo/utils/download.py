import os

import pyrfc6266
import requests

from .session import get_session
from .tqdm_ import tqdm


def download_file(url, filename=None, output_directory=None,
                  expected_size: int = None, desc=None, session=None, silent: bool = False,
                  **kwargs):
    """
    Download a file from a given URL to the local file system.

    This function downloads a file from a specified URL and saves it to the local file system. It supports optional parameters such as specifying the output filename, output directory, and expected file size.

    :param url: The URL from which to download the file.
    :type url: str
    :param filename: The local filename to save the downloaded file. If not provided, the function tries to extract it from the response headers.
    :type filename: str, optional
    :param output_directory: The directory where the downloaded file should be saved. If provided, the filename is combined with this directory.
    :type output_directory: str, optional
    :param expected_size: The expected size of the downloaded file in bytes. If specified, the function checks whether the downloaded file size matches the expected size.
    :type expected_size: int, optional
    :param desc: The description to be displayed during the download progress (e.g., in a progress bar).
    :type desc: str, optional
    :param session: An optional `requests.Session` object to be used for making the HTTP request.
    :type session: requests.Session, optional
    :param silent: If True, suppresses the progress bar and download progress display.
    :type silent: bool
    :param **kwargs: Additional keyword arguments to pass to the `requests.get` method.

    :return: The filename where the downloaded file is saved.
    :rtype: str

    :raises requests.exceptions.HTTPError: If the downloaded file size does not match the expected size (if provided).
    """
    session = session or get_session()
    response = session.get(url, stream=True, allow_redirects=True, **kwargs)
    expected_size = expected_size or response.headers.get('Content-Length', None)
    if filename is None:
        filename = pyrfc6266.parse_filename(response.headers.get('Content-Disposition'))
    if output_directory is not None:
        filename = os.path.join(output_directory, filename)
    expected_size = int(expected_size) if expected_size is not None else expected_size

    desc = desc or os.path.basename(filename)
    directory = os.path.dirname(filename)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filename, 'wb') as f:
        with tqdm(total=expected_size, unit='B', unit_scale=True, unit_divisor=1024, desc=desc, silent=silent) as pbar:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
                pbar.update(len(chunk))

    actual_size = os.path.getsize(filename)
    if expected_size is not None and actual_size != expected_size:
        os.remove(filename)
        raise requests.exceptions.HTTPError(f"Downloaded file is not of expected size, "
                                            f"{expected_size} expected but {actual_size} found.")

    return filename
