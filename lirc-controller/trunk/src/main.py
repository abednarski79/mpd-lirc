'''
Created on 14 Apr 2013

@author: abednarski
'''

import logging.config
from main.controller.generator import Generator
from main.controller.simple_processor import Processor
from optparse import OptionParser
from multiprocessing import Process, Queue

class Main:
    
    def __init__(self):
        logging.config.fileConfig('logging.conf')
        self.logger = logging.getLogger("controllerApp")
        
    def parseOption(self):
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
    generatorQueue = Queue()
    workerQueue = Queue()
    generator = Generator(generatorQueue)
    processor = Processor(generatorQueue, workerQueue)
    
    TODO: implement this guy !!!    
    worker = Worker(worker)
    generatorProcess = Process(target = generator.process)
    processorProcess = Process(target = processor.process)
    workerProcess = Process(target = worker.process)
    workerProcess.start()
    processorProcess.start()
    generatorProcess.start()
    
    
    '''def __init__(self):
        self.logger = logging.getLogger("controllerApp")
        self.logger.info("Loading configuration ..")
        configurationReader = ConfigurationReader(configXml)
        configuration = configurationReader.readConfiguration()
        self.logger.info("Processing configuration ...")
        self.processor = Processor(configuration)
        self.logger.info("Initializing pylirc handler, configuration file: %s, blocking: %s" % (configCfg, configuration.blocking))
        self.lirchandle = pylirc.init("pylirc", configCfg)'''
    

    '''logging.config.fileConfig('logging.conf')
    logger = logging.getLogger("controllerApp")
    generator  = Main()
    options = main.readOption()
    logger.info("Options passed from command line: %s" % options)
    main.initialize(options.cfg, options.xml)
    main.run()'''