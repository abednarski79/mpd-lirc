#!/bin/sh

LOCK_FILE="/tmp/busy.lock"
BACKUP_ROOT_PATH=/mnt/nasfiles/Backup

# [check] if other program is currently running
if [ -e $LOCK_FILE ]; then
	echo "Busy, backup task will try next time ..."
	exit
fi	

# create lock file
touch $LOCK_FILE

# run backups

# Beata_Desktop
BACKUP_NAME=Beata_Desktop
CURRENT_BACKUP_PATH=$BACKUP_ROOT_PATH/current_$BACKUP_NAME
SOURCE_FOLDER=/mnt/$BACKUP_NAME/Users/beata/Desktop
LOCAL_FOLDER=/mnt/$BACKUP_NAME
REMOTE_FOLDER=//192.168.1.2/Users
MOUNT_USER=Beata
MOUNT_PASSWORD=kotek
BACKUP_FREQUENCY=1 # how frequently to backup in seconds, 604800 = 7 days, 86400 = 1 day, 2592000 = 1 month
# [check] if the last backup was done more then N seconds ago
/root/scripts/backup/lastChangeGreaterThen.sh $BACKUP_FREQUENCY $CURRENT_BACKUP_PATH && \
# if [check] of last backup time successful then [mount]
/root/scripts/backup/mountSambaShare.sh $LOCAL_FOLDER $REMOTE_FOLDER $MOUNT_USER $MOUNT_PASSWORD && \
# if [mount] successful then [backup]
/root/scripts/backup/backup.sh $BACKUP_ROOT_PATH $SOURCE_FOLDER $BACKUP_NAME
# independent on the [backup] result - [unmount]
/root/scripts/backup/umountSambaShare.sh $LOCAL_FOLDER

# Beata_Movies
BACKUP_NAME=Beata_Movies
CURRENT_BACKUP_PATH=$BACKUP_ROOT_PATH/current_$BACKUP_NAME
SOURCE_FOLDER=/mnt/$BACKUP_NAME
REMOTE_FOLDER=//192.168.1.2/Movies
MOUNT_USER=Beata
MOUNT_PASSWORD=kotek
BACKUP_FREQUENCY=604800 # how frequently to backup in seconds, 604800 = 7 days, 86400 = 1 day, 2592000 = 1 month
# [check] if the last backup was done more then N seconds ago
/root/scripts/backup/lastChangeGreaterThen.sh $BACKUP_FREQUENCY $CURRENT_BACKUP_PATH && \
# if [check] of last backup time successful then [mount]
/root/scripts/backup/mountSambaShare.sh $SOURCE_FOLDER $REMOTE_FOLDER $MOUNT_USER $MOUNT_PASSWORD && \
# if [mount] successful then [backup]
/root/scripts/backup/backup.sh $BACKUP_ROOT_PATH $SOURCE_FOLDER $BACKUP_NAME
# independent on the [backup] result - [unmount]
/root/scripts/backup/umountSambaShare.sh $SOURCE_FOLDER

# TODO
#- but name the backup file .running
# after the setup fill finish rename .running file to the final name

# clean up lock file
rm $LOCK_FILE