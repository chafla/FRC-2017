#! /bin/bash

export PYTHONPATH=${PYTHONPATH}:../common-robotics:../object-tracking
./location_publisher.py --grpc raspi11.local --camera camera-gear-front --mqtt mqtt-turtle.local

