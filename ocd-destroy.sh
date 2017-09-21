#!/bin/bash

NAME="$2"

oc delete all -lapp=$NAME
oc delete pvc $NAME
oc delete secret $NAME