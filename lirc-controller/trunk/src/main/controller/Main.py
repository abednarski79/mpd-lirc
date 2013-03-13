from ProcessorTest import ProcessorTest
from datetime import datetime
from main.controller import ConfigurationReader, Processor
from optparse import OptionParser
import pylirc
import select

class Main():

    def readOption(self):
        parser = OptionParser()
        parser.add_option("-c", "--conf", 
                          dest="cfg", 
                          action="store",
                          help="reads configuration from cfg FILE", 
                          metavar="FILE")
        parser.add_option("-x", "--xml", 
                          dest="xml", 
                          action="store",
                          help="reads configuration from xml FILE", 
                          metavar="FILE")
        (options, args) = parser.parse_args()    
        return options
    
    def initialize(self, configCfg, configXml):
        print "Initializing ..."
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