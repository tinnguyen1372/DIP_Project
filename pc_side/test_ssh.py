#!/usr/bin/env python3
ev3_ip = "169.254.182.148"
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
                        format='%(asctime)s %(levelname)8s: %(message)s',
                    stream= sys.stdout)
logging = logging.getLogger(__name__)

class SSH_Client():
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
            self.spawn = wexpect.spawn(f'ssh {self.user}@{self.ip}',encoding = 'utf-8',timeout = 30)
            self.spawn.logfile = sys.stdout
            self.spawn.expect("Password:")
            self.spawn.sendline(self.password)
            time.sleep(1)
            logging.info("Logged in EV3")
            logging.info("Running {}.py in {}".format(filename,dir))
            self.spawn.sendline(f"python3 ./{dir}/{filename}.py")
            self.spawn.expect("\n",timeout = None)
            self.spawn.expect("\n", timeout = None)
            self.spawn.expect("\n",timeout = None)

            self.spawn.sendline("exit")
            self.spawn.expect(wexpect.EOF,timeout =None)
 
            self.spawn.close()
            logging.info("Done Solving")
            return
        except Exception as e:
            logging.info("Failed to connect to EV3 with error: {}".format(e))
            return

# order = ["main.py",]
# ev3 = SSH_Client(ip = ev3_ip)
# try:        
#     ev3.spawn_ssh(dir = directory, filename = file_to_run)
# except Exception as e:
#     logging.info("Error in execution: {}".format(e))