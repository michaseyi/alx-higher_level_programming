#!/usr/bin/env bash
# displays the size of the body of response received
curl -s "$1" | wc -c