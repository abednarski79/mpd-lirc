'''
Created on 14 Apr 2013

@author: abednarski
'''

import logging.config
# from main.controller.generator import Generator
from main.controller.processor_2 import Processor
from main.controller.worker import Worker
from optparse import OptionParser
from multiprocessing import Process, Queue
from main.controller.configuration import ConfigurationReader

class Main:
    
    def __init__(self):
        logging.config.fileConfig('logging.conf')
        self.logger = logging.getLogger("controllerApp")
        
    def parseOptions(self):
        parser = OptionParser()
        parser.add_option("-c", "--conf", 
                          dest="cfg", 
                          action="store",
                          help="configuration from cfg FILE", 
                          metavar="FILE")
        parser.add_option("-x", "--xml", 
                          dest="xml", 
                          action="store",
                          help="configuration from xml FILE", 
                          metavar="FILE")
        (options, args) = parser.parse_args()  
        # Making sure all mandatory options appeared.
        mandatories = ['cfg', 'xml']
        for m in mandatories:
            if not options.__dict__[m]:
                self.logger.error("mandatory option %s is missing" % m)
                parser.print_help()
                exit(-1)
        return options
    
if __name__ == '__main__':
    main = Main()    
    parameters = main.parseOptions()
    configurationReader = ConfigurationReader(parameters.xml)
    configuration = configurationReader.readConfiguration()    
    generatorQueue = Queue()
    workerQueue = Queue()
    # generator = Generator(generatorQueue)
    processor = Processor(configuration.buttons, generatorQueue, workerQueue)
    worker = Worker(workerQueue)
    # generatorProcess = Process(target = generator.loop)
    processorProcess = Process(target = processor.loop)
    workerProcess = Process(target = worker.loop)
    workerProcess.start()
    processorProcess.start()
    # generatorProcess.start()
    generatorQueue.put_nowait("FORWARD_ID")
    
