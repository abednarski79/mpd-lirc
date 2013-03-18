'''
Created on 8 Oct 2011

@author: abednarski
'''

from main.controller.volume.MixerFacade import MixerFacade
from main.controller.volume.VolumeController import VolumeController
import mox
import unittest

class VolumeControllerTest(unittest.TestCase):
    
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        self.mixerMocker = mox.Mox()        
    
    def testInitialization(self):
        volume = 100
        mixer = self.mixerMocker.CreateMock(MixerFacade)  
        # record mode                      
        mixer.setVolume(volume)
        # mixer.getVolume()
        self.mixerMocker.ReplayAll()
        # code to be tested
        volumeController = VolumeController(volume, mixer)
        # check
        self.mixerMocker.VerifyAll()
        # self.assertEquals(volume, volumeController.getVolume())
       
    def testVolumeUp(self):
        volume = 50
        step = 10
        mixer = self.mixerMocker.CreateMock(MixerFacade)                        
        mixer.setVolume(volume)
        mixer.getVolume().AndReturn(volume)
        mixer.setVolume(volume + step)
        self.mixerMocker.ReplayAll()
        volumeController = VolumeController(volume, mixer)
        volumeController.volumeUp(step)
        self.mixerMocker.VerifyAll() 
        
    def testVolumeDown(self):
        volume = 50
        step = -10
        mixer = self.mixerMocker.CreateMock(MixerFacade)                        
        mixer.setVolume(volume)
        mixer.getVolume().AndReturn(volume)
        mixer.setVolume(volume + step)
        self.mixerMocker.ReplayAll()
        volumeController = VolumeController(volume, mixer)
        volumeController.volumeDown(step)
        self.mixerMocker.VerifyAll()
    
    # def testMute(self):
         
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