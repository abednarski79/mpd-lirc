'''
Created on 11 Mar 2012

@author: abednarski
'''
from threading import Timer

class Processor():
    '''
    classdocs
    '''
    
    def __init__(self, configuration):
        self.currentButton = None
        self.currentAction = None
        self.lastButton = None
        self.lastAction = None
        self.timer = None
        self.isFirstTimeRun = True
        self.isTimerRunning = False
        self.configurationMap = {}        
        for button in configuration.buttons:
            self.configurationMap[button.key] = button
        self.executionQueue = []
    
    def addToQueue(self, action):
        print "Adding action %s to execution queue" % (action)
        self.executionQueue.append(action)        
        self.isTimerRunning = False
        
    def preProcess(self, key, repeat):
        currentButton = self.configurationMap[key]
        print "preProcess: Current button %s, repeat %s" % (currentButton, repeat)
        if(self.isFirstTimeRun == True):
            self.currentAction = currentButton.click 
            print "preProcess: Creating timer, delay: %s, arguments: %s" % (self.currentAction.fireDelay, self.currentAction.action)     
            self.timer = Timer(self.currentAction.fireDelay, self.addToQueue, [self.currentAction.action])
            self.timer.start()                        
            self.isFirstTimeRun = False
        self.lastButton = currentButton
        
                        