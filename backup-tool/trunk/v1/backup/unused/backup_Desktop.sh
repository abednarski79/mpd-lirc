#!/bin/sh


MOUNT_POINT=/mnt/nasfiles/Temp/Beata_Desktop/
SOUCER_FOLDER=$MOUNT_POINT/beata/Desktop/
MOUNT_ULR=//192.168.1.2/Users
MOUNT_USER=Beata
MOUNT_PASSWORD=kotek
BACKUP_NAME=Beata_Desktop

# cleanup
umount $MOUNT_POINT

# create  mount point
mkdir -p $MOUNT_POINT

# mount drive
mount -t cifs --read-only $MOUNT_ULR $MOUNT_POINT -o user=$MOUNT_USER,password=$MOUNT_PASSWORD
MOUNT_EXIT_STATUS=$?
if [ "$MOUNT_EXIT_STATUS" != 0 ]; then
	echo "Error mounting file system: " $MOUNT_ULR
	exit
fi

# backup
/root/scripts/backup/backup.sh $BACKUP_ROOT $SOUCER_FOLDER $BACKUP_NAME

# clean up mount point
umount $MOUNT_POINT
UMOUNT_EXIT_STATUS=$?
if [ "$UMOUNT_EXIT_STATUS" != 0 ]; then
        echo "Error un-mounting file system: " $MOUNT_ULR
        exit
fi
rm -rf $MOUNT_POINT
