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
        gapDuration = 0.5
        # button - PLUS
        plusAction = Action("plus-action", isCancelable = False)
        self.plusButton = Button("PLUS-BUTTON", plusAction, plusAction, plusAction)                
        # button - MENU
        globalModeAction = Action("global-menu", fireDelay = gapDuration)
        currentMenuAction = Action ("current-menu-action", minimalRepeatTrigger = 1)
        self.menuButton = Button("MENU-BUTTON", globalModeAction, globalModeAction, currentMenuAction)
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
        print "Sleeping before finishing the click ...",
        time.sleep(self.configuration.gapDuration)
        print "Done"
            
    def testPlusButtonClick(self):
        currentActionList = []
        self.clickButton(self.plusButton, 0)
        currentActionList.append(self.plusButton.click.action)
        self.assertEqual(self.processor.executionQueue, currentActionList);
                             
    def testPlusButtonDoubleClick(self):
        currentActionList = []
        self.clickButton(self.plusButton, 0)
        currentActionList.append(self.plusButton.click.action)
        self.clickButton(self.plusButton, 0)
        currentActionList.append(self.plusButton.doubleClick.action)
        self.assertEqual(self.processor.executionQueue, currentActionList);        
    
    def testPlusButtonLongClick(self):
        currentActionList = []
        self.clickButton(self.plusButton, 0)
        currentActionList.append(self.plusButton.click.action)
        self.clickButton(self.plusButton, 1)
        currentActionList.append(self.plusButton.hold.action)
        self.clickButton(self.plusButton, 2)
        currentActionList.append(self.plusButton.hold.action)
        self.assertEqual(self.processor.executionQueue, currentActionList);  
            
    def testForwardButtonClick(self):
        currentActionList = []
        self.clickButton(self.forwardButton, 0)
        currentActionList.append(self.forwardButton.click.action)
        self.assertEqual(self.processor.executionQueue, currentActionList);
    
    def testForwardButtonDoubleClick(self):
        currentActionList = []
        self.clickButton(self.forwardButton, 0)        
        self.clickButton(self.forwardButton, 0)
        currentActionList.append(self.forwardButton.doubleClick.action)        
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only next album action");

    def testForwardButtonLongClick(self):
        currentActionList = []
        self.clickButton(self.forwardButton, 0)        
        self.clickButton(self.forwardButton, 1)
        currentActionList.append(self.forwardButton.hold.action)        
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only next playlist action");
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1ClickCommand']
    unittest.main()