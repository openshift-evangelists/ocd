#!/bin/bash

NAME="$1"
SOURCE="$2"

[ "" = "$SOURCE" ] && SOURCE="."

pod="`oc get pods -lapp=$NAME -o name | head`"

oc rsync --watch=true $SOURCE ${pod:5}:.