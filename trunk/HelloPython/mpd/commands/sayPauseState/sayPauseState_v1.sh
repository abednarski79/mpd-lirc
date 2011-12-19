#!/bin/bash
BASEDIR=$(dirname $0)
source $BASEDIR/../configuration.sh
perl $MPD_LIRC_ROOT/commands/sayPauseState/sayPauseState.pl