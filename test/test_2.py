output = "U2 F2 R2 F2 R3 F2 U2 R1 B3 L2 U1 L2 F2 D2 R3 D3 B2 R3"
actions = output.strip().split()
print(actions)
import logging
# log = logging.getLogger(__name__)

from pprint import pformat

def run_kociemba_actions(actions):
        print('Action (kociemba): {}'.format(' '.join(actions)))
        total_actions = len(actions)

        for (i, a) in enumerate(actions):
            # if a.endswith("3"):
            #     face_down = list(a)[0]
            #     rotation_dir = 1
            # elif a.endswith("2"):
            #     face_down = list(a)[0]
            #     rotation_dir = 2
            # elif a.endswith("1"):
            #     face_down = list(a)[0]
            #     rotation_dir = 3
            face_down = list(a)[0]
            rotation_dir = 4 - int(a[-1])

            print("Move {}/{}: Face_down:{}     Rotation_dir:{} (action: {})".format(i, total_actions, face_down, rotation_dir, pformat(a)))

            def move(face_down):
                print("Face_down {}".format(face_down))
                state = ['U', 'D', 'F', 'L', 'B', 'R']
                position = state.index(face_down)
                actions = {
                    0: ["flip", "flip"],
                    1: [],
                    2: ["rotate_cube_2", "flip"],
                    3: ["rotate_cube_1", "flip"],
                    4: ["flip"],
                    5: ["rotate_cube_3", "flip"]
                }.get(position, None)
                for a in actions:
                    print("Cube run function {}()".format(a))
                
            move(face_down)

            if rotation_dir == 1:
                # self.rotate_cube_blocked_1()
                print("Cube run rotate_cube_blocked_1()")
            elif rotation_dir == 2:
                # self.rotate_cube_blocked_2()
                print("Cube run rotate_cube_blocked_2()")
            elif rotation_dir == 3:
                # self.rotate_cube_blocked_3()
                print("Cube run rotate_cube_blocked_3()")
            print("\n")
run_kociemba_actions(actions)
# self.cube_done()