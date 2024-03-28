#!/bin/bash
# a bash script that takes in a URL, sends a GET request to that URL and displays the body of the response with a given header variable and value
curl -H "X-School-User-Id:98" -sLX GET "$1"
