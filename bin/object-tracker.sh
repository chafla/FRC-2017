#! /bin/bash

export PYTHONPATH=${PYTHONPATH}:/home/pi/git/common-robotics:/home/pi/git/object-tracking
/home/pi/git/object-tracking/object_tracker.py --bgr "174, 56, 5" --width 400 --flip
