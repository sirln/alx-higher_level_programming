#!/bin/bash
# Script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sH X-School-User-I:98 -X GET "$1"
