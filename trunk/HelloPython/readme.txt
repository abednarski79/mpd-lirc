Instalation
-----------

1) Edit $HOME/.bashrc and add lines:

# copy from here ...
# MPD LIC configuration
MPD_LIRC_LIB=/home/abednarski/workspace/mpd-lirc/build/lib/python-mpd-0.3.0
MPD_LIRC_BIN=/home/abednarski/workspace/mpd-lirc/build/bin
PYTHONPATH=$MPD_LIRC_BIN:$MPD_LIRC_LIB
export MPD_LIRC_BIN
export PYTHONPATH
# ... to here

2) copy file file to directory

