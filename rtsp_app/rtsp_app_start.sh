#!/bin/sh
set -e  # Exit the script if any command fails

echo "Starting rtsp_app.py"
python3 rtsp_app.py
if [ $? -ne 0 ]; then
    echo "rtsp_app.py failed"
    exit 1
fi

echo "Starting mqtt2rtsp.py"
python3 mqtt2rtsp.py
if [ $? -ne 0 ]; then
    echo "mqtt2rtsp.py failed"
    exit 1
fi
