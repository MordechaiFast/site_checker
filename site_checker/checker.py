from http.client import HTTPConnection
from urllib.parse import urlparse

def site_online(url, timeout=2) -> bool:
    """Returns True if the target url is online.
    
    If the target is not online, the request's error is passed along.
    """
    parser = urlparse(url)
    host = parser.netloc or parser.path.split('/')[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request('HEAD', '/')
            return True
        except Exception as err:
            error = err
        finally:
            connection.close()
    raise error
