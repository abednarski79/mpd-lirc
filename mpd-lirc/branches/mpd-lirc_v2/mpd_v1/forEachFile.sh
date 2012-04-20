#!/bin/bash
#directory=/mnt/nasfiles/Music/
directory=.
for file in $( find /mnt/nasfiles/Music/05_playlist/ -name "*mp3" )
do
	ls -l $file
done  
