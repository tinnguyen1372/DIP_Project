#!/usr/bin/env python3

import logging
import string
import sys, pathlib
import threading
import logging
import time
import pexpect
# from pexpect.popen_spawn import PopenSpawn
import wexpect
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
logging = logging.getLogger(__name__)
class EV3():
    # Initialize User Config for SSH connection
    def __init__(self,**kw) :
        self.user = kw.get('username','robot')
        self.password = kw.get('password','maker')
        self.ip = kw.get('ip','')
        self.retry = 0
        logging.info("IP of {} loaded from config: {}".format(self.user, self.ip))
    
        # Threading looping connection try
        self.running = False

        # # Spawning connection
        # self.spawn_ssh()
    
    def spawn_ssh(self):
        try:
            # self.spawn = pexpect.spawn(f'ssh {self.user}@{self.ip}',timeout=10)
            logging.info(f'SSH-ing to {self.user}@{self.ip} with password {self.password}')
            # self.spawn = pexpect.spawn(f'ssh {self.user}@{self.ip}',timeout=10)
            # self.spawn = pexpect.popen_spawn.PopenSpawn(f'ssh {self.user}@{self.ip}',timeout=10)
            self.spawn = wexpect.spawn(f'ssh {self.user}@{self.ip}',timeout=10)
            self.spawn.expect("Password:".format(self.user, self.ip))
            self.spawn.sendline(self.password)
            logging.info("Logged in EV3")
            self.spawn.expect("#")
            logging.info(self.spawn.readline())
            self.spawn.sendline(f"python3 ./test_wed8/main.py")
            self.status = True
            self.running = False
            # try:

            # except:
            #     logging.debug("Failed to run file {}".format("main.py"))
            return
        except Exception as e:
            logging.info("Failed to connect to EV3 with error: {}".format(e))
            self.status = False
            if not self.status and not self.running:
                threading.Thread(target = self.run).start()
                self.running = True
            return

    def run(self):
        while not self.status:
            time.sleep(5)
            logging.info("Attempting to start again")
            self.spawn_ssh()
        return

ev3_ip = "169.254.111.4"
# order = ["main.py",]
ev3 = EV3(ip = ev3_ip)
try:        
    ev3.spawn_ssh()
except Exception as e:
    logging.info("Error in execution: {}".format(e))