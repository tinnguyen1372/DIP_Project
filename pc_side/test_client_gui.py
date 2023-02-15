#!/usr/bin/env python3
import solver
import paho.mqtt.client as mqtt
from rubikscolorresolver.solver import RubiksColorSolverGeneric
import json
from solver import solve
from tkinter import *
import twophase.cubie as cubie
import twophase.solver as sv
import twophase

# This is the Subscriber
# Constant
max_length = 19
time_out = 2
#IP Address of the Broker (Bluetooth Network Connection)
ev3_ip = "169.254.35.24"

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/ev3_to_pc")

def on_message(client, userdata, msg):
  dict = str(msg.payload.decode('utf-8'))
  cube = RubiksColorSolverGeneric(3)
  try:
    cube.enter_scan_data(json.loads(dict))
    cube.crunch_colors()
    output = "".join(cube.cube_for_kociemba_strict())
    cube.print_cube()
  except Exception as e:
    print(e)
    output = e
  cube = None
  cubestring = output
  visualise()
  method = 1 # 1 for Two phase Kociemba, 2 for Korf
  solution = solver.solve(max_length, time_out, cubestring, method)
  client.publish("topic/pc_to_ev3", solution)
  #client.disconnect()
    


# ################ A simple graphical interface which communicates with the server #####################################



# ################################## Some global variables and constants ###############################################
width = 60  # width of a facelet in pixels
facelet_id = [[[0 for col in range(3)] for row in range(3)] for face in range(6)]
colorpick_id = [0 for i in range(6)]
# cubestring = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
curcol = None
t = ("U", "R", "F", "D", "L", "B")
cols = ("yellow", "green", "red", "white", "blue", "orange")
########################################################################################################################

# ################################################ Diverse functions ###################################################
global cubestring

def show_text(txt):
    """Display messages."""
    print(txt)
    display.insert(INSERT, txt)
    root.update_idletasks()


def create_facelet_rects(a):
    """Initialize the facelet grid on the canvas."""
    offset = ((1, 0), (2, 1), (1, 1), (1, 2), (0, 1), (3, 1))
    for f in range(6):
        for row in range(3):
            y = 10 + offset[f][1] * 3 * a + row * a
            for col in range(3):
                x = 10 + offset[f][0] * 3 * a + col * a
                facelet_id[f][row][col] = canvas.create_rectangle(x, y, x + a, y + a, fill="grey")
                if row == 1 and col == 1:
                    canvas.create_text(x + width // 2, y + width // 2, font=("", 14), text=t[f], state=DISABLED)
    for f in range(6):
        canvas.itemconfig(facelet_id[f][1][1], fill=cols[f])


def create_colorpick_rects(a):
    """Initialize the "paintbox" on the canvas."""
    global curcol
    global cols
    for i in range(6):
        x = (i % 3)*(a+5) + 7*a
        y = (i // 3)*(a+5) + 7*a
        colorpick_id[i] = canvas.create_rectangle(x, y, x + a, y + a, fill=cols[i])
        canvas.itemconfig(colorpick_id[0], width=4)
        curcol = cols[0]


def get_definition_string():
    # TODO: convert from cubetring to color
    """Generate the cube definition string from the facelet colors."""
    color_to_facelet = {}
    for i in range(6):
        color_to_facelet.update({canvas.itemcget(facelet_id[i][1][1], "fill"): t[i]})
    s = ''
    for f in range(6):
        for row in range(3):
            for col in range(3):
                s += color_to_facelet[canvas.itemcget(facelet_id[f][row][col], "fill")]
    return s
########################################################################################################################

# ###################################### Solve the displayed cube ######################################################


def solvex():
    try:
        # convert from cubestring to color here
        defstr = get_definition_string()
        # or just put the defstr directly here
    except BaseException as e:
        show_text('Invalid facelet configuration.\nWrong or missing colors. ' + e.__doc__)
        return
    show_text(defstr + '\n')
    show_text(sv.solve(defstr,19,2) + '\n')

########################################################################################################################

# ################################# Functions to change the facelet colors #############################################


def clean():
    """Restore the cube to a clean cube."""
    for f in range(6):
        for row in range(3):
            for col in range(3):
                canvas.itemconfig(facelet_id[f][row][col], fill=canvas.itemcget(facelet_id[f][1][1], "fill"))


def empty():
    """Remove the facelet colors except the center facelets colors."""
    for f in range(6):
        for row in range(3):
            for col in range(3):
                if row != 1 or col != 1:
                    canvas.itemconfig(facelet_id[f][row][col], fill="grey")

def visualise():
    
    fc = twophase.face.FaceCube()
    fc.from_string(cubestring)
    idx = 0
    for f in range(6):
        for row in range(3):
            for col in range(3):
                canvas.itemconfig(facelet_id[f][row][col], fill=cols[fc.f[idx]])
                idx += 1
    

def random():
    """Generate a random cube and set the corresponding facelet colors."""
    cc = cubie.CubieCube()
    cc.randomize()
    fc = cc.to_facelet_cube()
    print(type(fc) )
    idx = 0
    for f in range(6):
        for row in range(3):
            for col in range(3):
                canvas.itemconfig(facelet_id[f][row][col], fill=cols[fc.f[idx]])
                idx += 1
########################################################################################################################

# ################################### Edit the facelet colors ##########################################################


def click(_event):
    """Define how to react on left mouse clicks."""
    global curcol
    idlist = canvas.find_withtag("current")
    if len(idlist) > 0:
        if idlist[0] in colorpick_id:
            curcol = canvas.itemcget("current", "fill")
            for i in range(6):
                canvas.itemconfig(colorpick_id[i], width=1)
            canvas.itemconfig("current", width=5)
        else:
            canvas.itemconfig("current", fill=curcol)
########################################################################################################################

#  ###################################### Generate and display the TK_widgets ##########################################




root = Tk()
root.wm_title("Solver Client")
canvas = Canvas(root, width=12 * width + 20, height=9 * width + 20)
canvas.pack()

bsolve = Button(text="Solve", height=2, width=10, relief=RAISED, command=solvex)
bsolve_window = canvas.create_window(10 + 10.5 * width, 10 + 6.5 * width, anchor=NW, window=bsolve)
bclean = Button(text="Clean", height=1, width=10, relief=RAISED, command=clean)
bclean_window = canvas.create_window(10 + 10.5 * width, 10 + 7.5 * width, anchor=NW, window=bclean)
bempty = Button(text="Empty", height=1, width=10, relief=RAISED, command=empty)
bempty_window = canvas.create_window(10 + 10.5 * width, 10 + 8 * width, anchor=NW, window=bempty)
brandom = Button(text="Random", height=1, width=10, relief=RAISED, command=random)
brandom_window = canvas.create_window(10 + 10.5 * width, 10 + 8.5 * width, anchor=NW, window=brandom)
display = Text(height=7, width=39)
text_window = canvas.create_window(10 + 6.5 * width, 10 + .5 * width, anchor=NW, window=display)
canvas.bind("<Button-1>", click)
create_facelet_rects(width)
create_colorpick_rects(width)
root.mainloop()


##############
# Connect to client
client = mqtt.Client()
client.connect(ev3_ip,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
########################################################################################################################