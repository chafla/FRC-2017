#!/usr/bin/env python3

import argparse
import logging
import socket
import time
from threading import Thread
import serial
from sys import exit

import paho.mqtt.client as paho
from common_constants import LOGGING_ARGS
from common_utils import mqtt_broker_info
from common_utils import is_windows


CLIENT = "client"

TOLERANCE_THRESH = 15


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: {0}".format(rc))
    Thread(target=publish_messages, args=(client, userdata)).start()


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code: {0}".format(rc))


def on_publish(client, userdata, mid):
    print("Published value to {0} with message id {1}".format(userdata["topic"], mid))


def publish_messages(client, userdata):
    total_sum = 0
    total_count = 0

    port = userdata["port"]

    # Init connection to serial port
    try:
        ser = serial.Serial(port=port, baudrate=115200)
    except serial.serialutil.SerialException as e:
        ser = None
        print(e)
        exit(0)

    try:
        while True:
            try:
                bytes = ser.readline()
                s = bytes.decode("utf-8")
                mm = int(s)
                print(mm)
                if mm < 0:  # out of range, get fresh data so it doesn't mess with averages
                    total_sum = 0
                    total_count = 0
                elif (total_sum + total_count == 0) or abs((total_sum / total_count) - mm) < TOLERANCE_THRESH:
                    total_sum += mm
                    total_count += 1
                else:
                    mm_enc = str(mm).encode("utf-8")
                    client.publish("{}/mm".format(userdata["topic"]),
                                   payload=mm_enc,
                                   qos=0)
                    total_sum = 0 + mm
                    total_count = 1

                time.sleep(0.5)

            except BaseException as e:
                print(e.__class__.__name__, e)
                time.sleep(1)

    finally:
        ser.close()


if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mqtt", required=True, help="MQTT broker hostname")
    parser.add_argument("-s", "--serial", required=True, help="Serial port", default="ttyACM0")
    parser.add_argument("-d", "--device", required=True, help="Device name (lidar_l or lidar_r")
    args = vars(parser.parse_args())

    port = ("" if is_windows() else "/dev/") + args["serial"]

    # Init connection to serial port

    # Setup logging
    logging.basicConfig(**LOGGING_ARGS)

    # Create userdata dictionary
    userdata = {"topic": args["device"], "port": port}

    # Initialize MQTT client
    client = paho.Client(userdata=userdata)

    # Add client to userdata
    userdata[CLIENT] = client

    # Setup MQTT callbacks
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    # Determine MQTT broker details
    mqtt_hostname, mqtt_port = mqtt_broker_info(args["mqtt"])

    try:
        # Connect to MQTT broker
        logging.info("Connecting to MQTT broker {0}:{1}...".format(mqtt_hostname, mqtt_port))
        client.connect(mqtt_hostname, port=mqtt_port, keepalive=60)
        client.loop_forever()
    except socket.error:
        logging.error("Cannot connect to MQTT broker {0}:{1}".format(mqtt_hostname, mqtt_port))
    except KeyboardInterrupt:
        pass

    print("Exiting...")
