#!/bin/bash

COUNT="$1"
NAME="$2"

oc scale dc $NAME --replicas=$COUNT