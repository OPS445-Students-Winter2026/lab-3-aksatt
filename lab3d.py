#!/usr/bin/env python3
# Author ID: 184240232
import subprocess

def free_space():
    # Launches the command and captures the output
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         shell=True)
    output = p.communicate()
    # Decode from bytes to string and strip the newline character
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())
