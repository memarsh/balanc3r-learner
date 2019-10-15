#!/usr/bin/env python3
"""Make BALANC3R robot stay upright using reinforcement learning."""

import logging
import time
from BalancerLearner import BalancerLearner
from ev3dev2.control.GyroBalancer import GracefulShutdown
from ev3dev2.sensor.lego import InfraredSensor

# Logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)
log.info("Starting Balanc3rLearner")

# Balance robot
robot = BalancerLearner(debug=True)
robot.balance()

try:
    # Wait for user to terminate program
    while True:
        time.sleep(0.5)

except (GracefulShutdown, Exception) as e:
    log.exception(e)
    # Exit cleanly so that all motors are stopped
    robot.shutdown()

log.info("Exiting Balanc3rLearner")
