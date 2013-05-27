
import pylirc
import select
import Queue

class Event():
    def __init__(self, key, repeat):
        self.key = key
        self.repeat = repeat
        
class Generator():
    
    def __init___(self, outputQueue):
        self.processorQueue = outputQueue
        
    def loop(self):        
        if(self.lirchandle):
            inputLirc = [self.lirchandle]
            self.logger.info("Succesfully opened lirc, handle is " + str(self.lirchandle))
            while True:
                inputready, outputready, exceptready = select.select(inputLirc,[],[])
                s = pylirc.nextcode(1)                    
                if(s):
                    for code in s:
                        repeat = code["repeat"]
                        currentCommand = code["config"]
                        try:
                            self.processorQueue.put_nowait(Event(currentCommand, repeat))
                        except Queue.Full:
                            self.logger.error("Processor queue is overloaded.")                    
        pylirc.exit()