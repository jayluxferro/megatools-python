#!/usr/bin/env python

"""
Author:     Jay Lux Ferro
Date:       24th August, 2019
"""

import subprocess


def cli(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    return p.stdout.read()

def formatDf(command):
    output = cli(command)
    res = {}
    for x in output.splitlines():
        d = x.decode().split(':')
        res.update({ d[0].lower() : d[-1].strip() })
    return res
