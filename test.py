from rubikscolorresolver.solver import RubiksColorSolverGeneric
import json
import logging
from math import sqrt
import twophase.solver as sv
dict = '{"27": [255, 206, 100], "16": [232, 83, 50], "8": [255, 85, 56], "40": [255, 88, 53], "4": [255, 255, 255], "22": [255, 255, 255], "48": [255, 255, 255], "29": [255, 255, 170], "31": [45, 85, 153], "15": [40, 67, 118], "19": [68, 177, 140], "32": [74, 202, 162], "21": [255, 255, 255], "54": [255, 255, 174], "45": [255, 255, 255], "11": [226, 87, 54], "47": [64, 163, 125], "44": [255, 255, 255], "7": [255, 255, 199], "9": [72, 170, 124], "25": [255, 255, 255], "30": [251, 131, 71], "38": [255, 179, 89], "13": [255, 255, 218], "37": [255, 255, 194], "42": [60, 156, 122], "5": [255, 255, 255], "50": [255, 255, 199], "20": [50, 79, 122], "33": [61, 159, 126], "28": [255, 185, 92], "35": [255, 173, 84], "46": [33, 53, 90], "1": [255, 255, 135], "6": [40, 71, 124], "39": [255, 130, 69], "24": [255, 168, 85], "18": [255, 98, 59], "14": [45, 82, 144], "2": [255, 255, 255], "34": [57, 84, 123], "49": [255, 255, 171], "51": [255, 255, 165], "10": [43, 76, 132], "3": [88, 183, 135], "36": [255, 96, 58], "52": [72, 176, 141], "53": [70, 196, 157], "12": [166, 55, 41], "17": [217, 70, 46], "23": [255, 200, 94], "26": [255, 166, 83], "43": [54, 83, 116], "41": [255, 83, 53]}'
def test():
        cube = RubiksColorSolverGeneric(3)
        try:
            cube.enter_scan_data(json.loads(dict))
            cube.crunch_colors()
            output = "".join(cube.cube_for_kociemba_strict())
        except Exception as e:
            print(e)
            # logger.exception(str(e))
            output = e
        # print(cube.cube_for_json()['squares'])

        cube = None
        print("".join(output))
        cubestring = output
        print("Recieved scramble from EV3: {}".format(cubestring))
        print('Solving...')
        solution = sv.solve(cubestring,19,2)
        solution = solution[:solution.strip().rfind(" ")]
        print(solution)

test()