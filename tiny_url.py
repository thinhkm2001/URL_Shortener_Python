import contextlib
import sys

from urllib.parse import urlencode
from urllib.request import urlopen
 
def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    response = urlopen(request_url)
    contextlib.closing(response)
    return response.read().decode('utf-8')

if __name__ == '__main__':
    url = input('Enter the link to shorten')
    make_tiny(url)
