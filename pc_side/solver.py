#!/usr/bin/env python3
import twophase.solver as twophase
#import optimal.solver as korf

def solve(max_length, time_out, cubestring, method):
    print("Recieved scramble from EV3: {}".format(cubestring))
    print('Solving...')
    solution = ""
    if (method == 1):
        solution = twophase.solve(cubestring,max_length,time_out)
        solution = solution[:solution.strip().rfind(" ")]
    # elif method == 2:
    #     solution = korf.solve(cubestring)
    #     solution = solution[:solution.strip().rfind(" ")]
    print(solution)
    return solution