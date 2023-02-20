#!/usr/bin/env python3
import twophase.solver as twophase
# import optimal.solver as korf

def solve(max_length, time_out, cubestring, method, goalstring= "FBRRUFRFULRFLRLUDUBLBUFDDBFLRRRDBBDRLUDULFDDFDUUBBLBFL"):
    print("Recieved scramble from EV3: {}".format(cubestring))
    print('Solving...')
    solution = ""
    if (method == 1): # Two phase algorithm
        solution = twophase.solve(cubestring,max_length,time_out)
        solution = solution[:solution.strip().rfind(" ")]
        print("Result from Kociemba method: {}".format(solution))
    # elif method == 2: # Korf algorithm
    #     solution = korf.solve(cubestring)
    #     solution = solution[:solution.strip().rfind(" ")]
    elif method == 3: # SolveTo using two phase algorithm
        print("Trying to solve to: {}".format(goalstring))
        solution = twophase.solveto(cubestring, goalstring)
        solution = solution[:solution.strip().rfind(" ")]
        print("Result from solveto method: {}".format(solution))
    print(solution)
    return solution