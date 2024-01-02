#!/bin/bash

/sbin/service tomcat stop
/bin/rm -rf /var/cache/tomcat/work/*
/bin/rm -rf /usr/share/tomcat/guvnorrepo/repository
/bin/rm -rf /usr/share/tomcat/guvnorrepo/workspaces
/bin/sleep 20
/sbin/service tomcat start

