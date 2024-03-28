#!/bin/bash
# a script that makes a request to url below that listens on port 5000, that causes the server to respond with a message "You got me!", in the body response
curl -sX PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me_3
