'''
Created on 14 Apr 2013

@author: abednarski
'''
import logging
import logging.config
from main.controller.app import Main

if __name__ == '__main__':
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger("controllerApp")
    main  = Main()
    options = main.readOption()
    logger.info("Options passed from command line: %s" % options)
    main.initialize(options.cfg, options.xml)
    main.run()