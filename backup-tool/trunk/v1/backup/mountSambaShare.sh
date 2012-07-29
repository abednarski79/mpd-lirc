#!/bin/sh

# MOUNT_POINT=/mnt/nasfiles/Temp/Beata_Desktop/
LOCAL_MOUNT_POINT=$1
# MOUNT_ULR=//192.168.1.2/Users
REMOTE_MOUNT_POINT=$2
# MOUNT_USER=Beata
USER_NAME=$3
# MOUNT_PASSWORD=kotek 
PASSWORD=$4

OPTIONS="-t cifs --read-only"
CREDENTIALS=""

if [ -z "$LOCAL_MOUNT_POINT" ]; then
        echo "Please set local mount point"
        exit 1
fi

if [ -z "$REMOTE_MOUNT_POINT" ]; then
        echo "Please set remote mount point"
        exit 1
fi

if [ -n "$USER_NAME" ] && [ -z "$PASSWORD" ]; then
		echo "Please set password as user name provided"
		exit 1
fi

if [ -z "$USER_NAME" ] && [ -n "$PASSWORD" ]; then
		echo "Please set username as password provided"
		exit 1
fi
		
if [ -n "$USER_NAME" ] && [ -n "$PASSWORD" ]; then
		CREDENTIALS="-o username="$USER_NAME",password="$PASSWORD		
fi


# create  mount point
mkdir -p $LOCAL_MOUNT_POINT && \
# mount shared folder
mount $OPTIONS $REMOTE_MOUNT_POINT $LOCAL_MOUNT_POINT $CREDENTIALS
