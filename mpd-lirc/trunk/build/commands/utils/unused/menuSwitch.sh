#!/bin/sh
BASEDIR=$(dirname $0)
. $BASEDIR/../configuration.sh
aplay -q $MPD_LIRC_ROOT/sounds/beep/beep-8.wav 
if [ -r /root/scripts/mpd_v2/resource/menu.flag ]; then
    rm /root/scripts/mpd_v2/resource/menu.flag
else
    touch /root/scripts/mpd_v2/resource/menu.flag    
fi
