#!/bin/bash
#Write a Bash script that takes in a URL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
