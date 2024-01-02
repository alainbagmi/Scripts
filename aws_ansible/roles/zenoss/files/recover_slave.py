#!/usr/bin/python

import MySQLdb as mariadb
import sys 
#sys.path.insert(0, '/home/bamboo/')
#import passwords

#password = passwords.passReturn(passwords.dbrepl)

counter = 0 
working = 0
while counter < 50000:


    try:
        mariadb_connection = mariadb.connect('172.23.86.13', 'mysqlrepl', 'F1ng3rF00d')
        cursor = mariadb_connection.cursor(mariadb.cursors.DictCursor)

        cursor.execute("SHOW SLAVE STATUS")
        data = cursor.fetchall()
        errors = []
        file = open("dberrors.txt", "a") 

        #This will only skip the errors inside of the cache tables.  Any other SQL errors should examined manually and determined if they should be skipped.  They can be manually added to this if statement if they recur enough.
        
        if "PRIMARY" in data[0]['Last_SQL_Error'] or "semaphore" in data[0]['Last_SQL_Error'] or "cache_form" in data[0]['Last_SQL_Error'] or "HA_ERR_FOUND_DUPP_KEY" in data[0]['Last_SQL_Error'] or "captcha_sessions" in data[0]['Last_SQL_Error'] or "queue" in data[0]['Last_SQL_Error'] or "breakpoints" in data[0]['Last_SQL_Error'] or "history" in data[0]['Last_SQL_Error'] or "cache_update" in data[0]['Last_SQL_Error'] or "watchdog" in data[0]['Last_SQL_Error'] or "sessions" in data[0]['Last_SQL_Error'] or "job_schedule" in data[0]['Last_SQL_Error'] or "views_data_export" in data[0]['Last_SQL_Error'] or "file_usage" in data[0]['Last_SQL_Error'] or "file_managed" in data[0]['Last_SQL_Error'] or "feeds_log" in data[0]['Last_SQL_Error'] or "Delete_rows_v1" in data[0]['Last_SQL_Error'] or "system" in data[0]['Last_SQL_Error']  or "variable" in data[0]['Last_SQL_Error']  or "key_value" in data[0]['Last_SQL_Error']  or "cache_feeds" in data[0]['Last_SQL_Error']: 
            data2 = data[0]['Last_SQL_Error']
            print('Critical: Galera Database Status Compromised | c=1')
            
            errors.append(data[0]['Last_SQL_Error'] + '\n')
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
  

    if working == 500:
        print ('Slave replication seems to be working.  Double check with a show slave status.')

    for item in errors:
        file.write(item)
 
    file.close()
    counter += 1
exit()
