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
***This project is only supported by the Windows OS.***
- Follow the instruction here: https://www.ev3dev.org/docs/getting-started/ in order to install ev3dev for the EV3 brick. ev3dev is a Debian Linux OS that runs on the LEGO® MINDSTORMS EV3
- Install the LEGO® MINDSTORMS® EV3 MicroPython extension on VS Code
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
    - Solving to specific patterns.
    > Here is a comparison between the two algorithms:
    ![Algo_Comparison](/img/Algo_Comparison.png "Comparison")
- Regarding scanning, we provide 2 modes of scanning:
    - Traditional scanning by Ultrasonic Sensor.
    - Scanning by webcam using OpenCV.

## How to install
- Clone this repository.
- Preparation on EV3:
    - Create a new project on EV3 and then migrate the directory named "wecuber" into the EV3 (either via SSH or VS Code).
    - Make sure the sensors and motors have been connected correctly.
    - Prepare the additional parts for flipper 2x2.
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
## 2x2x2 Solving
- These modifications has been done for 2x2:
    + Platform holder: Designed and 3D printed a smaller platform adapter to hold the smaller 2x2 cube.
    + Flipper arm: The flipping motion worked just fine. Minor additional parts have been added to block the upper layer from moving when doing rotate_cube_blocked actions
    + Color sensor motor: not used, instead the cube is scanned using computer vision
    + Ultrasonic sensor: no change
    + Solving algorithm: Used the Optimal 2x2 solver algorithm to solve the cube.
