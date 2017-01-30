#! /bin/bash

echo "Starting Python 2.7 with OpenCV 3.1 bindings..."
source /home/pi/.profile
workon py2cv3
export PYTHONPATH=${PYTHONPATH}:/home/pi/git/common-robotics:/home/pi/git/object-tracking
/home/pi/git/object-tracking/object_tracker.py --bgr "174, 56, 5" --width 400 --flip
