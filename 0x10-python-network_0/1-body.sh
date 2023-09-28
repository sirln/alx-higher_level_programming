#!/bin/bash
# Script that takes in a URL, sends a `GET` request to the URL,
# and displays the body of the response

URL=$1
STATUS_CODE=$(curl -o /dev/null -s -w '%{http_code}' "$URL")

if [ "$STATUS_CODE" -eq 200 ]; then
	curl -sLX GET "$URL"
fi
