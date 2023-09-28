#!/bin/bash
#Send a file content
curl -s -H "Content-Type: application/json" -d "$(cat $2)" $1
