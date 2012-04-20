#!/bin/bash
title=$(mpc -f %file% | head -n1)
aplay -q /root/scripts/mpd_v1/sounds/beep/beep-8.wav & python /root/scripts/mpd_v1/voter.py "$title" +1

