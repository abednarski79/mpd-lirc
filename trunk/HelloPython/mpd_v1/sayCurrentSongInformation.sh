#!/bin/bash
mpc pause
# PLAYLIST_VOICE="Playlist number $PLAYLIST_NUMBER"
cat /var/lib/mpd/voice_over/current_playlist.txt | espeak -s 120 -p 65 -a 800 -w /tmp/voice.wav && aplay /tmp/voice.wav
mpc --format "Album %album% Song %title%" | head -n1 | espeak -s 120 -p 65 -a 800 -w /tmp/voice.wav && aplay /tmp/voice.wav
mpc play

