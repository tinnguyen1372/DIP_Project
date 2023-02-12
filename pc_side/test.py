#!/usr/bin/env python3

import logging
import string
import sys, pathlib
import threading
import logging
import time
import pexpect
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
            self.spawn = pexpect.spawn(f'ssh {self.user}@{self.ip}',timeout=10)
            self.spawn.expect("password")
            self.sendline(self.password)
            self.spawn.expect(">")
            logging.info("Logged in EV3")
            self.status = True
            self.running = False
            return
        except:
            logging.info("Failed to connect to EV3")
            self.status = False
            if not self.status and not self.running:
                threading.Thread(target = self.run).start()
                self.running = True
            return

    # def run_file_name(filename):
    #     try:
    #         pexpect.run(f"python3 {filename}")
    #     except:
    #         logging.debug("Failed to run file {}".format(filename))

    def run(self):
        while not self.status:
            time.sleep(5)
            logging.info("Attempting to start again")
            self.spawn_ssh()
        return

ev3_ip = "127.0.0.1"
order = ["funtion_test",]
ev3 = EV3(ip = ev3_ip)
try:        
    ev3.spawn_ssh()
    pass
    # for i in order:
    #     ev3.run_file_name(i+'.py')
except Exception as e:
    logging.info("Error in execution")