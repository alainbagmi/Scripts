<?php
$databases['default']['default'] = array (
  'database' => '{{ tenant }}_stage',
  'username' => '{{ tenant }}_stage',
  'password' => '{{ dbpass }}',
  'host' => $_ENV['db_server'],
  'port' => $_ENV['db_port'],
  'driver' => 'mysql',
  'prefix' => '',
);

#---- Trusted Host Pattern
$settings['trusted_host_patterns'] = array(
   '{{ url_escaped }}',
);

#---- Memcache settings
$settings['memcache']['servers'] = [
    $_ENV['memcache_server1'] => 'default',
    $_ENV['memcache_server2'] => 'default',

];
$settings['memcache']['bins'] = ['default' => 'default'];
$settings['memcache']['key_prefix'] = '{{ tenant }}';
$settings['cache']['default'] = 'cache.backend.memcache';
$settings['memcache']['stampede_protection'] = TRUE;

#---- File Paths
#$config['system.file']['path']['temporary']  = '/var/www/sites-files/staging.{{ tenant }}_gov_build/tmp';
$settings['file_temp_path'] = '/var/www/sites-files/testint.{{ tenant }}_gov_build/tmp';
$settings['file_private_path'] = '/var/www/sites-files/staging.{{ tenant }}_gov_build/private';
$settings['file_public_path'] = 'sites/default/files';

#---- Drupal Hash Salt and Sync Directory

$settings['hash_salt'] = '{{ new_hash.stdout}}';
$settings['config_sync_directory'] = 'profiles/{{ tenant }}_gov/config/sync';


$settings['http_client_config']['proxy']['http'] = 'http://' . $_ENV['proxy_server'] . ':8080';
$settings['http_client_config']['proxy']['https'] = 'http://' . $_ENV['proxy_server'] . ':8080';
$settings['http_client_config']['proxy']['no'] = ['127.0.0.1', 'localhost', 'rpc.acquia.com', 'nspi.acquia.com', 'HQWCMPUT7ES01', 'HQWCMPUS7ES01', 'HQWCMPUP7ES01', 'HQWCMPUP7ES02'];
