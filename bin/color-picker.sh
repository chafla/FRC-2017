#! /bin/bash

echo "Starting Python 2.7 with OpenCV 3.1 bindings..."
source /home/pi/.profile
workon py2cv3
export PYTHONPATH=${PYTHONPATH}:/home/pi/git/common-robotics:/home/pi/git/object-tracking
/home/pi/git/object-tracking/color_picker.py -w 600
