#!/usr/bin/python
 
import cmd
import json
import subprocess
import requests
import sys
import time
 

try:
   alias = sys.argv[1]
except Exception as e:
#   print e
   print "No tenant alias was passed into the script."
   exit(1)

try:
   drupal_version = sys.argv[2]
except Exception as e:
#   print e
   print "No drupal version was passed into the script."
   exit(1)


tenant_distro_list = [ {'tenant_alias':'cbp',
                        'jira_distro':'WCM-CBP-dotGov-Developers'},
                       {'tenant_alias':'cfema',
                        'jira_distro':'WCM-FEMA-Career-Developers'},
                       {'tenant_alias':'daipd8',
                        'jira_distro':'WCM-DA-dotGov-Developers'},
                       {'tenant_alias':'dhs',
                        'jira_distro':'WCM-DHS-dotGov-Developers'},
                       {'tenant_alias':'diamond',
                        'jira_distro':'ALM-DHS-Diamond-Developers'},
                       {'tenant_alias':'fema',
                        'jira_distro':'WCM-FEMA-dotGov-Developers'},
                       {'tenant_alias':'femad8',
                        'jira_distro':'WCM-FEMA-dotGov-Developers'},
                       {'tenant_alias':'fleta',
                        'jira_distro':'WCM-FLETA-dotGov-Developers'},
                       {'tenant_alias':'fletc',
                        'jira_distro':'WCM-FLETC-dotGov-Developers'},

                       {'tenant_alias':'fletad8',
                        'jira_distro':'WCM-FLETA-dotGov-Developers'},
                       {'tenant_alias':'fletcd8',
                        'jira_distro':'WCM-FLETC-dotGov-Developers'},


                       {'tenant_alias':'ice',
                        'jira_distro':'WCM-ICE-dotGov-Developers'},
                       {'tenant_alias':'ics',
                        'jira_distro':'WCM-CERT-dotGov-Developers'},
                       {'tenant_alias':'niccs',
                        'jira_distro':'WCM-NICCS-dotGov-Developers'},
                       {'tenant_alias':'cisa',
                        'jira_distro':'ALM-CISA-CISAGOV-Developers'},
                       {'tenant_alias':'oig',
                        'jira_distro':'WCM-HHS-OIG-Developers'},
                       {'tenant_alias':'precheck',
                        'jira_distro':'WCM-TSA-PreCheck-Developers'},
                       {'tenant_alias':'niem',
                        'jira_distro':'WCM-ISEO-NIEM-Developers'},
                       {'tenant_alias':'rfema',
                        'jira_distro':'WCM-FEMA-dotGov-Developers'},
                       {'tenant_alias':'ready',
                        'jira_distro':'WCM-FEMA-dotGov-Developers'},
                       {'tenant_alias':'readyd8',
                        'jira_distro':'WCM-FEMA-dotGov-Developers'},
                       {'tenant_alias':'sits',
                        'jira_distro':'WCM-SITS-dotGov-Developers'},
                       {'tenant_alias':'tsa2',
                        'jira_distro':'WCM-TSA-dotGov-Developers'},
                       {'tenant_alias':'tsanews',
                        'jira_distro':'ALM-TSA-TASM-Developers'},
                       {'tenant_alias':'uscertd8',
                        'jira_distro':'WCM-CERT-dotGov-Developers'},
                       {'tenant_alias':'uscis',
                       'jira_distro':'WCM-CIS-dotGov-Developers'},
                       {'tenant_alias':'uscisd8',
                        'jira_distro':'WCM-CIS-dotGov-Developers'},
                       {'tenant_alias':'everify',
                        'jira_distro':'WCM-CIS-dotGov-Developers'},
                       {'tenant_alias':'rfema',
                        'jira_distro':'WCM-FEMA-dotGov-Developers'},
                       {'tenant_alias':'schoolsafety',
                        'jira_distro':'WCM-CISA-SCHSFTY-Developers'},

                  
                     ]
