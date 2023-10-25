#!/bin/python3

import os;
import sys;
import time;
import random;

s = 5
if len (sys.argv) > 1 and sys.argv[1].isnumeric():
    s = int(sys.argv[1])

pid = os.getpid();
ppid = os.getppid();
print("Сhild[" + str(pid) + "]: I am started. My PID " + str(pid) + ". Parent PID " + str(ppid) + ".");

time.sleep(s);

print("Child[" + str(pid) + "]: I am ended. PID " + str(pid) + ". Parent PID " + str(ppid) + ".");
os._exit(random.randint(0, 1));