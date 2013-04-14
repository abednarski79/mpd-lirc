'''
Created on 14 Apr 2013

@author: abednarski
'''

import sys
print sys.path

from main.controller.app import Main

if __name__ == '__main__':    
    main  = Main()
    options = main.readOption()
    print "Options passed from command line: %s" % options
    main.initialize(options.cfg, options.xml)
    main.run()