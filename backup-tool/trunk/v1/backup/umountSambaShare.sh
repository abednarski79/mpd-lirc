#!/bin/sh

# MOUNT_POINT=/mnt/nasfiles/Temp/Beata_Desktop/
LOCAL_MOUNT_POINT=$1

if [ -z "$LOCAL_MOUNT_POINT" ]; then
        echo "Please set local mount point"
        exit 1
fi

# umount shared folder
umount $LOCAL_MOUNT_POINT && \
# remove mount directory
rmdir $LOCAL_MOUNT_POINT 