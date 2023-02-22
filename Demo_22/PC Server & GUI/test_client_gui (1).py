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
import queue
import logging
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)8s: %(message)s',
                    )
logging = logging.getLogger(__name__)
comque= queue.Queue()

cube = RubiksColorSolverGeneric(3)

# This is the Subscriber
# Constant
max_length = 19
time_out = 2
#IP Address of the Broker (Bluetooth Network Connection)
# ev3_ip = "169.254.119.198"
DEFAULT_DIRECTORY = "wecuber"
DEFAULT_FILE = "function_test"
DEFAULT_IP = "169.254."
STRING_CUBE = "" # save the scanned rubik (not for visualisation)
GOAL_STRING = "" # for the solveto method
METHOD = 1 
IS_RANDOM = FALSE

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/ev3_to_pc")

def on_message(client, userdata, msg):
  dict = str(msg.payload.decode('utf-8'))
#   global cube
  try:
    cube = RubiksColorSolverGeneric(3)
    cube.enter_scan_data(json.loads(dict))
    cube.crunch_colors()
    output = "".join(cube.cube_for_kociemba_strict())
    global STRING_CUBE
    STRING_CUBE = output
    cube.print_cube()
    comque.put(output)
    # visualise()
    root.event_generate('<<TimeChanged>>', when='tail')
  except Exception as e:
    print(e)
    output = e
  cube = None
#   string_cube = output
#   visualise(output)
#   method = 1 # 1 for Two phase Kociemba, 2 for Korf
  method = 1
  if (dropdown.get() == "Kociemba's algorithm"): 
      method = 1
  elif dropdown.get() == "Korf's algorithm": method = 2
  elif dropdown.get() == "Solve to chosen pattern": method = 3
  solution = solver.solve(max_length, time_out, STRING_CUBE, method,  solveToString.get("1.0",'end-1c')) # default is Kociemba
  client.publish("topic/pc_to_ev3", solution)
  #client.disconnect()

def on_message_scanOnly(client, userdata, msg):
  dict = str(msg.payload.decode('utf-8'))
  print("Using scanOnly method")
#   global string_cube
  cube = RubiksColorSolverGeneric(3)
  try:
    cube.enter_scan_data(json.loads(dict))
    cube.crunch_colors()
    output = "".join(cube.cube_for_kociemba_strict())
    global STRING_CUBE
    STRING_CUBE = output
    cube.print_cube()
    comque.put(STRING_CUBE)
    # visualise()
    root.event_generate('<<TimeChanged>>', when='tail')
  except Exception as e:
    print(e)
    output = e
  cube = None
  global GOAL_STRING
  GOAL_STRING = solveToString.get("1.0",'end-1c')
  print("Will solve to {}".format(GOAL_STRING))
  solution = solver.solve(max_length, time_out, STRING_CUBE, METHOD, GOAL_STRING)
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

def show_text(txt):
    """Display messages."""
    print(txt)
    display.insert(INSERT, txt)
    root.update_idletasks()

def show_text_random(txt):
    """Display messages."""
    print(txt)
    solveToString.delete("1.0","end")
    solveToString.insert(INSERT, txt)
    root.update_idletasks()

def show_text_log(txt):
    """Display messages."""
    print(txt)
    logText.delete("1.0","end")
    logText.insert(INSERT, txt)
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


# def solvex():
#     try:
#         # convert from cubestring to color here
#         defstr = get_definition_string()
#         # or just put the defstr directly here
#     except BaseException as e:
#         show_text('Invalid facelet configuration.\nWrong or missing colors. ' + e.__doc__)
#         return
#     show_text(defstr + '\n')
#     show_text(sv.solve(defstr,19,2) + '\n')

# def advanced_solve():
#     logging.info("Connecting to mqtt_com...")
#     ip = txt_ip.get("1.0",'end-1c')
#     ssh_client_button()
#     # ev3 = SSH_Client(ip = ip)
#     # ev3.spawn_ssh(dir = directory, filename = "function_test")
#     global commonClient
    
#     # global commonClient
#     # client = mqtt.Client()
#     try:
#         commonClient.connect(ip,1883,60)
#         commonClient.on_connect = on_connect
#         commonClient.on_message = on_message
#         commonClient.loop_forever()
#     # try:
#     #     commonClient.subscribe("topic/ev3_to_pc")
#     #     cube.enter_scan_data(json.loads(dict))
#     #     cube.crunch_colors()
#     #     output = "".join(cube.cube_for_kociemba_strict())
#     #     global STRING_CUBE
#     #     STRING_CUBE = output
        
