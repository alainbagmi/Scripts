aws_tenant_creation tasks
-----------
* Create testint,staging and prod databases and db users if they don't exist
* Create the tenants Bitbucket project if it doesn't exist
* Clone the myd8 repo and change myd8 to tenant, create the _gov repo and branches
* Run drush make, create the _gov_build repo and branches
* Create the settings repo
* Initialize all git repos and make origin the bitbucket repos

-----------
External Tasks (must be done manually)
Pre-Tasks:
* Find the required values to run the plan
    * akamai_group- Find in Akamai
    * akamai_path- Can be found in Akamai config, or on netstorage
    * daily_db- database that is associated with the target environment (test, stage or prod)
    * db_pass- Password created by engineers
    * drupal_version- 
    * edit_code- Akamai config
    * edit_url- Akamai config
    * prod_edit_code- Akamai config
    * prod_public_code- Akamai config
    * public_code- Akamai config
    * tenant- tenant's site name i.e. iced8, cbp
    * site_url- Akamai config
    * stash_project- Bitbucket
    * env-
Post-Tasks:
* Edit Project permissions (if project is new), to allow dev groups access
* Edit Repo permissions to allow dev groups access
* Add new relic id to group_vars/tenants once it is available



aws_tenant_onboarding tasks: initial
-----------
* Create the tenant_vars file for Ansible
* Create the Asset files directory including /files, /private and /tmp
* Create the wwwroot directory (env.tenant_gov_build)
* Create the appropriate branch in wwwroot for the env and run the git config core.fileMode command
* Create the vhost edit and public files in /etc/httpd/tenants
* Create symlinks for edit and public files in /etc/httpd

aws_tenant_onboarding tasks: update
-----------
* Update the tenant vars file with urls, database backup env
* Create the Asset files directory including /files, /private and /tmp
* Create the wwwroot directory (env.tenant_gov_build)
* Create the appropriate branch in wwwroot for the env and run the git config core.fileMode command
* Create the vhost edit and public files in /etc/httpd/tenants
* Create symlinks for edit and public files in /etc/httpd
* Update the drush.yml file with env



Extra-Vars
=======================
Tenant Initial Creation
-------------
Key | Value | Notes
--------- | --------- | --------- |
akamai_group | 115983
akamai_path | /183946/wcmdemo
daily_db | test
db_pass | Th!si5@t3st
drupal_version | 8
edit_code | 1043586
edit_url | edit-preview.punzo.dhs.gov
prod_edit_code | 1045567
prod_public_code | 1053489
public_code | 1043584
tenant | punzod8
site_url | preview.punzo.dhs.gov
stash_project | apunzo
env | testint
-----------
-----------
 List/Dict of Extra-Vars
-----------
* akamai_group- 43551
* akamai_path- 
* daily_db- test
* db_pass
* drupal_version- 8
* edit_code- 406338
* prod_edit_code- 406337
* prod_public_code- 406245
* public_code-406246
* tenant- mediad8
* edit_url- edit-preview-media.dhs.gov
* site_url- preview-media.dhs.gov
* stash_project- media
* env



Examples:
-------------
akamai_group: 115983
akamai_path: /183946/wcmdemo
daily_db: test
db_pass: Th!si5@t3st
drupal_version: 8
edit_code: 1043586
edit_url: edit-preview.punzo.dhs.gov
prod_edit_code: 1045567
prod_public_code: 1053489
public_code: 1043584
tenant: punzod8
site_url: preview.punzo.dhs.gov
stash_project: apunzo
env: testint

-------------
Tenant Onboarding
-------------
edit_url: edit-preview.punzo.dhs.gov
tenant: punzod8
site_url: preview.punzo.dhs.gov
stash_project: apunzo
env: testint


edit_url: edit-testint.punzo.dhs.gov
tenant: punzod8
site_url: testint.punzo.dhs.gov
env: testint



Tenant Onboarding: Migration to other environments (staging/production)
daily_db: stage
db_pass: Th!si5@t3st
edit_url: edit-preview.punzo.dhs.gov
tenant: punzod8
site_url: preview.punzo.dhs.gov
stash_project: apunzo
env: wcmlab_staging