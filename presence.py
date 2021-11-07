#!/bin/python3
import argparse
import subprocess
from time import sleep
import pulsectl

argparser = argparse.ArgumentParser(
    description='Automatically reduce volume of background applications')
argparser.add_argument(
    dest='period',
    type=float,
    help='Period in seconds',
    nargs='*',
    default=0.2)
argparser.add_argument(
    dest='active_volume',
    type=float,
    help='The volume to set when the active window is focused',
    nargs='*',
    default=1.0)
argparser.add_argument(
    dest='inactive_volume',
    type=float,
    help='The volume to set when the active window is not focused',
    nargs='*',
    default=0.5)
args = argparser.parse_args()

pulse = pulsectl.Pulse('pulse-volume-control')
while True:
    active_pid = subprocess.check_output(['xdotool', 'getwindowfocus', 'getwindowpid']).decode('utf-8').strip()
    for app in pulse.sink_input_list():
        pid = app.proplist['application.process.id']
        volume = app.volume
        if pid == active_pid:
            volume.values = 2 * [args.active_volume]
        else:
            volume.values = 2 * [args.inactive_volume]
        pulse.volume_set(app, volume)
    sleep(args.period)
