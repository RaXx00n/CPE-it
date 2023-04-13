#!/bin/bash

# Run the elasticsearch-create-enrollment-token command
token=$(./elasticsearch-create-enrollment-token --url https://127.0.0.1:9200 -s kibana)

# Copy the token to the clipboard
echo $token | pbcopy

# Open Kibana and wait for it to load
open http://localhost:5601
echo "Waiting for Kibana to load..."
sleep 30

# Get the name of the frontmost browser window
browser=$(osascript -e 'tell application "System Events" to get name of first process whose frontmost is true')

# Enter the token into the browser
echo "Entering token into $browser..."
osascript -e 'tell application "System Events" to keystroke "a" using {command down}'
osascript -e 'tell application "System Events" to keystroke "'"$token"'"'
osascript -e 'tell application "System Events" to keystroke return'
