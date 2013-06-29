
import pylirc
import select
import Queue
import logging

class Event():
    def __init__(self, key, repeat):
        self.key = key
        self.repeat = repeat
        
class Generator():
    
    def __init__(self, configurationPath, outputQueue):
        self.processorQueue = outputQueue
        self.logger = logging.getLogger("generator")
        self.lirchandle = pylirc.init("pylirc", configurationPath, False)

    def loop(self):
        if(self.lirchandle):
            inputLirc = [self.lirchandle]
            self.logger.info("Succesfully opened lirc, handle is " + str(self.lirchandle))
            while True:
                self.logger.debug("Before select...")
                inputready, outputready, exceptready = select.select(inputLirc,[],[])
                self.logger.debug("After select...")
                s = pylirc.nextcode(1)                    
                self.logger.debug("After next-code...")
                if(s):
                    self.logger.debug("After if...")
                    for code in s:
                        self.logger.debug("After for...")
                        repeat = code["repeat"]
                        currentCommand = code["config"]
                        try:
                            self.processorQueue.put_nowait(Event(currentCommand, repeat))
                        except Queue.Full:
                            self.logger.error("Processor queue is overloaded.")                    
        pylirc.exit()