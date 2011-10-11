#!/bin/bash
PLAYLIST=0$1_playlist
mpc clear && mpc update && mpc add $PLAYLIST && mpc play
echo "Playlist number $1" > /var/lib/mpd/voice_over/current_playlist.txt
echo "$1" > /var/lib/mpd/playlist_number.txt

