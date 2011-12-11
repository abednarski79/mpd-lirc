#!/bin/bash
title=$(mpc -f %file% | head -n1)
BASEDIR=$(dirname $0)
source $BASEDIR/../configuration.sh
aplay -q $MPD_LIRC_ROOT/sounds/beep/beep-8.wav & python $MPD_LIRC_ROOT/commands/voter.py "$title" +1

