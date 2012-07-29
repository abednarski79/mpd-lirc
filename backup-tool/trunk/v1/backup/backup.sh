#!/bin/sh

BACKUP_ROOT_PATH=$1
SOURCE_PATH=$2
BACKUP_NAME=$3

if [ -z "$BACKUP_ROOT_PATH" ]; then
        echo "Please set backup root path"
        exit
fi

if [ -z "$SOURCE_PATH" ]; then
	echo "Please set source path"
	exit
fi

if [ -z "$BACKUP_NAME" ]; then
	echo "Please set backup name"
	exit
fi

echo "---"$SOURCE_PATH 

date=`date "+%Y-%m-%dT%H_%M_%S"`
CURRENT_WORKING_DIR=$BACKUP_ROOT_PATH/current_$BACKUP_NAME
CURRENT_BACKUP_FOLDER=$BACKUP_ROOT_PATH/back_$BACKUP_NAME-$date

rsync -axP --delete --delete-excluded --link-dest=$CURRENT_WORKING_DIR $SOURCE_PATH $CURRENT_BACKUP_FOLDER
rm -f $CURRENT_WORKING_DIR
ln -s $CURRENT_BACKUP_FOLDER $CURRENT_WORKING_DIR

