#!/usr/bin/env python3
ev3_ip = "169.254.21.205"
directory = "test_wed8"
file_to_run = "function_test"

import logging
import string
import sys, pathlib
import threading
import logging
import time
import pexpect
from pexpect.popen_spawn import PopenSpawn
import wexpect

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s',
                        stream= sys.stdout
                    )
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
    
    def spawn_ssh(self,dir, filename):
        try:
            # self.spawn = pexpect.spawn(f'ssh {self.user}@{self.ip}',timeout=10)
            logging.info(f'SSH-ing to {self.user}@{self.ip} with password {self.password}')
            # self.spawn = pexpect.spawn(f'ssh {self.user}@{self.ip}',timeout=10)
            # self.spawn = pexpect.popen_spawn.PopenSpawn(f'ssh {self.user}@{self.ip}', encoding = 'utf-8')
            self.spawn = wexpect.spawn(f'ssh {self.user}@{self.ip}',encoding = 'utf-8',timeout = None)
            self.spawn.logfile = sys.stdout
            self.spawn.expect("Password:")
            self.spawn.sendline(self.password)
            logging.info("Logged in EV3")

            self.spawn.sendline("python3 ./{}}/{}}.py".format(dir,filename))
            self.spawn.expect("\n")
            self.spawn.expect("\n")
            self.spawn.expect("\n",timeout = None)
            self.spawn.sendline("exit")
            self.spawn.expect(wexpect.EOF)
 
            self.spawn.close()
            logging.info("Done Solving")
            self.status = True
            self.running = False
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

# order = ["main.py",]
ev3 = EV3(ip = ev3_ip)
try:        
    ev3.spawn_ssh(dir = directory, filename = file_to_run)
except Exception as e:
    logging.info("Error in execution: {}".format(e))