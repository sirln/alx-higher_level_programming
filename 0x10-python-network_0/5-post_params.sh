#!/bin/bash
# Script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
