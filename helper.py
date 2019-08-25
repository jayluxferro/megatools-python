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

def ls(command):
    output = cli(command)
    res = []
    for x in output.splitlines():
        res.append(x.decode())
    return res

def put(command):
    output = cli(command).decode().lower()
    
    if output.find('exists') != -1:
        return { 'error': True, 'message': 'File already exists' }

    elif output.find('error') != -1:
        return { 'error': True, 'message': 'Process failed' }

    else:
        return { 'error': False, 'message': 'Process completed' }


def rm(command):
    output = cli(command).decode().lower()

    if output.find('error') != -1:
        return { 'error': True, 'message': 'File not found' }
    else:
        return { 'error': False, 'message': 'Process completed' }


def md(command):
    output = cli(command).decode().lower()

    if output.find('exists') != -1:
        return { 'error': True, 'message': 'Directory already exists' }
    elif output.find('error') != -1:
        return { 'error': True, 'message': 'Failed to create directory' }
    else:
        return { 'error': False, 'message': 'Directory created' }


def copy(command):
    output = cli(command).decode().lower()

    if output.find('error') != -1:
        return { 'error': True, 'message': 'Process failed' }
    else:
        return { 'error': False, 'message': 'Process completed' }


def get(command):
    output = cli(command).decode().lower()

    if output.find('error') != -1:
        return { 'error': True, 'message': 'Process failed' }
    else:
        return { 'error': False, 'message': 'Process completed' }


def url(command):
    output = cli(command).decode()

    if output.lower().find('error') != -1:
        return { 'error': True, 'message': 'Process failed' }
    else:
        return { 'error': False, 'link': output.strip().split(' ')[0] } 


def dl(command):
    output = cli(command).decode().lower()

    if output.find('error') != -1:
        return { 'error': True, 'message': 'Process failed' }
    else: 
        return { 'error': False, 'message': 'Process completed' }
