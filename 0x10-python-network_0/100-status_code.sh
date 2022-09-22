#!/bin/bash
# displays status code of response
curl -si "$1" | head -n1 | cut --delim=' ' --field=2
