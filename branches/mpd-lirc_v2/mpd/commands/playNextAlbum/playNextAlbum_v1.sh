#!/bin/sh
BASEDIR=$(dirname $0)
. $BASEDIR/../configuration.sh
python $MPD_LIRC_BIN/command/clients/cmd_clients.py PLAY_NEXT_ALBUM
