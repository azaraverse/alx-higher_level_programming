#!/bin/bash
# sends a request to a URL passed as an arg and displays the status code of the response only
curl -so /dev/null -w "%{http_code}" "$1"
