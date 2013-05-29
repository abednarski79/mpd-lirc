'''
Created on 8 May 2013

@author: abednarski
'''
import logging

class Job:
    
    def __init__(self, buttonId, actionType):
        self.buttonId = buttonId
        self.actionType = actionType
    
    def __str__(self):
        return self.buttonId + ", " + self.actionType
    
        
class Worker:
    
    def __init__(self, configuration, workerQueue):
        self.workerQueue = workerQueue
        self.mapping = configuration.buttons
        self.cache = configuration.cache
        self.logger = logging.getLogger("controllerApp")
    
    def loop(self):
        while True:
            job = self.workerQueue.get()
            if job is None:
                break            
            self.onEvent(job)        
    
    def onEvent(self, job):
        self.logger.info("Executing job: %s" % job)
        method = self.cache[job.taskUniqueKey]
        if(method is None):
            self.logger.error("No task with id: %s in cache." % job.taskUniqueKey);
            return
        try:                 
            method()
        except Exception as detail:
            self.logger.error("Error occurred while executing job: %s, error message: %s" % (job, detail));        