#!/bin/bash

SOURCE="$1"
NAME="$2"

oc start-build $NAME --from-dir=$SOURCE