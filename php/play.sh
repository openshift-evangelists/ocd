#!/bin/bash

ocd app sample

ocd create php frontend https://github.com/openshift-demos/php-sample.git

# oc get dc
# oc get build
# oc get pods

ocd create mysql db

# oc get dc
# oc get pods

ocd url add frontend

# Check the url from browser

ocd link db frontend

# Check the env vars in browser (bottom of the phpinfo() page)

ocd sync frontend

# Edit the index.php and something before the PHP code and wait for sync
# Reload the page in the browser

ocd scale frontend 2

# Use curl to the the web page, should be switching between the origin and edited

ocd destroy db

#oc get all -lapp=db
#oc get pvc
#oc get secret

ocd wipe

# oc get dc
# oc get build
# oc get pods

ocd exit