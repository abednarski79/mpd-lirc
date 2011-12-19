#!/bin/bash
BASEDIR=$(dirname $0)
source $BASEDIR/../configuration.sh
aplay -q $MPD_LIRC_ROOT/sounds/beep/beep-8.wav & amixer set Speaker 5%-