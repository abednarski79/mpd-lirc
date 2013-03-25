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
        self.timer = None
        self.isTimerRunning = False
        self.configurationMap = {}        
        for button in configuration.buttons:
            self.configurationMap[button.id] = button
        self.executionQueue = []    

    def processEvent(self, key, repeat):
        ''' 
        Process single event and executes selected task, where:
        key - name of the key to be processed
        repeat - repeat index number 
        '''
        currentButton = self.configurationMap[key]
        if(currentButton == None):
            print "processEvent: Button with key %s not present in configuration." % (key)
            return
        print "processEvent: Current button %s, repeat %s" % (currentButton, repeat)
        if(repeat == 0):
            if(self.isTimerRunning == False):
                print "processEvent: Timer is not running, processing 'click' task"
                currentAction = currentButton.click
            else:
                print "processEvent: Timer is running, processing 'double click' task"
                self.cancelTimer()          
                currentAction = currentButton.doubleClick
        else:
            print "processEvent: Button is repeated, processing 'hold' task"
            if(self.isTimerRunning):
                self.cancelTimer()
            currentAction = currentButton.hold
        self.executeTask(currentAction, repeat)
    
    def executeTask(self, action, repeat):
        if(repeat < action.minimalRepeatTrigger):
            print "executeTask: Ignoring task, delay: %s, name: %s, min. repeat trigger: %s" % (action.fireDelay, action.task, action.minimalRepeatTrigger)
            return
        print "executeTask: Processing task, delay: %s, name: %s, min. repeat trigger: %s" % (action.fireDelay, action.task, action.minimalRepeatTrigger)
        if(action.fireDelay == 0):           
            self.addToExecutionQueue(action.task)
        else:
            self.startTimer(action.fireDelay, self.addToExecutionQueue, [action.task])

    def cancelTimer(self):
        print "cancelTimer: Cancelling the timer"        
        self.timer.cancel()
        self.isTimerRunning = False
        
    def startTimer(self, executionDelay, methodToExecute, parameters):
        print "startTimer: Starts the timer for executing a task"
        self.timer = Timer(executionDelay, methodToExecute, parameters)
        self.timer.start()        
        self.isTimerRunning = True
        
    def addToExecutionQueue(self, action):
        print "addToExecutionQueue: Adding task %s to execution queue" % (action)
        self.executionQueue.append(action)        
        self.isTimerRunning = False
                