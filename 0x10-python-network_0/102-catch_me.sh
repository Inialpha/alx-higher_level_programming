#!/bin/bash
#A bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sL -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
