from fabric.api import *
'''
OPS435 Assignment 2S - Winter 2021
Program: a2s_ajzarcone.py
Author: "Agostino Zarcone"
The python code in this file a2s_ajzarcone.py is original work written by
Agostino Zarcone. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
'''

env.user = "student"

def addUser(name):
    '''add a user with given user name to remote system'''
    cmd = 'useradd ' + name
    status = sudo(cmd)
    print(status)
 
def listUser():
    '''return a list of shell user on a remote system'''
    env.warn_only=True
    cmd = 'getent passwd | grep ' + '"/bin/bash"' + ' | cut -d: -f1'
    status = run(cmd)
    results1 = []
    for user in status.splitlines():
        results1.append(user)
    print(results1)

def listSysUser():
    '''return a list of system (non-shell) user'''
    env.warn_only=True
    cmd = 'getent passwd | grep ' + '"nologin"' + ' | cut -d: -f1'
    status = run(cmd)
    results2 = []
    for user in status.splitlines():
        results2.append(user)
    print(results2)

def findUser(name):
    '''find user with a given user name'''
    env.warn_only=True
    cmd = 'getent passwd | cut -d: -f1 | grep ' + name
    status = run(cmd)
    if status == name:
        print('Found user ' + name + ' on the system.')
    else:
        print('User ' + name + ' is not on the system.')

