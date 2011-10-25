'''
Created on 20 Oct 2011

@author: abednarski
'''
# IMPORTS
import sys

from mpd import (MPDClient)
from socket import error as SocketError

HOST = 'localhost' 
PORT = '6600'

class ConnectionManager():    
    """Intialization of mpd client"""
    
    def __init__(self, host=HOST, port=PORT):
            self.__host = host
            self.port = port
            self.connection_id = {'host':host, 'port':port}
                 
    def connect__(self, client, connection_id):
        """
        Simple wrapper to connect MPD.
        """
        try:
            client.connect(**self.connection_id)
        except SocketError:
            return False
        return True
    
    def getConnection(self):
        ## MPD object instance
        client = MPDClient()
        if self.connect__(client, self.connection_id):
            print 'Got connected!'
            return client
        else:
            print 'fail to connect MPD server.'
            sys.exit(1)