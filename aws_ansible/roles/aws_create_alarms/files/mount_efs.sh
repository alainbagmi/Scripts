#!/bin/sh
export AWS_CONFIG_FILE="/etc/aws/config"
export AWS_SHARED_CREDENTIALS_FILE="/etc/aws/credentials"
#Variables
EC2_ID=($(cat /var/lib/cloud/data/instance-id))
TIME_STAMP=($(date '+%Y-%m-%dT%H:%M:%SZ'))
EFS_MOUNT_FLAG=1
echo $EC2_ID
echo $TIME_STAMP
while IFS='|' read -r A B C D E
do
echo "$A"
echo "$B"
echo "$C"
echo "$D"
echo "$E"
#Mount = mount -t command
EFS_MOUNT="$A"
#DNS = Asset/vhost url
EFS_DNS="$B"
#Mount Point = asset/vhost path
EFS_MOUNT_POINT="$C"
#Metric Name
METRIC_NAME="${D}"
MOUNT_ENV="$E"
EFS_MOUNT_STATUS=($(df -h | grep $EFS_MOUNT_POINT | awk '{print $1}'))
echo $METRIC_NAME
echo "Mount Status"
echo $EFS_MOUNT_STATUS
if [ "$EFS_MOUNT_STATUS" == "$EFS_DNS" ];
then
   echo "$D mount is good"
   /usr/local/bin/aws cloudwatch put-metric-data --metric-name $METRIC_NAME --namespace EFSMount --value 1 --timestamp $TIME_STAMP --dimensions InstanceId=$EC2_ID,Environment=$MOUNT_ENV
else
   echo "$D Mount is bad"
   /usr/local/bin/aws cloudwatch put-metric-data --metric-name $METRIC_NAME --namespace EFSMount --value 0 --timestamp $TIME_STAMP --dimensions InstanceId=$EC2_ID,Environment=$MOUNT_ENV
   sudo $EFS_MOUNT $EFS_DNS $EFS_MOUNT_POINT
   EFS_MOUNT_FLAG=0
fi
done < /usr/local/bin/efs_volume
if [ "$EFS_MOUNT_FLAG" == 0 ];
then
   echo $EFS_MOUNT_FLAG
   sudo systemctl restart httpd
else
   echo "Nothing to see here"
fi