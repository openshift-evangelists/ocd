#!/bin/bash

NAME="$1"

oc delete all -lapp=$NAME
oc delete pvc $NAME
oc delete secret $NAME