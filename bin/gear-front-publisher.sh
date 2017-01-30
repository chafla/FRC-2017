#! /bin/bash

export PYTHONPATH=${PYTHONPATH}:../common-robotics:../object-tracking
/home/pi/git/FRC-2017/location_publisher.py --grpc raspi11.local --camera camera-gear-front --mqtt mqtt-turtle.local

