#!/bin/bash
#Takes in URL, displays all HTTP methods the server will accept
curl -siX OPTIONS "$1" | grep -i Allow | cut -d ' ' -f1 --complement
