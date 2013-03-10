import pylirc
import select
from optparse import OptionParser
from ProcessorTest import ProcessorTest
from datetime import datetime

def main():    
    options = readOption()
    initialize(options.conf)

def readOption():
    parser = OptionParser()
    parser.add_option("-c", "--conf", 
                      dest="conf", 
                      action="store",
                      help="reads configuration from FILE", 
                      metavar="FILE")    
    (options, args) = parser.parse_args()    
    return options

def initialize(config):
    print "Initializing ..."
    processor = ProcessorTest()
    isRunning = 1
    blocking = 0
    previousTime = 0
    lirchandle = pylirc.init("pylirc", config, blocking)
    if(lirchandle):
        inputLirc = [lirchandle]
        print "Succesfully opened lirc, handle is " + str(lirchandle)
        while isRunning:
            inputready,outputready,exceptready = select.select(inputLirc,[],[])
            s = pylirc.nextcode(1)
            currentTime = datetime.now().microsecond                        
            if(s):
                for code in s:
                    repeat = code["repeat"]
                    currentCommand = code["config"]
                    print "\nDelta %s, command %s, repleat %s" % ((currentTime -previousTime), currentCommand, repeat)
                    processor.processEvent(currentCommand, repeat)
                    previousTime = currentTime                    
    pylirc.exit()    

if __name__ == '__main__':
    main()