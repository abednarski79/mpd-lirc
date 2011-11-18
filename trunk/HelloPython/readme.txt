Instalation
-----------

1) Edit $HOME/.bashrc and add lines:

# copy from here ...
# MPD LIC configuration
MPD_LIRC_ROOT=$HOME/workspace/mpd-lirc/build
MPD_LIRC_LIB=$MPD_LIRC_ROOT/lib/python-mpd-0.3.0
MPD_LIRC_BIN=$MPD_LIRC_ROOT/bin
MPD_LIRC_COMMANDS=$MPD_LIRC_ROOT/commands
PYTHONPATH=$MPD_LIRC_BIN:$MPD_LIRC_LIB
export MPD_LIRC_BIN
export MPD_LIRC_COMMANDS
export PYTHONPATH
# ... to here

2) copy file file to directory

