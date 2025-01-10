#!/bin/sh
set -e  # Exit the script if any command fails

echo "Starting tuya2mqtt.py"
python3 tuya2mqtt.py
if [ $? -ne 0 ]; then
    echo "tuya2mqtt.py failed"
    exit 1
fi
