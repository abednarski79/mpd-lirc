#!/bin/bash
title=$(mpc -f %file% | head -n1)
aplay -q ../sounds/beep/beep-8.wav & python ./voter.py "$title" +1

