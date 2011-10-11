#!/bin/bash
title=$(mpc -f %file% | head -n1)
aplay -q /root/scripts/mpd/sounds/beep/beep-8.wav & python /root/scripts/mpd/voter.py "$title" -1

