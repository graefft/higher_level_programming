#!/bin/bash
#Takes in URL, sends request to URL, displays body of response
curl -s -L -X GET "$1"
