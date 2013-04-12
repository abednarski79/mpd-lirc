'''
Created on 12 Apr 2013

@author: adambednarski

Should be able to react on following commands:

- start - loads configuration and starts listener

- stop - 

Then just start it with ./contollerd.py start, and stop it with ./contollerd.py stop.

'''


#!/usr/bin/python
import time
from daemon import runner

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
    def run(self):
        while True:
            print("Howdy!  Gig'em!  Whoop!")
            time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()