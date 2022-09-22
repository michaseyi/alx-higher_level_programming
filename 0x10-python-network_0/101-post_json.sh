#!/bin/bash
# sends json to server
 curl -H 'Content-Type: application/json' --data-binary "@kk" "$1"
 