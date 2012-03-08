'''
Created on 8 Oct 2011

@author: abednarski
'''

from controller.volume.Mixer import Mixer
from controller.volume.VolumeController import VolumeController
import mox
import unittest

class VolumeControllerTest(unittest.TestCase):
    
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        self.mixerMocker = mox.Mox()        
    
    def testInitialization(self):
        mixer = self.mixerMocker.CreateMock(Mixer)
        volume = 100
        # mixer.getVolume()
        self.mixerMocker.ReplayAll()
        self.mixerMocker.VerifyAll()
        
#    
#    def testNextSongWhenCurrentIsLast(self):
#        self.getCurrentSong=self.playlist_1[14]
#        client = MockClient(self.getCurrentSong, self.playlist_1)
#        playlistManager = PlaylistManager(client);
#        command = PlayNextSongCommand(playlistManager)
#        self.assertRaises(PlaylistManagerException, command.execute)
#    
#    def testPreviousSongWhenCurrentIsNotFirst(self):
#        self.getCurrentSong=self.playlist_1[8]
#        client = MockClient(self.getCurrentSong, self.playlist_1)
#        playlistManager = PlaylistManager(client);
#        command = PlayPreviousSongCommand(playlistManager)
#        command.execute()        
#        self.assertEqual(client.getCurrentSong()['pos'], str(7));
#    
#    def testPreviousSongWhenCurrentIsFirst(self):
#        self.getCurrentSong=self.playlist_1[0]
#        client = MockClient(self.getCurrentSong, self.playlist_1)
#        playlistManager = PlaylistManager(client);
#        command = PlayPreviousSongCommand(playlistManager)        
#        self.assertRaises(PlaylistManagerException, command.execute)
#        
#    def testNextAlbumWhenCurrentIsNotLast(self):
#        self.getCurrentSong=self.playlist_1[6]
#        client = MockClient(self.getCurrentSong, self.playlist_1)
#        playlistManager = PlaylistManager(client);
#        command = PlayNextAlbumCommand(playlistManager)
#        command.execute()        
#        self.assertEqual(client.getCurrentSong()['pos'], str(9));
#
#    def testNextAlbumWhenCurrentIsLast_1(self):
#        self.getCurrentSong=self.playlist_1[14]
#        client = MockClient(self.getCurrentSong, self.playlist_1)
#        playlistManager = PlaylistManager(client);
#        command = PlayNextAlbumCommand(playlistManager)        
#        self.assertRaises(PlaylistManagerException, command.execute)
#      
#    def testNextAlbumWhenCurrentIsLast_2_1(self):
#        self.getCurrentSong=self.playlist_2[9]
#        client = MockClient(self.getCurrentSong, self.playlist_2)
#        playlistManager = PlaylistManager(client);
#        command = PlayNextAlbumCommand(playlistManager)
#        command.execute()        
#        self.assertEqual(client.getCurrentSong()['pos'], str(12));
#  
#    def testNextAlbumWhenCurrentIsLast_2_2(self):
#        self.getCurrentSong=self.playlist_2[13]
#        client = MockClient(self.getCurrentSong, self.playlist_2)
#        playlistManager = PlaylistManager(client);
#        command = PlayNextAlbumCommand(playlistManager)        
#        self.assertRaises(PlaylistManagerException, command.execute)
#                
#    def testPreviousAlbumWhenCurrentIsNotFirst_1(self):
#        self.getCurrentSong=self.playlist_1[8]
#        client = MockClient(self.getCurrentSong, self.playlist_1)
#        playlistManager = PlaylistManager(client);
#        command = PlayPreviousAlbumCommand(playlistManager)
#        command.execute()        
#        self.assertEqual(client.getCurrentSong()['pos'], str(3));
#        
#    def testPreviousAlbumWhenCurrentIsNotFirst_2(self):
#        self.getCurrentSong=self.playlist_2[13]
#        client = MockClient(self.getCurrentSong, self.playlist_2)
#        playlistManager = PlaylistManager(client);
#        command = PlayPreviousAlbumCommand(playlistManager)
#        command.execute()        
#        self.assertEqual(client.getCurrentSong()['pos'], str(9));
#        
#    def testPreviousAlbumWhenCurrentIsFirst(self):
#        self.getCurrentSong=self.playlist_1[2]
#        client = MockClient(self.getCurrentSong, self.playlist_1)
#        playlistManager = PlaylistManager(client);
#        command = PlayPreviousAlbumCommand(playlistManager)        
#        self.assertRaises(PlaylistManagerException, command.execute);
