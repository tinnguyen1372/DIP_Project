#!/usr/bin/env python3

from mindcuber import MindCuber
import logging
import json
import sys
from rubikscolorresolver.solver import RubiksColorSolverGeneric
from subprocess import check_output

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
 
    #Step 2: Resolve Color
    cube = RubiksColorSolverGeneric(3)
    cube.enter_scan_data(mcube.colors)
    cube.crunch_colors()
    kociemaba_cube = cube.cube_for_kociemba_strict()

    #Step 3: Solve using TwoPhase

    cmd = ['kociemba', ''.join(map(str, kociemaba_cube))]
    log.info("Subprocessing Command: '%s'" % (' '.join(cmd)))
    solution = check_output(cmd).decode('ascii')

    if 'ERROR' in solution:
        msg = "kociemba returned the following error: '%s'" % (solution)
        log.error(msg)
        mcube.on_scan_error()
        if not scan_try:
            solve(1) 
        else:
            sys.exit(1)
            mcube.shutdown_robot()

    solution = solution.replace("'","3")
    log.info(solution)

    #Step 4: Solve
    mcube.flipper_hold_cube(100)
    try:
        mcube.resolve(solution)
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

# Operation Starts
solve(0)
