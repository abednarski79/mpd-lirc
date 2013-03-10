'''
Created on 11 Mar 2012

@author: abednarski
'''
from threading import Timer

class ProcessorTest():
    '''
    Processor
    '''  
    
    def __init__(self):
        self.fireDelay = 0.22
        self.currentButton = None
        self.timer = None
        self.isTimerRunning = False        
        
    def processEvent(self, key, repeat):
        ''' 
        Process single event and executes selected task, where:
        key - name of the key to be processed
        repeat - repeat index number 
        '''
        print "processEvent: Current button %s, repeat %s" % (key, repeat)
        if(repeat == 0):
            if(self.isTimerRunning == False):
                print "processEvent: Timer is not running, processing 'click' task"
                currentAction = "click"
            else:
                print "processEvent: Timer is running, processing 'double click' task"
                self.cancelTimer()          
                currentAction = "doubleClick"
        else:
            print "processEvent: Button is repeated, processing 'hold' task"
            if(self.isTimerRunning):
                self.cancelTimer()
            currentAction = "hold"
        self.executeTask(currentAction, repeat)
    
    def executeTask(self, action, repeat):
        if(action == "hold"):
            self.addToExecutionQueue(action)
        else:            
            self.startTimer(self.fireDelay, self.addToExecutionQueue, [action])

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
        self.isTimerRunning = False
                