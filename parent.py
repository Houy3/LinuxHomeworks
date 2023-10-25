#!/bin/python3

def startChildMessage(pid, childPid):
    print("Parent[" + str(pid) + "]: I ran children process with " + str(childPid) + " child_pid.")

def doFork():
    newChild = os.fork();
    if (newChild < 0):
        return doFork();
    return newChild;

import sys;
import random;
import os;

n = 5
if len (sys.argv) > 1 and sys.argv[1].isnumeric():
    n = int(sys.argv[1])

ppid = os.getpid();
childPids = [0]*n;
isChild = False;
i = 0;
while (i < n):
    #дублируем
    childPids[i] = doFork();
    #если поток потомок, то выходим
    if childPids[i] == 0 :
        isChild = True;
        break;
    #если поток родитель, то выводим сообщение
    startChildMessage(ppid, childPids[i])
    i += 1;

#если поток родитель
if not isChild:
    i = 0;
    while (i < n):
        #ожидаем завершения
        childPid, status = os.wait();
        #почему-то статус умножается на 256, поэтому делим на 256
        status = int(status / 256);
        print("Parent[" + str(ppid) + "]: Child with PID " + str(childPid) + " terminated. Exit Status " + str(status) + ".")
        if (status != 0):
            newChild = doFork();
            if (newChild == 0) :
                isChild = True;
                break;
            startChildMessage(ppid, newChild)
        else:
            i += 1;

if isChild:
    os.execve('child.py', ["child", str(random.randint(5,10))], {})