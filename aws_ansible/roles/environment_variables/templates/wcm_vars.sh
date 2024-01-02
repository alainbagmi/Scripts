#!/bin/bash

# Memcache Vars
{% for item in MEMCACHED_SERVERS%}
export memcache_server{{ loop.index }}={{ item }}
{% endfor %}

# DB Vars
export db_server={{ DB_SERVER }}
export db_port={{ DB_PORT }}

# Proxy Vars
export proxy_server={{ PROXY_SERVER }}

# Solar Vars
export solr_server={{ SOLR_SERVER }}
