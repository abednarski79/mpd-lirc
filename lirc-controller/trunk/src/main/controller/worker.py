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
        self.logger = logging.getLogger("worker")
    
    def loop(self):
        self.logger.info("Starting up.")
        self.logger.info("Started.")
        while True:
            job = self.workerQueue.get()
            if job is None:
                self.logger.info("Shutdown signal received.")
                break            
            self.onEvent(job)        
    
    def onEvent(self, job):
        cacheKey = job.taskUniqueKey()
        self.logger.info("New job received: %s" % cacheKey)
        if cacheKey not in self.cache:
            self.logger.warning("No task with id: %s in cache: %s" % cacheKey, self.cache);
            return        
        self.logger.debug("Cache contains method: %s" % cacheKey)
        method = self.cache[cacheKey]
        if method is None:
            self.logger.warning("Method is missing: %s" % cacheKey)
            return
        self.logger.info("Executing job: %s" % cacheKey)
        try:
            method(job.parameter)
        except Exception as details:
            self.logger.error("Can't run method %s, details: %s" % (cacheKey, details))
    
    def shutdown(self):
        self.logger.info("Shutting down.")        
        self.workerQueue.put_nowait(None)
            