#!/bin/bash
# sends json to server
 curl -s -H 'Content-Type: application/json' --data "@$2" "$1"
