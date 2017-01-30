#! /bin/bash

export PYTHONPATH=${PYTHONPATH}:../common-robotics:../object-tracking
./object_tracker.py --bgr "174, 56, 5" --width 400 --flip
