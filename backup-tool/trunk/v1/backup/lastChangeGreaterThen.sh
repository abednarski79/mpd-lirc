#!/bin/sh

DELTA=$1
FILE_PATH=$2

if [ -z "$FILE_PATH" ]; then
        echo "Please set file path"
        exit 1
fi

if [ -z "$DELTA" ]; then
        echo "Please set delta time"
        exit 1
fi

if [ ! -e $FILE_PATH ];then
	echo "File "$FILE_PATH" does not exist"
	exit
fi

CURRENT_TIME=`date "+%s"`
LAST_CHANGE_TIME=`stat --format "%Z" $FILE_PATH`
TEMP=$(($LAST_CHANGE_TIME + $DELTA))
if [ $TEMP -gt $CURRENT_TIME ];then
	echo "File was modified bellow the threshold of" $DELTA "seconds."
	exit 1
fi
exit

