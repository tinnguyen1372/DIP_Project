#!/usr/bin/env python3

from mindcuber import MindCuber
import mqtt_comm as com
import logging
import json
import sys



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
    mcube.wait_for_cube_insert()

    # Push the cube to the right so that it is in the expected
    # position when we begin scanning
    mcube.flipper_hold_cube(100)
    mcube.flipper_away(100)

    #Step 1: Scan
    mcube.scan()
    scan_result_as_string = str(json.dumps(mcube.colors))

    #Step 2: Generate solution
    result = com.send_to_pc(scan_result_as_string)

    #Step 3: Solve
    mcube.flipper_hold_cube(100)
    try:
        mcube.resolve(result)
    except:
        if not scan_try:
            mcube.on_scan_error()
            log.info("Scan Error /n Scanning Again...")
            solve(1)            
        else:
            log.info("Scan Error /n System Terminating...")
            mcube.shutdown_robot()
            sys.exit(1)


        mcube.shutdown_robot()

    # except Exception as e:
    #     log.exception(e)
    #     mcube.shutdown_robot()
    #     sys.exit(1)

solve(0)
