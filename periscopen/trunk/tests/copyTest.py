'''
Created on 14 May 2012

@author: abednarski
'''

import shutil
import logging


def copySubtitle( srcFile, dstFile):
    log = logging.getLogger(__name__)
    log.debug("Copying file: %s to: %s" % (srcFile, dstFile))
    try:            
        shutil.copy2(srcFile, dstFile)
        log.debug("File copied successfully to: %s " % dstFile)
        return dstFile
    except IOError as (errno, strerror):
        log.error("IOError error %s while copying file from %s to %s" % (strerror, srcFile, dstFile))
        raise
    except :
        log.error("Error while copying file from %s to %s" % (srcFile, dstFile))
        raise

src = "/media/nas/Torrent/The_Kings_Speech_2010/The_Kings_Speech_2010.OpenSubtitles_pl_1.srt"

dst = "/media/nas/Torrent/The_Kings_Speech_2010/The_Kings_Speech_2010.srt"

copySubtitle(src, dst)
