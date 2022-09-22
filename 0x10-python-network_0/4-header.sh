#!/bin/bash
# sends a get request including a header
curl -s -H 'X-School-User-id: 98' "$1"
