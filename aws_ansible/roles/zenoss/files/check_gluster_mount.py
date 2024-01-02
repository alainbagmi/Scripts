#!/usr/bin/env python

import os, subprocess

# Define Mount point variable, could change this to be passed as input if wanted
mount_point = "/data/shared"

# Check if Mount point is mounted
mount_status = os.path.ismount(mount_point)

#  Logic to mount if not mounted and alert
if mount_status == True:
    print("The Gluster mount is good|g=1")
else:
    print("The Gluster mount is bad|g=0")
    subprocess.Popen(["/bin/mount", mount_point])
