#!/usr/bin/env python3
import twophase.solver as twophase
# import optimal.solver as korf
from rubikscube2x2solver import solver as sv2x2

def solve(max_length, time_out, cubestring, method, goalstring):
    print("Recieved scramble from EV3: {}".format(cubestring))
    print('Solving...')
    solution = ""
    if (method == 1): # Two phase algorithm
        if len(cubestring) == 54:
            solution = twophase.solve(cubestring,max_length,time_out)
            solution = solution[:solution.strip().rfind('(')]
        elif len(cubestring) == 24:
            solution = sv2x2.solve(cubestring)
            solution = solution[:solution.strip().rfind('(')]
        print("Result from Kociemba method: {}".format(solution))
    elif method == 2: # Korf algorithm
        # solution = korf.solve(cubestring)
        # solution = solution[:solution.strip().rfind(" ")]
        solution = twophase.solve(cubestring,max_length,time_out)
        solution = solution[:solution.strip().rfind('(')]
        print("Result from Kociemba method: {}".format(solution))
    elif method == 3: # SolveTo using two phase algorithm
        print("Trying to solve to: {}".format(goalstring))
        print(len(goalstring))
        solution = twophase.solveto(cubestring, goalstring)
        solution = solution[:solution.strip().rfind('(')]
        print("Result from solveto method: {}".format(solution))
    # print(solution)
    return solution

