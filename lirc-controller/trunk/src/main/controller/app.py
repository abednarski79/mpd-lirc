
from datetime import datetime
from main.controller.configuration import ConfigurationReader
from main.controller.processor import Processor
from optparse import OptionParser
# import pylirc
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
                print "mandatory option %s is missing" % m
                parser.print_help()
                exit(-1)
        return options
        
    def initialize(self, configCfg, configXml):
        self.logger.info("Initializing ...")
        configurationReader = ConfigurationReader(configXml)
        configuration = configurationReader.readConfiguration()
        self.processor = Processor(configuration)
        self.lirchandle = pylirc.init("pylirc", configCfg, configuration.blocking)            
    
    def run(self):
        isRunning = 1
        previousTime = 0;
        if(self.lirchandle):
            inputLirc = [self.lirchandle]
            print "Succesfully opened lirc, handle is " + str(self.lirchandle)
            while isRunning:
                inputready,outputready,exceptready = select.select(inputLirc,[],[])
                s = pylirc.nextcode(1)
                currentTime = datetime.now().microsecond                        
                if(s):
                    for code in s:
                        repeat = code["repeat"]
                        currentCommand = code["config"]
                        print "\nDelta %s, command %s, repleat %s" % ((currentTime -previousTime), currentCommand, repeat)
                        self.processor.processEvent(currentCommand, repeat)
                        previousTime = currentTime                    
        pylirc.exit()