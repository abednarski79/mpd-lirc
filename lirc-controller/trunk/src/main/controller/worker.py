'''
Created on 8 May 2013

@author: abednarski
'''
import logging

class Worker:
    
    def __init__(self, workerQueue):
        self.workerQueue = workerQueue
        self.logger = logging.getLogger("controllerApp")
    
    def process(self):
        while True:
            job = self.workerQueue.get()            
            self.onEvent(job)        
    
    def onEvent(self, job):
        self.logger.info("Executing method: " + job)
        try:
            job()
        except Exception as detail:
            self.logger.error("Error occurred while executing job: %s, error message: %s" % (job, detail));
            