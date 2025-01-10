#!/bin/sh

# sequential
# echo "Starting tuya2mqtt.py"
# python3 tuya2mqtt.py

echo "Starting scripts in parallel"
python3 tuya2mqtt.py &

# Wait for all background jobs to complete
wait
echo "All scripts completed"
