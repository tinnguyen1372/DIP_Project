# EE3080 DIP AY2022/2023
# MINDCUBER Project Using ev3dev2

## References
-   The original MINDCUB3R code at https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/MINDCUB3R/mindcuber.py
-   The twophase solver and GUI for 3x3 Cube at https://github.com/hkociemba/RubiksCube-TwophaseSolver
-   The solver and GUI for 2x2 Cube at https://github.com/hkociemba/Rubiks2x2x2-OptimalSolver
-   The rubikscolorresolver from Dwalton at https://github.com/dwalton76/rubiks-color-resolver
-   The rubikscolortracker for OpenCV features at https://github.com/dwalton76/rubiks-cube-tracker

## Prerequisite
-   This project is running by instead of running all the solver algorithm inside the EV3, we change to:
    -   Using paho-MQTT for data communication
    -   Spawning SSH connection to EV3 by **wexpect (Windows version of pexpect)** for remotely controlling EV3 to run file inside
-   wexpect is the library to spawn command on Windows terminal, using to spawn SSH connection to EV3. Unfortunately, this project only support the Windows OS, if you want to make it run on Ubuntu OS, should **make change on the SSH_Client.py file** to the pexpect library. 
-   Documentation of paho-MQTT: https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php
-   Documentation of wexpect: https://wexpect.readthedocs.io/en/latest/
-   Documentation of pexpect: https://pexpect.readthedocs.io/en/latest/

## How to install
-   Git clone this repo
-   Preparation on EV3:
    -   Create a new project on EV3 and then migrate the directory name wecuber into the EV3
    -   Make sure the sensors have been connected correctly
    -   Prepare the addition for flipper 2x2 
    -   Spawn Bluetooth connection to PC
-   Preparation on PC:
    -   Install all the dependencies
        ```.bash
        pip install -r requirements.txt
        ``` 
    -   Check the dependencies installed:
        ```.bash
        pip freeze
        ```
    -   Have your PC installed OpenSSH in Settings
    
- Run the code:
    -   After preparation, simply run the file ****
        ```.bash
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
