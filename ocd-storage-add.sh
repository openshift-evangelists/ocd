#!/bin/bash

TYPE="$1"
SIZE="$2"
TARGET="$3"
NAME="$4"


[ "shared" = "$TYPE" ] && CLS="ReadWriteMany"
[ "local" = "$TYPE" ] && CLS="ReadWriteOnce"

cat <<EOF | oc create --dry-run=true -f -
apiVersion: "v1"
kind: "PersistentVolumeClaim"
metadata:
  name: $NAME
spec:
  accessModes:
    - $CLS
  resources:
    requests:
      storage: ${SIZE}Gi
  volumeName: $NAME
EOF


oc volume dc $NAME --add --type=persistentVolumeClaim --mount-path=$TARGET --claim-name=$NAME