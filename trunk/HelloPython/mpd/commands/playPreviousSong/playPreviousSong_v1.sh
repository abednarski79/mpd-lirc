#!/bin/bash
BASEDIR=$(dirname $0)
source $BASEDIR/../configuration.sh
python $MPD_LIRC_BIN/command/clients/cmd_clients.py PLAY_PREVIOUS_SONG