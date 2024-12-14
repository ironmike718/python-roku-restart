#!/usr/bin/python3

"""
date: 04.20.21
edit: 12.08.24
author: mike melendez
description: python roku reboot
requires: python 3.6+
shoutouts: leveraged some code/logic from https://github.com/chall32/ROKU_restart.sh
validation: successfully tested on Roku Ultra & Roku Streaming Stick
"""

# imports

import sys, time, requests

# global vars

roku_reboot = ["home", "up", "right", "up", "right", "up", "up", "right", "select"]
cmd_timer = 0.35

# main loop

def main():

    # check for single arg

    if len(sys.argv) == 2:
        roku_host = sys.argv[1]
    else:
        sys.exit("\nusage: ./roku_restart3.py <roku ip addr>\n")

    # attempt initial connection w/ home key

    try:
        requests.post(f"http://{roku_host}:8060/keypress/home")
        time.sleep(4)
    except:
        sys.exit(f"\nerror: unable to connect to roku @ {roku_host}\n")

    # perform reboot

    for cmd in roku_reboot:
        requests.post(f"http://{roku_host}:8060/keypress/{cmd}")
        time.sleep(cmd_timer)

# start app

if __name__ == '__main__':
    main()
