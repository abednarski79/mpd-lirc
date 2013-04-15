
from datetime import datetime
from main.controller.configuration import ConfigurationReader
from main.controller.processor import Processor
from optparse import OptionParser
import pylirc
import select
import logging

class Main():
    
    def __init__(self):
        self.logger = logging.getLogger("controllerApp")
        
    def readOption(self):
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
        
    def initialize(self, configCfg, configXml):
        self.logger.info("Loading configuration ..")
        configurationReader = ConfigurationReader(configXml)
        configuration = configurationReader.readConfiguration()
        self.logger.info("Processing configuration ...")
        self.processor = Processor(configuration)
        self.logger.info("Initializing pylirc handler, configuration file: %s, blocking: %s" % (configCfg, configuration.blocking))
        self.lirchandle = pylirc.init("pylirc", configCfg)
    
    def run(self):
        isRunning = 1
        previousTime = 0;
        if(self.lirchandle):
            inputLirc = [self.lirchandle]
            self.logger.info("Succesfully opened lirc, handle is " + str(self.lirchandle))
            while isRunning:
                inputready,outputready,exceptready = select.select(inputLirc,[],[])
                s = pylirc.nextcode(1)
                currentTime = datetime.now().microsecond                        
                if(s):
                    for code in s:
                        repeat = code["repeat"]
                        currentCommand = code["config"]
                        self.logger.debug("Delta %s, command %s, repleat %s" % ((currentTime -previousTime), currentCommand, repeat))
                        self.processor.processEvent(currentCommand, repeat)
                        previousTime = currentTime                    
        pylirc.exit()