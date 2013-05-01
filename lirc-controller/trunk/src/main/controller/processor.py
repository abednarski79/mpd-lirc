'''
Created on 11 Mar 2012

@author: abednarski
'''
from threading import Timer
import logging
import Queue
import threading
from main.controller.configuration import Action, Configuration
import time

def worker():   
    print "hi3"   

class Processor():
    '''
    Processor
    '''    
    
    def __init__(self, configuration):
        self.logger = logging.getLogger("controllerApp")        
        self.currentButton = None
        self.timer = None
        self.isTimerRunning = False
        self.buttonsMap = configuration.buttons            
        self.executionQueue = []
        #self.startQueueRunner()
              
    '''def worker(self):
        fo = open("/tmp/foo.txt", "wb")
        fo.write("hi2-0\n")
        fo.flush()
        #self.logger.debug("starting the loop")            
        while True:          
            time.sleep(1)  
            fo.write("hi2-1\n")
            fo.flush()
            #self.logger.debug("running...")            
            action = self.executionQueue.get()
            time.sleep(1)
            fo.write("hi2-2\n")
            fo.flush()
            #action.task.executeCommand(action.task.parameter)
            self.executionQueue.task_done()
            time.sleep(1)
            fo.write("hi2-3\n")
            fo.flush()
            
    def startQueueRunner(self):
        print "hi8-1"
        runner = threading.Thread(target=self.worker)
        runner.daemon = True
        runner.start()
        print "hi8-2"
        self.logger.debug("runner started.")'''        
        
    def processEvent(self, key, repeat):
        ''' 
        Process single event and executes selected task, where:
        key - name of the key to be processed
        repeat - repeat index number 
        '''        
        if(self.buttonsMap.has_key(key)):
            currentButton = self.buttonsMap[key]
        else:
            self.logger.debug("processEvent: Button with key %s not present in configuration." % (key))
            return
        self.logger.debug("processEvent: Current button %s, repeat %s" % (currentButton, repeat))
        if(repeat == 0):
            if(self.isTimerRunning == False):
                self.logger.debug("processEvent: Timer is not running, processing 'click' task")
                currentAction = currentButton.click
            else:
                self.logger.debug("processEvent: Timer is running, processing 'double click' task")
                self.cancelTimer()          
                currentAction = currentButton.doubleClick
        else:
            self.logger.debug("processEvent: Button is repeated, processing 'hold' task")
            if(self.isTimerRunning):
                self.cancelTimer()
            currentAction = currentButton.hold
        if(currentAction != None):
            self.executeTask(currentAction, repeat)
        else:
            self.logger.debug("Action for repeat %s not configured for button: %s" % (repeat, key))
    
    def executeTask(self, action, repeat):
        if(repeat < action.minimalRepeatTrigger):
            self.logger.debug("executeTask: Ignoring task, delay: %s, name: %s, min. repeat trigger: %s" % (action.fireDelay, action.task, action.minimalRepeatTrigger))
            return
        self.logger.debug("executeTask: Processing task, delay: %s, name: %s, min. repeat trigger: %s" % (action.fireDelay, action.task, action.minimalRepeatTrigger))
        if(action.fireDelay == 0):           
            self.addNowToExecutionQueue(action.task)
        else:
            self.addWithDelayToExecutionQueue(action.fireDelay, self.addNowToExecutionQueue, [action.task])            

    def cancelTimer(self):
        self.logger.debug("cancelTimer: Cancelling the timer")
        self.timer.cancel()
        self.isTimerRunning = False
    
    def addWithDelayToExecutionQueue(self, executionDelay, methodToExecute, parameters):
        self.logger.debug("startTimer: Starts the timer for executing a task")
        self.timer = Timer(executionDelay, methodToExecute, parameters)
        self.timer.start()        
        self.isTimerRunning = True
        
    def addNowToExecutionQueue(self, action):
        self.logger.debug("addNowToExecutionQueue: Adding task %s to execution queue" % (action))
        self.executionQueue.append(action)        
        self.isTimerRunning = False        
        
'''if __name__ == '__main__':    
    print "hop-0"
    buttons = {}
    configuration = Configuration(1, False, buttons)
    processor = Processor(configuration)
    action = Action("s", "b", None)
    processor.executionQueue.join()
    processor.addNowToExecutionQueue(action)
    processor.addNowToExecutionQueue(action)
    print "flop-1"'''