#! /bin/bash

export PYTHONPATH=${PYTHONPATH}:../common-robotics
./location_publisher.py --grpc raspi11.local --camera camera-gear-front --mqtt mqtt.local

