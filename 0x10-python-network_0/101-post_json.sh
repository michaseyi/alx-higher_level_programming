#!/bin/bash
# sends json to server
 curl -H 'Content-Type: application/json' --data-binary @"$2" "$1"