#     except Exception as e:
#         logging.info("Scan-only operation error")
#     # global GOAL_STRING
#     # GOAL_STRING = solveToString.get("1.0",'end-1c')
#     # print("Will solve to {}".format(GOAL_STRING))
#     # solution = solver.solve(max_length, time_out, STRING_CUBE, METHOD, GOAL_STRING)
#     # commonClient.publish("topic/pc_to_ev3", solution)
    
# ########################################################################################################################

# # ################################# Functions to change the facelet colors #############################################


def clean():
    """Restore the cube to a clean cube."""
    for f in range(6):
        for row in range(3):
            for col in range(3):
                canvas.itemconfig(facelet_id[f][row][col], fill=canvas.itemcget(facelet_id[f][1][1], "fill"))
    show_text_log("Cube visualisation cleaned successfully!")


def empty():
    """Remove the facelet colors except the center facelets colors."""
    for f in range(6):
        for row in range(3):
            for col in range(3):
                if row != 1 or col != 1:
                    canvas.itemconfig(facelet_id[f][row][col], fill="grey")
    show_text_log("Cube visualisation emptied successfully!")

def visualise(event):
    # global string_cube
    if not IS_RANDOM:
        return
    temp_cubestring = comque.get()
    print("visualising ")
    # print(string_cube)
    print(temp_cubestring)
    fc = twophase.face.FaceCube()
    fc.from_string(temp_cubestring)
    # fc is already modified to match the rubik's face of the app
    idx = 0
    for f in range(6):
        # center_cubie = cols[f][1][1]
        for row in range(3):
            for col in range(3):
                # print(cols[fc.f[idx]]) # red, yellow etc.
                # print(type(cols[fc.f[idx]])) # string
                canvas.itemconfig(facelet_id[f][row][col], fill=cols[fc.f[idx]])
                idx += 1
    

def random():
    """Generate a random cube and set the corresponding facelet colors."""
    if (METHOD!=3): 
        show_text_log("Random is only available for solve to method! ")
        return
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
                # true -> false
                # white->yellow
                # green->orange
                # yellow -> white
                # blue -> red
                # orange -> green
                # red-> blue
    show_text_random(get_definition_string()+"\n")
    show_text_log("Randomize the cube succesfully. Click run file button to solve.")
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

import threading
##############
########################################################################################################################
# thread = threading.Thread(target= mqtt_com).start()
import time
def test_mqtt(ip):
    logging.info("Connecting to mqtt_com...")
    logging.info("Connecting to {}".format(ip))
    commonClient = mqtt.Client()
    # client = mqtt.Client()
    try:
        commonClient.connect(ip,1883,60)
        commonClient.on_connect = on_connect
        commonClient.on_message = on_message
       
        global DEFAULT_IP
        DEFAULT_IP = ip
        commonClient.loop_forever()
    except Exception as e:
        logging.info("Cannot connect to {}. Please try again".format(ip))
    

# thread = threading.Thread(target= test_mqtt).start()
def mqtt_connect_button():
    ip = txt_ip.get("1.0",'end-1c')
    if ip != DEFAULT_IP:
        threading.Thread(target= test_mqtt,args=(ip,)).start()
        show_text_log("Connected to {} successfully. Click Run File to start scanning & solving".format(DEFAULT_IP))
    else:
        logging.info("Already connected to {}".format(DEFAULT_IP))
        show_text_log("Already connected to {}".format(DEFAULT_IP))

from SSH_Client import *
def ssh_client_connect():
    ip = txt_ip.get("1.0",'end-1c')
    directory = txt_directory.get("1.0",'end-1c')
    file_to_run = txt_file.get("1.0",'end-1c')

    ev3 = SSH_Client(ip = ip)
    try:        
        logging.info("Running file {}.py from directory /home/robot/{}".format(file_to_run,directory))
        ev3.spawn_ssh(dir = directory, filename = file_to_run)
    except Exception as e:
        logging.info("Error in execution: {}".format(e))
    
def ssh_client_button():
    threading.Thread(target= ssh_client_connect).start()
    show_text_log("Started scanning process ...")
    

root = Tk()
root.wm_title("Solver Client")
canvas = Canvas(root, width=12 * width + 20, height=9 * width + 20)
canvas.pack()

