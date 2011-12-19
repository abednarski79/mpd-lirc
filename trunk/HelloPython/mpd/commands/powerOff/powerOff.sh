#!/bin/bash
BASEDIR=$(dirname $0)
source $BASEDIR/../configuration.sh
aplay -q $MPD_LIRC_ROOT/sounds/beep/beep-22.wav & amixer -S & poweroff
