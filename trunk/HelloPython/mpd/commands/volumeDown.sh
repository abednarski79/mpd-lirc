#!/bin/bash
BASEDIR=$(dirname $0)
SOUNDSDIR=$BASEDIR/../sounds
aplay -q $SOUNDSDIR/beep/beep-8.wav & amixer set Speaker 5%-