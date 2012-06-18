#!/bin/bash

echo "Starting crawler script in directory: " $1

CRAWLER_COMMAND="python crawler.py"
WORKING_DIRECTORY=$1
DOWNLOADER_COMMAND=/home/abednarski/workspace3/periscopen_trunk/tests/resources/mock_downloader_command.sh
METAINFOREADER_COMMAND=/home/abednarski/workspace3/periscopen_trunk/tests/resources/mock_info_command.sh
CONVERTER_COMMAND=/home/abednarski/workspace3/periscopen_trunk/tests/resources/mock_converter_command.sh
OPTIONS="-d $WORKING_DIRECTORY -t"

if [ -n "$DOWNLOADER_COMMAND" ]; then
	OPTIONS="$OPTIONS -s $DOWNLOADER_COMMAND"
fi

if [ -n "$METAINFOREADER_COMMAND" ] 
then
	OPTIONS="$OPTIONS -m $METAINFOREADER_COMMAND"
fi

if [ -n "$CONVERTER_COMMAND" ] 
then
	OPTIONS="$OPTIONS -c $CONVERTER_COMMAND"
fi

echo "Calling crawler from script with options: " $OPTIONS

$CRAWLER_COMMAND $OPTIONS

echo "Finishing crawler script in directory: " $1
