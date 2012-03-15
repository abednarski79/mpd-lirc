'''
Created on 11 Mar 2012

@author: abednarski
'''
from controller.Configuration import Configuration, Button, Action
from controller.Processor import Processor
import time
import unittest



class ProcessorTest(unittest.TestCase):
        
    def setUp(self):
        print "Setup processor"
        gapDuration = 2
        # button - PLUS
        plusAction = Action("plus-action", isCancelable = False)
        self.plusButton = Button("PLUS-BUTTON", plusAction, plusAction, plusAction)                
        # button - MENU
        globalModeAction = Action("global-menu", fireDelay = gapDuration)
        currentMenuAction = Action ("current-menu-action", minimalRepeatTrigger = 1)
        self.menuButton = Button("PLUS-BUTTON", globalModeAction, globalModeAction, currentMenuAction)
        # button - FORWARD
        nextSongAction = Action("next-song-action", fireDelay = gapDuration)
        nextAlbumAction = Action("next-album-action", fireDelay = gapDuration)
        nextPlaylistAction = Action("next-playlist-action", minimalRepeatTrigger = 1)
        self.forwardButton = Button("FORWARD-BUTTON", nextSongAction, nextAlbumAction, nextPlaylistAction)
        # button - PLAY
        playPauseAction = Action("play-pause-action", fireDelay = gapDuration)
        powerOffAction = Action("power-off", minimalRepeatTrigger = 5)
        self.playButton = Button("PLAY-BUTTON", playPauseAction , playPauseAction, powerOffAction)
        # configuration
        buttons = (self.plusButton, self.menuButton, self.forwardButton, self.playButton)        
        self.configuration = Configuration(gapDuration, buttons)
        # processor        
        self.processor = Processor(self.configuration)

    def tearDown(self):
        self.processor= None                

    def clickButton(self, command, repeat):
        self.processor.preProcess(command, repeat)
        time.sleep(self.configuration.gapDuration)
        
    def testPlusButton(self):
        self.clickButton(self.plusButton, 0)        
        self.clickButton(self.plusButton, 0)
        self.assertEqual(len(self.processor.executionQueue), 2, 
                         "Expected number of command should be 2 but is: %s" %(len(self.processor.executionQueue)));
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1ClickCommand']
    unittest.main()