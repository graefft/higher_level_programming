#!/bin/bash
#Takes in URL, displays all HTTP methods the server will accept
curl -siX OPTIONS 0.0.0.0:5000/route_4 | grep -i Allow | cut -d ' ' -f1 --complement
