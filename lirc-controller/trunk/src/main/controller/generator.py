
import pylirc
import select

class Event():
    def __init__(self, code, repeat):
        self.code = code
        self.repeat = repeat
        
class Generator():
    
    def __init___(self, outputQueue):
        self.outputQueue = outputQueue
        
    def process(self):        
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
                        self.outputQueue.put(Event(currentCommand, repeat))                    
        pylirc.exit()