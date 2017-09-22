#!/bin/bash

NAME="$1"
DIR="$2"

if [ "" = "$DIR" ]; then
	oc start-build $NAME
else
	oc start-build $NAME --from-dir=$SOURCE
fi