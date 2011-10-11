'''
Created on 8 Oct 2011

@author: abednarski
'''

import unittest
import cPickle
import os
import managers.playlist_manager
#from managers import PlaylistManager

class PlaylistManagerTest(unittest.TestCase):
    
    def setUp(self):
        # load play list and current song information
        pathCurrentSongDump = os.path.join(os.getcwd(), 'dump', 'current_song.dump')
        pathPlaylistDump = os.path.join(os.getcwd(), 'dump', 'playlist.dump')
        fileCurrentSongDump = open (pathCurrentSongDump, "r")
        filePlaylistDump = open (pathPlaylistDump, "r")
        self.currentSong = cPickle.load(fileCurrentSongDump)
        self.playlist = cPickle.load(filePlaylistDump)
        self.playlistManager = managers.playlist_manager.PlaylistManager()
        self.playlistManager.playNextSong()
        self.first = '1'
        self.second = '2'
        self.msg = 'Heuston we have a problem !'
        
    def testNextSongWhenCurrentIsNotLast(self):        
        self.assertEqual(self.first, self.second, self.msg);
    
    def testNextSongWhenCurrentIsLast(self):
        self.assertEqual(self.first, self.second, self.msg);
    
    def testPreviousSongWhenCurrentIsNotFirst(self):
        self.assertEqual(self.first, self.second, self.msg);
    
    def testPreviousSongWhenCurrentIsFirst(self):
        self.assertEqual(self.first, self.second, self.msg);
        
    def testNextAlbumWhenCurrentIsNotLast(self):
        self.assertEqual(self.first, self.second, self.msg);

    def testPreviousAlbumWhenCurrentIsNotFirst(self):
        self.assertEqual(self.first, self.second, self.msg);
        
    def testNextAlbumWhenCurrentIsLast(self):
        self.assertEqual(self.first, self.second, self.msg);
        
    def testPreviousAlbumWhenCurrentIsFirst(self):
        print(self.currentSong)
        # self.assertEqual(self.first, self.second, self.msg);
            