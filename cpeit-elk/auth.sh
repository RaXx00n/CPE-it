#!/bin/bash

# Run the elasticsearch-create-enrollment-token command
output=$(./elasticsearch-create-enrollment-token --url https://127.0.0.1:9200 -s kibana)

# Extract the token from the output
token=$(echo $output | grep -oP 'enrollment_token":"\K[^"]+')

# Open Firefox and navigate to the Kibana endpoint
firefox https://your-kibana-url

# Wait for Kibana to load
sleep 10

# Enter the token into the Kibana UI
xdotool type "$token"
xdotool key Return

