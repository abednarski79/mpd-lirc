'''
Created on 19 Jun 2013

@author: abednarski
'''
from urlparse import urlparse
from urlparse import parse_qs

if __name__ == '__main__':
    o = urlparse('http://wroclaw.radio.pionier.net.pl:8000/pl/tuba10-1.mp3?playlist=1&test=2')
    print parse_qs(o.query)
