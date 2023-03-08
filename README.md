# EE3080 DIP AY2022/2023
# MINDCUBER Project Using ev3dev2

## References
- The original MINDCUB3R code can be found at https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/MINDCUB3R/mindcuber.py.
- The twophase solver and GUI for 3x3 Cube can be found at https://github.com/hkociemba/RubiksCube-TwophaseSolver.
- The Optimal Solver can be found at https://github.com/hkociemba/RubiksCube-OptimalSolver.
- The solver and GUI for 2x2 Cube can be found at https://github.com/hkociemba/Rubiks2x2x2-OptimalSolver.
- The rubikscolorresolver from Dwalton can be found at https://github.com/dwalton76/rubiks-color-resolver.
- The rubikscolortracker from Dwalton for OpenCV features can be found at https://github.com/dwalton76/rubiks-cube-tracker.

## Prerequisite
***Unfortunately, this project is only supported by the Windows OS.***
- This project is run by changing the approach from running all the solver algorithms inside the EV3, to:
    - Using paho-MQTT for data communication.
    - Spawning an SSH connection to EV3 by **wexpect (Windows version of pexpect)** to remotely control EV3 to run files inside.
- Documentation for paho-MQTT can be found at https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php.
- Documentation for wexpect can be found at https://wexpect.readthedocs.io/en/latest/.
> If you want to run it on Ubuntu OS, you should **make changes to the SSH_Client.py file** to use the pexpect library.
- Documentation for pexpect can be found at https://pexpect.readthedocs.io/en/latest/.

## Overview:
- Regarding solving, we provide 3 modes of solving:
    - Solving the cube by Twophase solver.
    - Solving the cube by Optimal Solver.
    - Solving to specific patterns using cubestring (Inverse Solving).
    > Here is a comparison between the two algorithms:
    ![Algo_Comparison](/img/Algo_Comparison.png "Comparison")
- Regarding scanning, we provide 2 modes of scanning:
    - Traditional scanning by Ultrasonic Sensor.
    - Scanning by webcam using OpenCV.

## How to install
- Clone this repository.
- Preparation on EV3:
    - Create a new project on EV3 and then migrate the directory named "wecuber" into the EV3.
    - Make sure the sensors have been connected correctly.
    - Prepare the addition for flipper 2x2.
    - Spawn a Bluetooth connection to PC.
- Preparation on PC:
    - Install all the dependencies:
        ```
        pip install -r requirements.txt
        ```
    - Check the installed dependencies:
        ```
        pip freeze
        ```
    - Have your PC installed OpenSSH in Settings.
    
- Run the code:
    - After preparation, simply run the file ****
        ```
        python3 *filename*
        ```
## Miscellaneous
- The code for 2x2 cube is still under development and there is no stable version yet.
- So far, these modifications need to be done for 2x2:
    + Change scan_cube order (already did)
    Platform holder: no change needed. The shape is still cubic, so the topology is the same with 45 and 90 degrees movements. The sizing for the 2x2 cube is smaller, so the Hardware subteam helped out with designing a smaller platform with the same gear ratio to hold the smaller 2x2 cube.
    + Flipper arm: since my code instructs the flipper arm to “go all the way until stopped by an object”, it will still be able to touch the smaller 2x2 cube. Hardware team also helped to insert a horizontal bar at the flipper tip to hold the smaller 2x2 cube.
    + Color sensor motor: changes need to be made as now the code does not read “center tile, corner tile and edge tile” similar to the 3x3 cube anymore. The 2x2 rubik's cube now only has 4 corner tiles without any center nor edge tile. The matrix used to save the tile color values is also different in shape compared to the 3×3 cube.
    + Color sensor: no change, as there are still 6 same colors belonging to 6 faces of the cube.
    + Ultrasonic sensor: increase the distance between the sensor and the cube to 8cm, as the 2x2 cube is smaller so the distance should be larger.
