'''
Created on 11 Mar 2012

@author: abednarski
'''
from threading import Timer

class Processor():
    '''
    Processor
    '''
    
    def __init__(self, configuration):
        self.currentButton = None
        self.lastButton = None
        self.timer = None
        self.isTimerRunning = False
        self.configurationMap = {}        
        for button in configuration.buttons:
            self.configurationMap[button.key] = button
        self.executionQueue = []
    
    def addToQueue(self, action):
        print "addToQueue: Adding action %s to execution queue" % (action)
        self.executionQueue.append(action)        
        self.isTimerRunning = False

    def preProcess(self, key, repeat):
        currentButton = self.configurationMap[key]
        if(currentButton == None):
            print "preProcess: Button with key %s not present in configuration." % (key)
            return
        print "preProcess: Current button %s, repeat %s" % (currentButton, repeat)
        if(repeat == 0):
            if(self.isTimerRunning == False):
                print "preProcess: Timer is not running, processing 'click' action"
                currentAction = currentButton.click
            else:
                print "preProcess: Timer is running, processing 'double click' action"
                self.cancelTimer()          
                currentAction = currentButton.doubleClick
            self.processAction(currentAction, repeat)
        else:
            print "preProcess: Timer is running, button is repeated, processing 'hold' action"
            if(self.isTimerRunning):
                self.timer.cancel()
                self.isTimerRunning = False
            self.processAction(currentButton.hold, repeat)
            return
        self.lastButton = currentButton
    
    def processAction(self, action, repeat):
        if(repeat < action.minimalRepeatTrigger):
            print "processAction: Ignoring action, delay: %s, name: %s, min. repeat trigger: %s" % (action.fireDelay, action.action, action.minimalRepeatTrigger)
            return
        print "processAction: Processing action, delay: %s, name: %s, min. repeat trigger: %s" % (action.fireDelay, action.action, action.minimalRepeatTrigger)
        if(action.fireDelay == 0):           
            self.addToQueue(action.action)
        else:
            self.timer = Timer(action.fireDelay, self.addToQueue, [action.action])
            self.timer.start()
            self.isTimerRunning = True

    def cancelTimer(self):
        print "cancelTimer: Cancelling the timer"
        self.timer.cancel()
        self.isTimerRunning = False