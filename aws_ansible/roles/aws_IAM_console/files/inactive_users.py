import boto3
import sys
import os
import yaml
import datetime
from datetime import datetime
from dateutil.tz import tzutc

dir_path = os.path.dirname(os.path.realpath(__file__))

resource = boto3.resource('iam')
client = boto3.client('iam')
today = datetime.now()


def get_inactive_users():
    disabled_user_list = []
    for user in resource.users.all():
        if user.password_last_used is not None:
           delta = (today - user.password_last_used.replace(tzinfo=None)).days
           if delta >= 90:
              disabled_user_list.append(user.user_name)
              print("Username: ", user.user_name, delta)
    return (disabled_user_list)

def get_nonprotected_users(list_1):
    nonprotected_list = []
    for user in list_1:
        get_user =resource.User(user)
        if get_user.tags:
           for tag in get_user.tags:
               if tag['Key'] == 'user_type' and tag['Value'] != 'protected':
                  nonprotected_list.append(get_user.user_name)
                  print(get_user.user_name)
    return (nonprotected_list)

def get_protected_users():
    for user in resource.users.all():
        get_user = resource.User(user.user_name)
        if get_user.tags:
           for tag in get_user.tags:
               if tag['Key'] == 'user_type' and tag['Value'] == 'protected':
                  print(get_user.user_name)

def get_test_users():
    test_list = []
    for user in resource.users.all():
        get_user = resource.User(user.user_name)
        if get_user.tags:
           for tag in get_user.tags:
               if tag['Key'] == 'user_type' and tag['Value'] == 'test':
                  test_list.append(get_user.user_name)
                  print(get_user.user_name)
    return (test_list)
   
def write_to_yaml(list_1):
    disable_users = {'disabled_users': list_1}
    disabled_path = os.path.join(dir_path, "disabled_users.yml")
    with open(disabled_path, 'w') as outfile:
        yaml.dump(disable_users, outfile, explicit_start=True, default_flow_style=False)  
    
def main():
    #Don't Remove Below this line
    inactive_users = get_inactive_users()
    nonprotected_users = get_nonprotected_users(inactive_users)
    write_to_yaml(nonprotected_users)
#    test_users = get_test_users()
#    write_to_yaml(test_users)
    
if __name__=="__main__":
   main()
