#!/bin/sh
# /root/scripts/ledOrangeBlink.sh
BASEDIR=$(dirname $0)
. $BASEDIR/../configuration.sh
aplay -q $MPD_LIRC_ROOT/sounds/beep/beep-8.wav & amixer -S & poweroff
