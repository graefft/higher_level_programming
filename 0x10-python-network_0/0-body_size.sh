#!/bin/bash
#Takes in URL, sends request to URL, displays size of body of response
LENGTH=$(curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2)
echo "$LENGTH"
