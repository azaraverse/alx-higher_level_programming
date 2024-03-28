#!/bin/bash
# a bash script that takes in the URL passed as an argument and displays all HTTP methods the server will accept
curl -s --head -X OPTIONS "$1" | grep -i '^allow' | awk '{print substr($0, index($0,$2))}'
