#!/bin/bash
# MPD LIC configuration
MPD_LIRC_ROOT=/root/scripts/mpd_v2
MPD_LIRC_LIB=$MPD_LIRC_ROOT/lib/python-mpd-0.3.0
MPD_LIRC_BIN=$MPD_LIRC_ROOT/bin
PYTHONPATH=$MPD_LIRC_BIN:$MPD_LIRC_LIB
export MPD_LIRC_ROOT
export PYTHONPATH
