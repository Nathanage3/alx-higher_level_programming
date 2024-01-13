#!/bin/bash
#Write a Bash script that takes in a URL, sends a request
#to that URL, and displays the size of the body of the
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Use curl to send a request and display the size of the response body in bytes
response_size=$(curl -sI "$url" | awk '/Content-Length/ {print $2}' | tr -d '\r\n')

if [ -z "$response_size" ]; then
    echo "Failed to retrieve response size."
else
    echo "Size of the response body for $url is $response_size bytes."
fi
