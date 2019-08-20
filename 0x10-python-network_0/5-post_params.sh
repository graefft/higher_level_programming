#!/bin/bash
#Takes in URL, sends POST request and displays body of response 
curl -s -X POST "$1" -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