hp = Label(text='Remote SSH connection', font=("Arial", 9, "bold"))
hp_window = canvas.create_window(10 + 0 * width, -25+ 0.6 * width, anchor=NW, window=hp)
hp = Label(text='EV3 IP address', font=("", 7))
hp_window1 = canvas.create_window(10 + 0 * width, -25+ 0.9 * width, anchor=NW, window=hp)
txt_ip = Text(height=1, width=20)
txt_ip.insert(INSERT, DEFAULT_IP)
txt_ip_window = canvas.create_window(10 + 0 * width, -25+ 1.2 * width, anchor=NW, window=txt_ip)
hp = Label(text='EV3 directory', font=("", 7))
hp_window2 = canvas.create_window(10 + 0 * width, -25+ 1.5 * width, anchor=NW, window=hp)
txt_directory = Text(height=1, width=20)
txt_directory_window = canvas.create_window(10 + 0 * width,-25+ 1.8 * width, anchor=NW, window=txt_directory)
hp = Label(text='EV3 file name', font=("", 7))
hp_window3 = canvas.create_window(10 + 0 * width, -25+ 2.1 * width, anchor=NW, window=hp)
txt_directory.insert(INSERT, DEFAULT_DIRECTORY)
txt_file = Text(height=1, width=20)
txt_file_window = canvas.create_window(10 + 0 * width, -25+ 2.4 * width, anchor=NW, window=txt_file)
txt_file.insert(INSERT, DEFAULT_FILE)
bsolve = Button(root,text="Run File", height=2, width=10, relief=RAISED, command=ssh_client_button)
bsolve_window = canvas.create_window(10 + 1.5 * width, -25 + 2.8 * width, anchor=NW, window=bsolve)
bsolve = Button(root,text="Connect", height=2, width=10, relief=RAISED, command=mqtt_connect_button)
bsolve_window = canvas.create_window(10 +0* width, -25 + 2.8 * width, anchor=NW, window=bsolve)

# bsolve = Button(root,text="Solve", height=2, width=10, relief=RAISED, command=advanced_solve)
# bsolve_window = canvas.create_window(10 + 10.5 * width, 10 + 6.5 * width, anchor=NW, window=bsolve)
bclean = Button(root,text="Clean", height=1, width=10, relief=RAISED, command=clean)
bclean_window = canvas.create_window(10 + 10.5 * width, 10 + 7.5 * width, anchor=NW, window=bclean)
bempty = Button(root,text="Empty", height=1, width=10, relief=RAISED, command=empty)
bempty_window = canvas.create_window(10 + 10.5 * width, 10 + 8 * width, anchor=NW, window=bempty)
brandom = Button(root,text="Random", height=1, width=10, relief=RAISED, command=random)
brandom_window = canvas.create_window(10 + 10.5 * width, 10 + 8.5 * width, anchor=NW, window=brandom)
display = Text(root,height=7, width=29)
text_window = canvas.create_window(100 + 6.5 * width, 10 + .5 * width, anchor=NW, window=display)


def option_changed(self, *args):
    global dropdown
    global METHOD
    temp_res = dropdown.get()
    print("User select", temp_res)
    print(type(temp_res))
    if (temp_res == "Kociemba's algorithm"): 
        METHOD = 1
        IS_RANDOM = False
        clean()
        show_text_random("")
    elif temp_res == "Korf's algorithm": 
        METHOD = 2
        IS_RANDOM = False
        clean()
        show_text_random("")
    elif temp_res == "Solve to chosen pattern":
        METHOD = 3
        IS_RANDOM = True

label_algo = Label(text='Select advanced algorithm/function', font=("Arial", 9, "bold"))
hp_window = canvas.create_window(50 + 5.5 * width, 10+6.5*width, anchor=NW, window=label_algo)
dropdown = StringVar(root)
dropdown.set("Kociemba's algorithm") # default value
option_dropdown = OptionMenu(
    root, 
    dropdown, "Kociemba's algorithm", "Korf's algorithm", "Solve to chosen pattern",
    command = option_changed)
option_dropdown.pack()
dropdown_window = canvas.create_window(50+6.5*width, 10+6.5*width, anchor = NW, window = option_dropdown)




solveToString = Text(height=2, width=20)
solveToString_window = canvas.create_window(50+6.5* width, 30+ 6.5 * width, anchor=NW, window=solveToString)
solveToString.insert(INSERT, GOAL_STRING)


logText = Text(height=3, width=20)
logText_window = canvas.create_window(50+6.5* width, 80+ 6.5 * width, anchor=NW, window=logText)


canvas.bind("<Button-1>", click)
create_facelet_rects(width)
clean()
# create_colorpick_rects(width)

root.bind('<<TimeChanged>>', visualise)



root.mainloop()


