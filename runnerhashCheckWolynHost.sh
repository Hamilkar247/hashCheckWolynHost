#!/bin/bash
REAL="$(dirname "$(realpath "$0")")"
echo "$REAL"
PATH="$REAL"/venv/bin:"$PATH"
python "$REAL"/hashCheckWolynHost.py "$@"
echo "python \"$REAL\"/runnerhashCheckWolynHost.sh.py \"$@\" "

