import yaml
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

linux_data_path = os.path.join(dir_path, "linux_list.data")
ssh_data_path = os.path.join(dir_path, "ssh_list.data")

linux_list = eval(open(linux_data_path).read())
ssh_dict = eval(open(ssh_data_path).read())

update_dict = {}
create_dict = {}
delete_list = {}


print (ssh_dict)

# If the IAM user is IN Linux then add them to the update list #
# Else if the IAM is NOT IN Linux then add them to the create list #
if bool(linux_list):
    print("linux_list is empty")
    for x in linux_list:
        for key, value in ssh_dict.items():
            if key in linux_list and key == x:
                update_dict.update([(key, value)])
            #print("This user will be updated on the servers: " + key)
            elif key not in linux_list:
                create_dict.update([(key, value)])
                print("This user will be added to the servers: " + key)
if not bool(linux_list):
    for key, value in ssh_dict.items():
        if key not in linux_list:
            create_dict.update([(key, value)])
            print("This user will be added to the servers: " + key)

print(create_dict)
# If the Linux User is not in IAM but is in Linux and isn't the ec2-user then add to the Delete list #
for x in linux_list:
    #for key, value in ssh_dict.items():
    #    print(key, value)
    if x not in ssh_dict and x != "ec2-user" and x != "ssm-user" and x != "splunk" and x != "sonar" and x != "postfix" and x != "nobody" and x != "operator" and x != "nfsnobody" and x != "bamboo" and x != "apache":
        delete_list.update([("user", x)])
        #delete_list.append(x)
        print("Adding " + x + " to delete list")

update_path = os.path.join(dir_path, "update_users.yml")
create_path = os.path.join(dir_path, "create_users.yml")
delete_path = os.path.join(dir_path, "delete_users.yml")

with open(update_path, 'w') as outfile:
    yaml.dump(update_dict, outfile, default_flow_style=False)

with open(create_path, 'w') as outfile:
    yaml.dump(create_dict, outfile, default_flow_style=False)

with open(delete_path, 'w') as outfile:
    yaml.dump(delete_list, outfile, default_flow_style=False)

print(update_dict)
print(create_dict)
print(delete_list)