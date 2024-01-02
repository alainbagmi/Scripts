<?php
$databases['default']['default'] = array (
  'database' => '{{ tenant }}_prod',
  'username' => '{{ tenant }}_prod',
  'password' => '{{ db_pass }}',
  'host' => $_ENV['db_server'],
  'port' => $_ENV['db_port'],
  'driver' => 'mysql',
  'prefix' => '',
);

# REPLACE THIS SECTION WHEN TENANT GOES LIVE TO PROPER URL'S
#---- Trusted Host Pattern
#$settings['trusted_host_patterns'] = array(
#  '{{ url_escaped }}',
#);

#---- Memcache settings
$settings['memcache']['servers'] = [
    $_ENV['memcache_server1'] => 'default',
];
$settings['memcache']['bins'] = ['default' => 'default'];
$settings['memcache']['key_prefix'] = '{{ tenant }}';
$settings['cache']['default'] = 'cache.backend.memcache';
$settings['memcache']['stampede_protection'] = TRUE;

#---- File Paths
$settings['file_temp_path'] = '/var/www/sites-files/production.{{ tenant }}_gov_build/tmp';
$settings['file_private_path'] = '/var/www/sites-files/production.{{ tenant }}_gov_build/private';
$settings['file_public_path'] = 'sites/default/files';

#---- Drupal Hash Salt and Sync Directory
$settings['hash_salt'] = '{{ new_hash.stdout }}';
$settings["config_sync_directory"] = 'profiles/{{ tenant }}_gov/config/sync';

$config['image.settings']['allow_insecure_derivatives'] = TRUE;