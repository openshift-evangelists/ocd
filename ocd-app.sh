#!/bin/bash

NAME="$1"

echo "$NAME" > $HOME/.ocd/context

oc project -q 2>&1 > /dev/null

[ 1 == $? ] && oc new-project $NAME