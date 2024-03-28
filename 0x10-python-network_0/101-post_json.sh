#!/bin/bash
# sends a json POST request to a url and displays the body of the response. uses a file to send POST request
curl -sX POST -H "content-type: json" "$1" --data @"$2"
