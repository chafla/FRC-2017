#! /bin/bash

source /home/pi/.profile
workon py2cv3
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics:~pi/git/object-tracking
python2 ~pi/git/FRC-2017/location_publisher.py --grpc raspi11.local --camera camera-gear-front --mqtt mqtt-turtle.local &> ~pi/git/FRC-2017/logs/gear-front-publisher.out &

