import pygame
from PyCube import PyCube
import twophase.solver as sv

def launch_cube(solution):
    cube = PyCube()
    solution_list=list(solution.split(" "))
    result_solution = []
    for i in solution_list:
        try:
            if i[1] == '2':
                result_solution.append(i[0])
                result_solution.append(i[0])
            elif i[1] == '3':
                result_solution.append(i[0])
                result_solution.append(i[0])
                result_solution.append(i[0])
            elif i[1] == '1':
                result_solution.append(i[0])
            else:
                pass
        except:
            pass
    print(result_solution)
    cube.run(result_solution)
if __name__ == '__main__':
    cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
    solution = sv.solve(cubestring,19,2)
    launch_cube(solution)
