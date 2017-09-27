#!/bin/bash

SOURCE="$1"
TARGET="$2"

ARGS=""

json="`oc get secret $SOURCE -o json`"

keys="`echo "$json" | jq '.data | keys[]'`"

for name in $keys; do
	value="`echo "$json" | jq ".data[$name]"`"
	
	name="`echo "$name" | sed 's/-/_/g' | awk '{print toupper($0)}' | sed 's/"//g'`"
	value="`echo "$value" | sed 's/"//g' | base64 --decode`"

	ARGS="$ARGS $name=$value"
done

oc env dc $TARGET $ARGS