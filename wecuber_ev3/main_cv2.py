#!/usr/bin/env python3

from mindcuber import MindCuber
import mqtt_comm as com
import logging
import json
import sys
import time


# logging.basicConfig(filename='rubiks.log',
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))


def solve(scan_try):
    # try
    mcube = MindCuber()

    #Step 2: Generate solution
    log.info("2x2x2 solver")
    result = com.send_to_pc("CVSCAN2")
    time.sleep(2)
    mcube.wait_for_cube_insert()

    #Step 3: Solve
    mcube.flipper_hold_cube(100)
    try:
        mcube.resolve(result)
    except:
        if not scan_try:
            log.info("Scan Error /n Scanning Again...")
            solve(1)            
        else:
            log.info("Scan Error /n System Terminating...")
            mcube.shutdown_robot()
            sys.exit(1)


        mcube.shutdown_robot()
solve(0)
