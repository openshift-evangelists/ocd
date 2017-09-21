#!/bin/bash

source $SRC/common.sh

export CONTEXT='$([ -f $HOME/.ocd/context ] && echo "/`cat $HOME/.ocd/context`")'

subcommand "" $@