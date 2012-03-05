#!/bin/bash
# mpc pause
music_file=/mnt/nasfiles/Music/`mpc -f %file% | head -n1`
voice_file=$music_file.wav
aplay "$voice_file"
mp3info -p "%a, %l, %t" "$music_file" | espeak -w /tmp/example.wav && aplay /tmp/example.wav
# mpc play

