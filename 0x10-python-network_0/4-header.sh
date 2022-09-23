#!/bin/bash
# sends a get request including a header
curl -s -H "X-School-User-Id: 98" -X GET "$1"
