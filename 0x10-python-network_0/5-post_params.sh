#!/bin/bash
# a bash script that takes in a URL, sends a POST request to that URL and displays the body of the response with a given variable and value
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -sX POST "$1"
