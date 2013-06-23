'''
Created on 23 Jun 2013

@author: abednarski
'''

import signal, os, time, sys

def shutdown(signum, frame):
    print "Shutting down"
    exit(0)

if __name__ == '__main__':
    i = 0    
    f = open('/tmp/log.txt', 'w')
    sys.stdout = f
    signal.signal(signal.SIGTERM, shutdown)    
    while True:
        i = i + 1
        print "Still alive ! %s" % i
        f.flush() 
        time.sleep(0.25)
