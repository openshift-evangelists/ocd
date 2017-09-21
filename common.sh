#!/bin/bash

function subcommand() {
	ARGS=( "$@" )
	PREFIX="${ARGS[0]}"
	SUB="${ARGS[1]}"
	REST=("${ARGS[@]:2}")

	$SRC/ocd-${PREFIX}${SUB}.sh "${REST[@]}"
}