#!/bin/bash

# This script uses curl to test GET and POST requests to this application.
# To test GET requests: ./test.sh GET
# To test POST requests: ./test.sh POST '{"phrase": "<phrase>"}'
# Eg. ./test.sh POST '{"phrase": "small suns"}'

PORT=8080
HOST="http://localhost:"${PORT}


if [ "$1" == "GET" ]; then
	curl --request GET ${HOST}"/read"
else
	curl --request POST --header "Content-type: application/json" \
	     --data "$2" ${HOST}"/write"
fi
