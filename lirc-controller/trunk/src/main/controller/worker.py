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
        cacheKey = job.taskUniqueKey()
        self.logger.info("Executing job at cache key: %s" % cacheKey)        
        if cacheKey in self.cache:
            self.logger.info("Cache contains key: %s" % cacheKey)
            method = self.cache[cacheKey]
            if method is not None:
                self.logger.info("Method for key: %s is populated." % cacheKey)
                self.logger.debug(type(method))
        else:
            self.logger.error("No task with id: %s in cache: %s" % cacheKey, self.cache);
        '''try:                 
            method()
        except Exception as detail:
            self.logger.error("Error occurred while executing job: %s, error message: %s" % (job, detail));'''        