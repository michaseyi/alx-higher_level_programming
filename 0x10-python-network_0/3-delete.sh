#!/bin/bash
# displays all http methods the server will accept
curl -s "$1" | grep "Allow:" | cut --delim=' ' --field=2-

