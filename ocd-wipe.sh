#!/bin/bash

NAME="$2"

for name in $(oc get dc -o name -locdapp=`cat $HOME/.ocd/context`); do
  name=${name:18}
  oc delete secret $name
  oc delete pvc $name
done

oc delete all -locdapp=`cat $HOME/.ocd/context`
