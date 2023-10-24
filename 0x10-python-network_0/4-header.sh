#!/bin/bash
#A Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -s -X GET -H "X-School-User-Id: 98" $1
