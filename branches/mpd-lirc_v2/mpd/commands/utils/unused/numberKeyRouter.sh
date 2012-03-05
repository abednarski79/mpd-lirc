#!/bin/sh
if [ -r /root/scripts/mpd_v2/resource/menu.flag ]; then
    echo "Menu is off"
    sh /root/scripts/mpd_v2/commands/utils/loadAndPlayRadio.sh $1 
else
    echo "Menu is on"
    sh /root/scripts/mpd_v2/commands/utils/loadAndPlayDirectory.sh $1
fi
