#!/bin/bash
# sends json to server
 curl -H 'Content-Type: application/json' -X POST --data "@$2" "$1"
