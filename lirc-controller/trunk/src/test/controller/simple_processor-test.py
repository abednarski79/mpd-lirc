'''
Created on 11 Mar 2012

@author: abednarski
'''
from main.controller.configuration import Configuration, Button, Action
from main.controller.simple_processor import Processor, Event
import time
import unittest
from multiprocessing import Queue

class ProcessorTest(unittest.TestCase):
    
    __test__ = True
    
    actionDelayFactor = 1.1
    testDelayFactor = 1.2    
    
    def setUp(self):
        print "Setup processor"
        self.gapDuration = 1
        blocking = False
        # button - PLUS
        # all types of usage should results in this same task
        plusAction = Action("plus-id", "plus-task", isCancelable = False)
        self.plusButton = Button("PLUS-BUTTON", plusAction, plusAction, plusAction)        
        # button - FORWARD
        # when clicked once then next song should be played, when double-clicked then next album should be played 
        # and when hold then next play-list should be played 
        nextSongAction = Action("next-song-id", "next-song-task", fireDelay = (self.gapDuration * self.actionDelayFactor))
        nextAlbumAction = Action("next-album-id", "next-album-task", fireDelay = (self.gapDuration * self.actionDelayFactor))
        nextPlaylistAction = Action("next-playlist-id", "next-playlist-task", minimalRepeatTrigger = 1)
        self.forwardButton = Button("FORWARD-BUTTON", nextSongAction, nextAlbumAction, nextPlaylistAction)      
        # button - MENU
        # when clicked once then general mode menu task should be executed, when hold current mode menu task should be executed
        globalModeAction = Action("global-menu-id", "global-menu-task", fireDelay = (self.gapDuration * self.actionDelayFactor))
        currentMenuAction = Action ("current-menu-id", "current-menu-task", minimalRepeatTrigger = 1)
        self.menuButton = Button("MENU-BUTTON", globalModeAction, globalModeAction, currentMenuAction)
        # button - PLAY
        # when clicked once then play/pause task should be executed, when hold for at least 5 rounds power off task should be executed
        playPauseAction = Action("play-pause-id", "play-pause-task", fireDelay = (self.gapDuration * self.actionDelayFactor))
        powerOffAction = Action("power-off-id", "power-off-task", minimalRepeatTrigger = 5)
        self.playButton = Button("PLAY-BUTTON", playPauseAction , playPauseAction, powerOffAction)
        # configuration
        buttons = {}
        buttons[self.plusButton.id] = self.plusButton
        buttons[self.forwardButton.id] = self.forwardButton
        buttons[self.menuButton.id] = self.menuButton
        buttons[self.playButton.id] = self.playButton  
        self.processorQueue = Queue()
        self.actualWorkerQueue = Queue()
        self.expectedWorkerQueue = Queue()
        # processor        
        self.processor = Processor(buttons, self.processorQueue, self.actualWorkerQueue)

    def validateQueuesEqual(self,queue1, queue2):
        list1 = []
        list2 = []
        while not queue1.empty():
            element = queue1.get_nowait()
            list1.append(element)                
        while not queue2.empty():
            element = queue2.get_nowait()
            list2.append(element)
        list1.sort()
        list2.sort()
        self.assertEqual(list1, list2)
    
    def tearDown(self):
        self.processor= None
        self.configuration = None

    def clickButton(self, button, repeat):
        ''' Simulates button click on the remote '''
        self.processorQueue.put(Event(button.id, repeat))
        print "Sleeping for %s before finishing current click ..." % (self.gapDuration)
        time.sleep(self.gapDuration)
        print "Done"
    
    def sendTerminationSignal(self):
        self.processorQueue.put(None)
    
    def sleepBeforeCheck(self):
        time.sleep(self.gapDuration * self.testDelayFactor)
                
    def XtestPlusButtonClick(self):        
        self.clickButton(self.plusButton, 0)
        self.sendTerminationSignal()
        self.expectedWorkerQueue.put(self.plusButton.click.task)
        self.expectedWorkerQueue.put(None)        
        self.processor.process()
        self.validateQueuesEqual(self.actualWorkerQueue, self.expectedWorkerQueue);
                             
    def XtestPlusButtonDoubleClick(self):        
        self.clickButton(self.plusButton, 0)
        self.expectedWorkerQueue.put(self.plusButton.click.task)
        self.clickButton(self.plusButton, 0)
        self.expectedWorkerQueue.put(self.plusButton.click.task)
        self.expectedWorkerQueue.put(None)
        self.sendTerminationSignal()        
        self.processor.process()
        self.sleepBeforeCheck()
        self.validateQueuesEqual(self.actualWorkerQueue, self.expectedWorkerQueue);        
    
    def XtestPlusButtonHold(self):
        self.clickButton(self.plusButton, 0)
        self.expectedWorkerQueue.put(self.plusButton.click.task)
        self.clickButton(self.plusButton, 1)
        self.expectedWorkerQueue.put(self.plusButton.click.task)
        self.clickButton(self.plusButton, 2)
        self.expectedWorkerQueue.put(self.plusButton.click.task)
        self.expectedWorkerQueue.put(None)
        self.sendTerminationSignal()        
        self.processor.process()
        self.sleepBeforeCheck()
        self.validateQueuesEqual(self.actualWorkerQueue, self.expectedWorkerQueue); 
            
    def testForwardButtonClick(self):
        self.clickButton(self.forwardButton, 0)
        self.sendTerminationSignal()
        self.expectedWorkerQueue.put(self.forwardButton.click.task)
        self.expectedWorkerQueue.put(None)        
        self.processor.process()
        #self.sleepBeforeCheck()
        self.validateQueuesEqual(self.actualWorkerQueue, self.expectedWorkerQueue);        
        
    
    def XtestForwardButtonDoubleClick(self):
        '''
        Forward button was double-clicked.
        It is only expected that double-click task will be executed and the single-click task should be ignored.
        '''
        currentActionList = []
        self.clickButton(self.forwardButton, 0)        
        self.clickButton(self.forwardButton, 0)
        currentActionList.append(self.forwardButton.doubleClick.task)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only next album task");

    def XtestForwardButtonHold(self):
        currentActionList = []
        self.clickButton(self.forwardButton, 0)        
        self.clickButton(self.forwardButton, 1)
        currentActionList.append(self.forwardButton.hold.task)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only next playlist task");

    def XtestMenuButtonClick(self):
        currentActionList = []
        self.clickButton(self.menuButton, 0)
        currentActionList.append(self.menuButton.click.task)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x global menu task");
    
    def XtestMenuDoubleButtonClick(self):
        currentActionList = []
        self.clickButton(self.menuButton, 0)
        self.clickButton(self.menuButton, 0)
        currentActionList.append(self.menuButton.doubleClick.task)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x global menu task");
        
    def XtestMenuHold(self):
        currentActionList = []
        self.clickButton(self.menuButton, 0)
        self.clickButton(self.menuButton, 1)
        currentActionList.append(self.menuButton.hold.task)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x current menu task");
        
    def XtestPlayButtonClick(self):
        currentActionList = []
        self.clickButton(self.playButton, 0)
        currentActionList.append(self.playButton.click.task)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x play-pause task");
    
    def XtestPlayButtonDoubleClick(self):
        currentActionList = []
        self.clickButton(self.playButton, 0)
        self.clickButton(self.playButton, 0)
        currentActionList.append(self.playButton.click.task)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x play-pause task");
        
    def XtestPlayButtonHoldx1(self):
        '''
        Play button was hold for 2 rounds.
        Expected no task to be executed as minimal repeats trigger of 5 was not satisfied.
        '''
        currentActionList = []
        self.clickButton(self.playButton, 0)
        self.clickButton(self.playButton, 1)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should be empty");
    
    def XtestPlayButtonHoldx5(self):
        '''
        Play button was hold for 6 rounds.
        Expected hold task to be executed as minimal repeats trigger is 5 was satisfied.
        '''
        currentActionList = []
        self.clickButton(self.playButton, 0)
        self.clickButton(self.playButton, 1)
        self.clickButton(self.playButton, 2)
        self.clickButton(self.playButton, 3)
        self.clickButton(self.playButton, 4)
        self.clickButton(self.playButton, 5)
        currentActionList.append(self.playButton.hold.task)
        self.sleepBeforeCheck()
        self.assertEqual(self.processor.executionQueue, currentActionList, "Should contain only 1x power-off task");
        
if __name__ == "__main__":
    unittest.main()
