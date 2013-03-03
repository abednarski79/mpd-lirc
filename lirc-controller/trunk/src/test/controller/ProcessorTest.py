'''
Created on 11 Mar 2012

@author: abednarski
'''
from main.controller.Configuration import Configuration, Button, Action
from main.controller.Processor import Processor
import time
import unittest


class ProcessorTest(unittest.TestCase):
    
    actionDelayFactor = 1.1
    testDelayFactor = 1.2

    def setUp(self):
        print "Setup processor"
        gapDuration = 1
        # button - PLUS
        # all types of usage should results in this same action
        plusAction = Action("plus-action", isCancelable = False)
        self.plusButton = Button("PLUS-BUTTON", plusAction, plusAction, plusAction)        
        # button - FORWARD
        # when clicked once then next song should be played, when double-clicked then next album should be played 
        # and when hold then next play-list should be played 
        nextSongAction = Action("next-song-action", fireDelay = (gapDuration * self.actionDelayFactor))
        nextAlbumAction = Action("next-album-action", fireDelay = (gapDuration * self.actionDelayFactor))
        nextPlaylistAction = Action("next-playlist-action", minimalRepeatTrigger = 1)
        self.forwardButton = Button("FORWARD-BUTTON", nextSongAction, nextAlbumAction, nextPlaylistAction)      
        # button - MENU
        # when clicked once then general mode menu action should be executed, when hold current mode menu action should be executed
        globalModeAction = Action("global-menu-action", fireDelay = (gapDuration * self.actionDelayFactor))
        currentMenuAction = Action ("current-menu-action", minimalRepeatTrigger = 1)
        self.menuButton = Button("MENU-BUTTON", globalModeAction, globalModeAction, currentMenuAction)
        # button - PLAY
        # when clicked once then play/pause action should be executed, when hold for at least 5 rounds power off action should be executed
        playPauseAction = Action("play-pause-action", fireDelay = (gapDuration * self.actionDelayFactor))
        powerOffAction = Action("power-off", minimalRepeatTrigger = 5)
        self.playButton = Button("PLAY-BUTTON", playPauseAction , playPauseAction, powerOffAction)
        # configuration
        buttons = (self.plusButton, self.menuButton, self.forwardButton, self.playButton)        
        self.configuration = Configuration(gapDuration, buttons)
        # processor        
        self.processor = Processor(self.configuration)


    def tearDown(self):
        self.processor= None
        self.configuration = None

    def clickButton(self, button, repeat):
        ''' Simulates button click on the remote '''
        self.processor.preProcess(button.key, repeat)
        print "Sleeping for %s before finishing current click ..." % (self.configuration.gapDuration)
        time.sleep(self.configuration.gapDuration)
        print "Done"
    
    def sleelBeforeTest(self):
        time.sleep(self.configuration.gapDuration * self.testDelayFactor)
                
    def testPlusButtonClick(self):
        currentActionList = []
        self.clickButton(self.plusButton, 0)
        currentActionList.append(self.plusButton.click.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList);
                             
    def XtestPlusButtonDoubleClick(self):
        currentActionList = []
        self.clickButton(self.plusButton, 0)
        currentActionList.append(self.plusButton.click.action)
        self.clickButton(self.plusButton, 0)
        currentActionList.append(self.plusButton.doubleClick.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList);        
    
    def XtestPlusButtonHold(self):
        currentActionList = []
        self.clickButton(self.plusButton, 0)
        currentActionList.append(self.plusButton.click.action)
        self.clickButton(self.plusButton, 1)
        currentActionList.append(self.plusButton.hold.action)
        self.clickButton(self.plusButton, 2)
        currentActionList.append(self.plusButton.hold.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList);  
            
    def XtestForwardButtonClick(self):
        currentActionList = []
        self.clickButton(self.forwardButton, 0)
        currentActionList.append(self.forwardButton.click.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList);
    
    def XtestForwardButtonDoubleClick(self):
        '''
        Forward button was double-clicked.
        It is only expected that double-click action will be executed and the single-click action should be ignored.
        '''
        currentActionList = []
        self.clickButton(self.forwardButton, 0)        
        self.clickButton(self.forwardButton, 0)
        currentActionList.append(self.forwardButton.doubleClick.action)
        self.sleelBeforeTest()        
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only next album action");

    def XtestForwardButtonHold(self):
        currentActionList = []
        self.clickButton(self.forwardButton, 0)        
        self.clickButton(self.forwardButton, 1)
        currentActionList.append(self.forwardButton.hold.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only next playlist action");

    def XtestMenuButtonClick(self):
        currentActionList = []
        self.clickButton(self.menuButton, 0)
        currentActionList.append(self.menuButton.click.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x global menu action");
    
    def XtestMenuDoubleButtonClick(self):
        currentActionList = []
        self.clickButton(self.menuButton, 0)
        self.clickButton(self.menuButton, 0)
        currentActionList.append(self.menuButton.doubleClick.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x global menu action");
        
    def XtestMenuHold(self):
        currentActionList = []
        self.clickButton(self.menuButton, 0)
        self.clickButton(self.menuButton, 1)
        currentActionList.append(self.menuButton.hold.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x current menu action");
        
    def XtestPlayButtonClick(self):
        currentActionList = []
        self.clickButton(self.playButton, 0)
        currentActionList.append(self.playButton.click.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x play-pause action");
    
    def XtestPlayButtonDoubleClick(self):
        currentActionList = []
        self.clickButton(self.playButton, 0)
        self.clickButton(self.playButton, 0)
        currentActionList.append(self.playButton.click.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x play-pause action");
        
    def XtestPlayButtonHoldx1(self):
        '''
        Play button was hold for 2 rounds.
        Expected no action to be executed as minimal repeats trigger of 5 was not satisfied.
        '''
        currentActionList = []
        self.clickButton(self.playButton, 0)
        self.clickButton(self.playButton, 1)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should be empty");
    
    def XtestPlayButtonHoldx5(self):
        '''
        Play button was hold for 6 rounds.
        Expected hold action to be executed as minimal repeats trigger is 5 was satisfied.
        '''
        currentActionList = []
        self.clickButton(self.playButton, 0)
        self.clickButton(self.playButton, 1)
        self.clickButton(self.playButton, 2)
        self.clickButton(self.playButton, 3)
        self.clickButton(self.playButton, 4)
        self.clickButton(self.playButton, 5)
        currentActionList.append(self.playButton.hold.action)
        self.sleelBeforeTest()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x power-off action");
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1ClickCommand']
    unittest.main()