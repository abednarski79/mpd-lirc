'''
Created on 11 Mar 2012

@author: abednarski
'''
from threading import Timer
import logging
from multiprocessing import Queue
import threading
from main.controller.configuration import Action, Configuration
import time

class Event():
    def __init__(self, key, repeat):
        self.key = key
        self.repeat = repeat

class Processor():
    '''
    Processor
    '''    
    
    def __init__(self, mapping, processorQueue, workerQueue):
        self.logger = logging.getLogger("controllerApp")        
        self.currentButton = None
        self.timer = None
        self.isTimerRunning = False
        self.mapping = mapping            
        self.processorQueue = processorQueue
        self.workerQueue = workerQueue
    
    def process(self):
        while True:
            event = self.processorQueue.get()
            if event is None:
                self.addToExecutionQueueNoWait(None)
                break          
            self.onEvent(event)
        self.logger.info("Processor - shutting down")
        
    def onEvent(self, event):
        ''' 
        Process single event and executes selected task, where:
        key - name of the key to be processed
        repeat - repeat index number 
        '''
        if(self.mapping.has_key(event.key)):
            currentButton = self.mapping[event.key]
        else:
            self.logger.error("onEvent: Button with key %s not present in configuration." % (event.key))
            return
        self.logger.debug("onEvent: Current button %s, repeat %s" % (currentButton, event.repeat))
        if(event.repeat == 0):
            if(self.isTimerRunning == False): 
                '''timer responsible for adding new tasks to execution queue is not running
                this means that this call will be treated as -click- action'''
                self.logger.debug("onEvent: Timer is not running, processing 'click' task")
                currentAction = currentButton.click
            else:
                '''timer responsible for adding new tasks to execution queue is currently running
                this means that this call will be treated as -double-click- action
                also timer needs to be cancelled (in other case -click- and -double-click- will be processed)'''
                self.logger.debug("onEvent: Timer is running, processing 'double click' task")
                self.cancelTimer()          
                currentAction = currentButton.doubleClick
        else:
            '''repeat index > 0 so this same button was hold, this call will be processed as -hold- action
            also in this case timer must be cancelled'''
            self.logger.debug("onEvent: Button is repeated, processing 'hold' task")
            if(self.isTimerRunning):
                self.cancelTimer()
            currentAction = currentButton.hold
        if(currentAction != None):
            self.addTaskToWorkerQueue(currentAction, event.repeat)
        else:
            self.logger.error("Action for repeat %s not configured for button: %s" % (event.repeat, event.key))
    
    def addTaskToWorkerQueue(self, action, repeat):
        if(repeat < action.minimalRepeatTrigger):
            self.logger.debug("executeTask: Ignoring task, delay: %s, name: %s, min. repeat trigger: %s" % (action.fireDelay, action.task, action.minimalRepeatTrigger))
            return
        self.logger.debug("executeTask: Processing task, delay: %s, name: %s, min. repeat trigger: %s" % (action.fireDelay, action.task, action.minimalRepeatTrigger))
        if(action.fireDelay == 0):           
            self.addToExecutionQueueNoWait(action.task)
        else:
            self.addToExecutionQueueWait(action.fireDelay, self.addToExecutionQueueNoWait, [action.task])            

    def cancelTimer(self):
        self.logger.debug("cancelTimer: Cancelling the timer")
        self.timer.cancel()
        self.isTimerRunning = False
    
    def addToExecutionQueueWait(self, executionDelay, methodToExecute, parameters):
        self.logger.debug("startTimer: Starts the timer for executing a task")
        self.timer = Timer(executionDelay, methodToExecute, parameters)
        self.timer.start()        
        self.isTimerRunning = True
        
    def addToExecutionQueueNoWait(self, action):
        self.logger.debug("addToExecutionQueueNoWait: Adding task %s to execution queue" % (action))
        self.workerQueue.put(action)        
        self.isTimerRunning = False
        