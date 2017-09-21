#!/bin/bash

SOURCE="$1"
NAME="$2"

pod="`oc get pods -lapp=app -o name | head`"

oc rsync --watch=true $SOURCE ${pod:5}:.