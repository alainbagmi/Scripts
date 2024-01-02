#!/usr/bin/python

import MySQLdb as mariadb
from time import sleep
import sys 
#sys.path.insert(0, '/home/bamboo/')
#import passwords
#password = passwords.passReturn(passwords.dbrepl)

counter = 0 
working = 0
while counter < 50000:

    try:
        mariadb_connection = mariadb.connect('172.23.86.13', 'mysqlrepl', 'my%qL3sd0')
        cursor = mariadb_connection.cursor(mariadb.cursors.DictCursor)

        cursor.execute("SHOW SLAVE STATUS")
        data = cursor.fetchall()
        errors = []
        
        if "error" in data[0]['Last_SQL_Error']: 
            print('Critical: Galera Database Status Compromised | c=1')
            cursor.execute("STOP SLAVE")
            cursor.execute("set global sql_slave_skip_counter=1")
            cursor.execute("START SLAVE")
            working = 0
        else:
            print("Ok | c=0")
            working += 1
            mariadb_connection.close()
    

    except Exception as e:
        print(e)
        print('Critical: Cannot connect to MariaDB | c=1')
  

    if working == 1135: 
        print ('Slave replication seems to be working.  Double check with a show slave status.')

    counter += 1
    sleep(0.4)
exit()
