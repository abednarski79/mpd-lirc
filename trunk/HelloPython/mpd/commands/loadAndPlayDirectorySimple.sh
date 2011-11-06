#!/bin/bash
PLAYLIST=0$1_playlist
mpc --wait clear
mpc update 
mpc --wait add $PLAYLIST
echo "Loading playlist" $PLAYLIST
mpc play

