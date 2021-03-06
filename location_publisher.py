#!/usr/bin/env python2

import logging
from logging import info
from threading import Thread

import common_cli_args  as cli
from common_cli_args import setup_cli_args
from common_constants import CAMERA_NAME
from common_constants import LOGGING_ARGS
from common_utils import mqtt_broker_info
from common_utils import sleep
from location_client import LocationClient
from mqtt_connection import MqttConnection

if __name__ == "__main__":
    # Parse CLI args
    args = setup_cli_args(cli.grpc, cli.mqtt, cli.camera)

    # Setup logging
    logging.basicConfig(**LOGGING_ARGS)

    # Start location reader
    locations = LocationClient(args["grpc"]).start()


    # Define MQTT callbacks
    def on_connect(client, userdata, flags, rc):
        info("Connected to MQTT broker with result code: {0}".format(rc))
        Thread(target=publish_locations, args=(client, userdata)).start()


    def on_disconnect(client, userdata, rc):
        info("Disconnected from MQTT broker with result code: {0}".format(rc))


    def on_publish(client, userdata, mid):
        print("Published message id: {0}".format(mid))


    def publish_locations(client, userdata):
        while True:
            x_loc = locations.get_x()
            if x_loc is not None:
                result, mid = client.publish("{0}/x".format(userdata[CAMERA_NAME]),
                                             payload="{0}:{1}".format(x_loc[0], x_loc[1]).encode('utf-8'))


    # Setup MQTT client
    hostname, port = mqtt_broker_info(args["mqtt"])
    mqtt_conn = MqttConnection(hostname, port, userdata={CAMERA_NAME: args["camera"]})
    mqtt_conn.client.on_connect = on_connect
    mqtt_conn.client.on_disconnect = on_disconnect
    mqtt_conn.client.on_publish = on_publish
    mqtt_conn.connect()

    try:
        sleep()
    except KeyboardInterrupt:
        pass
    finally:
        mqtt_conn.disconnect()
        locations.stop()

    print("Exiting...")
