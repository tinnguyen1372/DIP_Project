#!/usr/bin/env python3

import logging
import string
import sys, pathlib
import threading
import logging
import time
import pexpect

class EV3():
    # Initialize User Config for SSH connection
    def __init__(self,**kw) :
        self.event = threading.Event()
        self.user = kw.get('username','robot')
        self.password = kw.get('password','maker')
        self.ip = kw.get('ip','')
        self.retry = 0
        logging.info("IP of {} loaded from config: {}".format(self.user, self.ip))
    
        # Threading looping connection try
        self.lock = threading.Lock()
        self.running = False
        self.counter= threading.Thread(target = self.time_loop, daemon = True)

        # # Spawning connection
        # self.spawn_ssh()
    
    def spawn_ssh(self):
        try:
            # self.spawn = pexpect.spawn(f'ssh {self.user}@{self.ip}',timeout=10)
            self.spawn = pexpect.spawn(f'ssh {self.user}@ev3dev',timeout=10)
            self.spawn.expect("password")
            self.sendline(self.password)
            self.spawn.expect(">")
            logging.info("Logged in EV3")
            self.status = True
            self.running = False
            self.counter.start()
            return
        except:
            logging.debug("Failed to connect to EV3")
            self.status = False
            if not self.status and not self.running:
                threading.Thread(target = self.run, daemon = True).start()
                self.running = True
            return

    def run_file_name(filename):
        try:
            pexpect.run(f"python3 {filename}")
        except:
            logging.debug("Failed to run file {}".format(filename))

    def run(self):
        while not self.status:
            time.sleep(5)
            logging.debug("Attempting to start again")
            self.spawn_ssh()
        return

    def time_loop(self, num=0):
        # This function helps to keep the ssh always online inside the ssh client
        while True:
            if self.event.is_set():
                self.event.clear()
                num = 0
            if num>=10:
                if not self.status:
                    self.spawn_ssh()
                self.ask_status()
                num= 0
            time.sleep(1)
            num+=1

ev3_ip = ""
order = ["funtion_test",]
ev3 = EV3(ip = ev3_ip)
try:        
    ev3.spawn_ssh()
    for i in order:
        ev3.run_file_name(i+'.py')
except Exception as e:
    logging.info("Error in execution")