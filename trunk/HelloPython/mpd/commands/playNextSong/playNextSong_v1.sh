#!/bin/bash
BASEDIR=$(dirname $0)
BINDIR=$BASEDIR/../../bin/clients
cd $BINDIR
/usr/bin/python ./commands/cmd_clients.py PLAY_NEXT_SONG