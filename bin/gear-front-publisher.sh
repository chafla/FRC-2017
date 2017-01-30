#! /bin/bash

export PYTHONPATH=${PYTHONPATH}:/home/pi/git/common-robotics:/home/pi/git/object-tracking
/home/pi/git/FRC-2017/location_publisher.py --grpc raspi11.local --camera camera-gear-front --mqtt mqtt-turtle.local

