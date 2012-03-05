#!/bin/sh
BASEDIR=$(dirname $0)
. $BASEDIR/../configuration.sh
# aplay -q /root/scripts/mpd_v2/sounds/beep/beep-8.wav & amixer set Speaker 5%+
aplay -q $MPD_LIRC_ROOT/sounds/beep/beep-8.wav & amixer set Speaker 5%+
