#!/bin/sh
# sequential
# echo "Starting ipcam.py"
# python3 ipcam.py
# echo "Starting ipcam_no-windows.py"
# python3 ipcam_no-windows.py
# echo "Starting mqtt2rtsp.py"
# python3 mqtt2rtsp.py

echo "Starting scripts in parallel"
# python3 ipcam.py &
python3 ipcam_no-windows.py &
python3 mqtt2rtsp.py &

# Wait for all background jobs to complete
wait
echo "All scripts completed"
