#!/bin/bash
# a bash script that takes in the URL passed as an argument and displays all HTTP methods the server will accept
curl -s --head "$1" | grep -i Allow | awk '{print $2, $3, $4}'
