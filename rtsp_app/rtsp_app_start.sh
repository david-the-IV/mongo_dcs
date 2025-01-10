#!/bin/sh
set -e  # Exit the script if any command fails

# echo "Starting ipcam.py"
# python3 ipcam.py
# if [ $? -ne 0 ]; then
#     echo "ipcam.py failed"
#     exit 1
# fi

echo "Starting ipcam_no-windows.py"
python3 ipcam_no-windows.py
if [ $? -ne 0 ]; then
    echo "ipcam_no-windows.py failed"
    exit 1
fi

echo "Starting mqtt2rtsp.py"
python3 mqtt2rtsp.py
if [ $? -ne 0 ]; then
    echo "mqtt2rtsp.py failed"
    exit 1
fi
