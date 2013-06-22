'''
Created on 19 Jun 2013

@author: abednarski
'''
from urlparse import urlparse
from urlparse import parse_qs
import sys

def main(inputUrl):
    print "Processing URL: %s" % inputUrl
    parsedUrl = urlparse(inputUrl)    
    urlQuery = parse_qs(parsedUrl.query)
    print "Found URL query: $s" % urlQuery
    queryPlaylist = urlQuery['playlist']
    print "Found URL playlist query: $s" % queryPlaylist
    paylistNumber = queryPlaylist[0]
    print "Found URL playlist number: $s" % paylistNumber
    return paylistNumber;
    
if __name__ == '__main__':
    playlistNumber = main(sys.argv[1])
    print playlistNumber 
    