#!/usr/bin/env python3
"""Make BALANC3R robot stay upright."""

import logging
import time
from ev3dev2.control.GyroBalancer import GyroBalancer, GracefulShutdown
from ev3dev2.sensor.lego import InfraredSensor

# Logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)
log.info("Starting Balanc3rBaseline")

# Infrared remote
remote = InfraredSensor()
remote.mode = remote.MODE_IR_REMOTE

# Balance robot
robot = GyroBalancer()
robot.balance()

try:
    # Wait for user to terminate program
    while True:
        time.sleep(0.5)

except (GracefulShutdown, Exception) as e:
    log.exception(e)
    # Exit cleanly so that all motors are stopped
    robot.shutdown()

log.info("Exiting Balanc3rBaseline")
