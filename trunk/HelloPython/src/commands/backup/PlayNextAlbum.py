'''
Created on 1 Oct 2011

@author: abednarski
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORTS
import sys
import pprint
import string
from types import *
import cPickle

from mpd import (MPDClient, CommandError)
from socket import error as SocketError

HOST = 'localhost' 
PORT = '6600' 
PASSWORD = False
##
CON_ID = {'host':HOST, 'port':PORT}
##  

def mpdConnect(client, con_id):
    """
    Simple wrapper to connect MPD.
    """
    try:
        client.connect(**con_id)
    except SocketError:
        return False
    return True

def main():
    ## MPD object instance
    client = MPDClient()
    if mpdConnect(client, CON_ID):
        print 'Got connected!'
    else:
        print 'fail to connect MPD server.'
        sys.exit(1)
        
    ## Fancy output
    pp = pprint.PrettyPrinter(indent=4)    
    currentsong = client.currentsong()
    print '\nCurrent song file path:'
    pp.pprint(currentsong)
    ##songfile = currentsong['file']
    ##pp.pprint(string.split(songfile, '/'))
    print '\nCurrent playlist:'
    pp.pprint(client.playlistinfo())
    file_currentsong = open("/tmp/currentsong", 'w')
    file_playlist = open("/tmp/playlist", 'w')
    cPickle.dump(client.playlistinfo(), file_playlist);
    cPickle.dump(currentsong, file_currentsong);
    
    
# Script starts here
if __name__ == "__main__":
    main()