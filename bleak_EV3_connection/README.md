# Connect from Hub to PC using bleak

This directory contains implementation to transmit data between Hub and PC. There are two algorithms to choose, two-phase Kociemba with small solving time but not optimal in moves, and Korf's algo with optimal solution moves (typically 18, never exceed 20) but takes a lot of time

Steps to run:

1. Download and cd to this bleak_EV3_connection folder

2. Run `pip install -r requirements.txt`

3. On the hub terminal, run `python client.py`

4. On the PC terminal, choose algorithm (Kociemba/Korf) you want to use and run the file accordingly. It can be `python server-improved_Korf.py` or `python server-twoPhase_Kociemba.py`
