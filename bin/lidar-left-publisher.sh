#! /bin/bash

source ~pi/.profile
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics:~pi/git/object-tracking:~pi/git/common-utils:~pi/git/common-constants
python3 ~pi/git/FRC-2017/lidar_publisher.py --mqtt mqtt-turtle.local --lidar lidar_l --port ttyACM0 &> ~pi/git/FRC-2017/logs/lidar-left-publisher.out &

