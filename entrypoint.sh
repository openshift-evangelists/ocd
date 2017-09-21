#!/bin/bash

export SRC="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

mkdir -p $HOME/.ocd

export PROJECT='$(oc project -q)'
export CONTEXT='$([ -f $HOME/.ocd/context ] && echo "/`cat $HOME/.ocd/context`")'

alias ocd='$SRC/ocd.sh'

export PS1="[$PROJECT$CONTEXT] $PS1"