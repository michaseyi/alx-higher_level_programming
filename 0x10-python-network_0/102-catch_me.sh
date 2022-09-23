#!/bin/bash
# causes server to respond with "You got me!"
curl -s -L -H 'Origin: School' -d "user_id=98" -X PUT 0.0.0.0:5000/catch_me
