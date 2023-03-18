# EE3080 DIP AY2022/2023

# MINDCUBER Project Using ev3dev2

## References

- The original MINDCUB3R code can be found at https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/MINDCUB3R/mindcuber.py.
- The twophase solver and GUI for 3x3 Cube can be found at https://github.com/hkociemba/RubiksCube-TwophaseSolver.
- The Optimal Solver can be found at https://github.com/hkociemba/RubiksCube-OptimalSolver.
- The solver and GUI for 2x2 Cube can be found at https://github.com/hkociemba/Rubiks2x2x2-OptimalSolver.
- The rubikscolorresolver from Dwalton can be found at https://github.com/dwalton76/rubiks-color-resolver.
- The rubikscolortracker from Dwalton for OpenCV features can be found at https://github.com/dwalton76/rubiks-cube-tracker.
- The a webcam-based 3x3x3 rubik's cube from kkoomen for OpenCV features can be found at https://github.com/kkoomen/qbr.

## Prerequisite of installation

**_This project is only supported by the Windows OS._**

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
    
- Regarding scanning, we provide 2 modes of scanning:
  - Traditional scanning by Color Sensor.
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
  - After preparation, simply run the file \*\*\*\*
    ```
    python3 wecuber_GUI.py
    ```

## Introduction:

This project is a part of Design & Innovation Project (DIP) at School of Electrical & Electronic Engineering at NTU. The problem statement includes solving the rubik cube (3x3x3) using robots arms built from LEGO® MINDSTORMS® EV3. The additional requirements for this project is to solve the 2x2x2 rubik with the same setup.

## Materials and Equipment

To run this project, we use:

- LEGO® MINDSTORMS® hardware
- EV3 (the robot's "brain")
- A Python backend API to handle the wireless data communication between PC and EV3
- A Python backend API to handle the solving of rubiks using different algorithms, with the use of Computer Vision for scanning
- A Graphical User Interface (GUI) for better user experience

## Hardware & Software Architecture

// include images of the robot and the software diagram

## Results

- We managed to calibrate & develop the robot to solve the rubik's cube (3x3x3) in one minute on average. The number of moves would never exceed 20.
- We have created a separate program and different calibration to solve the 2x2x2 rubik successfully with the same hardware setup
- We have also developed new features that support the scanning and user experience (Computer Vision + GUI). This will be covered in detail in next part.

## New features

### 1. Better architecture: Client-server system architecture

![Client-server](/img/pc_and_ev3.png 'Client-server')

We have managed to decouple the solving algorithm from the EV3, and move it to the separate device like laptop. The EV3's responsibilities now only include rubik scanning, communicating with the laptop and controlling robot's movement based on the instructions given.

Meanwhile, the laptop will act as a server, which will run the solving algorithm(s) based on scanning results and return the instruction to the EV3.

This architecture is better than the normal one, where the EV3 will do all the work of scanning, running algorithm and control the robot's movement. Since the processor of EV3 is not as strong as the laptop's one, it would take long time to run the algorithms, especially the more complicated one - Korf's algorithm

### 2. Higher solving's success rate, less time spent on the process

We have spent a lot of time on calibrating the hardware by changing the physical and logical aspect. This includes choosing appropriate parameters for displacement, speed and position of each robot's movement to ensure best accuracy and performance. Hence, we are proud to say our success rate is close to 100% after multiple tries.

### 3. More optimal algorithms to choose from: Kociemba and Korf's algorithm

We have developed, modified and integrated successfully two rubik's solving algorithm:

- Kociemba's Two phase algorithm: Kociemba’s algorithm identifies a subset of 20 billion positions, called H. Reid showed that every position in this subset is solvable in at most 18 moves, and further that every cube position is at most 12 moves from this subset. Phase one finds a move sequence that takes an arbitrary cube position to some position in the subset H, and phase two finds a move sequence that takes this new position to the fully solved state.

- Korf's optimal algorithm: Richard Korf’s algorithm can solve any scrambled cube in 20 moves or fewer. It works by searching for solutions using an iterative-deepening depth-first search combined with A* (IDA*). Iterative-deepening depth-first search (IDDFS) is a tree-traversal algorithm. Like a breadth-first search (BFS), IDDFS is guaranteed to find an optimal path from the root node of a tree to a goal node, but it uses less memory than a BFS.

- Comparison between two algorithm:

Generally, Korf's solution will be less than the Kociemba's Two phase algorithm, but the time it takes to get the solution is considerably larger.

> Here is a comparison between the two algorithms:
> ![Algo_Comparison](/img/Algo_Comparison.png 'Comparison')

### 4. Better user experience: Developed Graphical User Interface

We have developed a graphical user interface so that the user could use our application easier, without the need to touch the command line or terminal.

![GUI_Screenshot](/img/GUI_Screenshot.png 'GUI')

### 5. Unique feature: Solving to specific patern

You also have the possibility to solve a cube not to the solved position but to some favorite pattern you want. This feature is already integrated successfully with the GUI.

### 6. Modification for 2x2x2 rubik solving

- These modifications have been done for 2x2:
  - Platform holder: Designed and 3D printed a smaller platform adapter to hold the smaller 2x2 cube.
  - Flipper arm: The flipping motion worked just fine. Minor additional parts have been added to block the upper layer from moving when doing rotate_cube_blocked actions
  - Color sensor motor: not used, instead the cube is scanned using computer vision
  - Ultrasonic sensor: no change
  - Solving algorithm: Used the Optimal 2x2 solver algorithm to solve the cube.

### 7. Computer Vision: faster scanning instead of Color Sensor

To detect the current state of the Rubik's Cube, this solver uses two Python libraries that integrate with OpenCV. These libraries provide a robust and efficient way to detect the current state of the Rubik's Cube using computer vision techniques.

The Rubik's Cube solver includes two submodules for OpenCV integration: one for 3x3 cube scanning and one for 2x2 cube scanning. Both submodules can be found in the repository.

To use the OpenCV integration in this Rubik's Cube solver, you can follow these steps:

1. Run the solver script and use the OpenCV integration to detect the current state of the Rubik's Cube.
2. Once the state of the Rubik's Cube is detected, the solver will generate a solution to the Rubik's Cube.

The OpenCV integration in this solver provides an efficient and accurate way to detect the current state of the Rubik's Cube, making it possible to solve Rubik's Cubes of different sizes.
