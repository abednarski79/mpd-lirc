#!/bin/sh
BASEDIR=$(dirname $0)
. $BASEDIR/../configuration.sh
PLAYLIST=/mnt/nasfiles/Radio/0$1_playlist.pls
echo "Loading radio pls list" $PLAYLIST
mpc clear
STATION_URL=`grep '^File[0-9]*' $PLAYLIST | sed -e 's/^File[0-9]*=//'`
echo "Playing radio url" $STATION_URL
mpc add $STATION_URL
$MPD_LIRC_ROOT/commands/utils/volumeUnmute.sh
mpc play