foundAlias = False
for tenant in tenant_distro_list:
  test = tenant["tenant_alias"]
  if test == alias:
    foundAlias = True
    break

if foundAlias == False:
    print("tenant alias not found in script's alias list")
    exit(1)


#Get the count of active sysadmins on the WCM team
user = "YmFtYm9vOkJhbUIwMGklNTYyMg=="
headers = {'Authorization': 'Basic YmFtYm9vOkJhbUIwMGklNTYyMg==', 'Content-Type': 'application/json'}
base_url = "http://172.22.58.14:8080/jira/rest/"
user_path = "api/2/group/member"
 
datapoints = {'groupname': "WCM-WCM-System-Admins", 'expand': 'groups'}
url = base_url + user_path
r = requests.get(url, headers=headers, params=datapoints)
data = r.json()

index = 0
userCount = int(data["total"])
emailList = []
emailListString = ""


for tenant in tenant_distro_list:
 #If the tenant aliases don't match, then ship the test of the loop iteration (since we dont care)
   if tenant['tenant_alias'] != alias:
      continue
 
 #If the tenant aliases do match, get all of the data
   else:
      datapoints = {'groupname': tenant['jira_distro'], 'expand': 'groups'}
      url = base_url + user_path
      r = requests.get(url, headers=headers, params=datapoints)
      data = r.json()
 
 #Subtract the count of the WCM-System-Admins group due since they are embedded in the group, and we don't want to pull their names.
      userList = data["values"]
      userList = userList[:-userCount or None]


#D8 only - Add the index location to the appended email due to format that the arguments have to be passed into the drush commands for D8 
      if drupal_version == "8":
        for user in userList:
           if user['active'] == True:
              emailList.append(str(index) + " " + user['name'])
              index += 1

#add in WCM admins.  Get current index by getting the length of the list
        emailList.append(str(len(emailList)) + " " + 'kyle.day@associates.hq.dhs.gov')
        emailList.append(str(len(emailList)) + " " + 'cathleen.tracy@hq.dhs.gov')
        emailList.append(str(len(emailList)) + " " + 'ryan.tackett@associates.hq.dhs.gov')
        emailList.append(str(len(emailList)) + " " + 'jacqi.hakun@associates.hq.dhs.gov')

        for email in emailList:
          print email


#D7 - Dont add indexes to the string due to the way the arguments are passed into the Drush command for D7
      if drupal_version == "7":
        for user in userList:
           if user['active'] == True:

#You have to add single quotes in as a literal string, so you enclose them with "'s and \'s
              emailList.append("\"" + user['name'] + "\"")
              index += 1
         
        emailList.append("\"kyle.day@associates.hq.dhs.gov\"")
        emailList.append("\"cathleen.tracy@hq.dhs.gov\"")
        emailList.append("\"ryan.tackett@associates.hq.dhs.gov\"")
        emailList.append("\"jacqi.hakun@associates.hq.dhs.gov\"")

        for item in emailList: 
          emailListString = emailListString + item + ","

#        print emailListString
        print ','.join(emailList)



#print ""
#print ""
#i = 0
#env = "staging"
#for email in emailList:
#  emailList[i] = '\'' + email + '\''
#  i=i+1
#  stringName = ','.join(emailList)
#command = 'php -r "print json_encode(array('+stringName+'));" | /usr/local/bin/drush --alias-path=/data/bamboo_scripts/drush_aliases @'+alias+'.'+env+' --root=/var/www/html/wwwroot/'+env+'.'+alias+'_gov_build/docroot vset --format=json update_notify_emails -'
#print command 



#env = "staging"
#i = 0
#for email in emailList:
#  emailList[i] = '\'' + email + '\''
#  i=i+1
#  stringName = ','.join(emailList)

#command = 'php -r "print json_encode(array('+stringName+'));" | /usr/local/bin/drush --alias-path=/data/bamboo_scripts/drush_aliases @'+alias+'.'+env+' --root=/var/www/html/wwwroot/'+env+'.'+alias+'_gov_build/docroot vset --format=json update_notify_emails -'
#print command



