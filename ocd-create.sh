#!/bin/bash

TYPE="$1"
NAME="$2"
SRC="$3"

[ "" = "$NAME" ] && NAME=$TYPE

if [ "" = "$DIR" ]; then
	oc new-app $TYPE --name $NAME -locdapp=`cat $HOME/.ocd/context`
else
	oc new-app $TYPE~$SRC --name $NAME -locdapp=`cat $HOME/.ocd/context`
fi