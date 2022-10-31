import http.client
import sys
from urllib.parse import urlparse


def expand_short_url(url):
    parsed_url = urlparse(url)
    h = http.client.HTTPSConnection(parsed_url.netloc)
    resource = parsed_url.path
    if parsed_url.query != "":
        resource += "?" + parsed_url.query
    h.request('HEAD', resource, headers={'User-Agent': 'curl/7.38.0'})
    response = h.getresponse()
    if response.status // 100 == 3 and response.getheader('Location'):
        return expand_short_url(response.getheader('Location'))
    else:
        return url


if __name__ == '__main__':
    expanded_url = expand_short_url(sys.argv[1])
    print(expanded_url)
