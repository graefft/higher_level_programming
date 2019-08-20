#!/bin/bash
#Takes in URL, sends DELETE request to URL, displays body of response
curl -s -L -X DELETE "$1"
