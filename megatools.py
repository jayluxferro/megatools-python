#!/usr/bin/env python3

"""
Author: Jay Lux Ferro
Email:  jayluxferro@sperixlabs.org, jay@ovond.com
Date:   23rd August, 2019
"""

import helper as hp
import os

class Mega:
    
    # Default path on macOS
    megaPath='/usr/local/bin/'
    dir_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, megaPath=None, configPath=dir_path + '/mega.rc'):
        
        if megaPath != None:
            self.megaPath = megaPath if megaPath[-1] == '/' else megaPath + '/'
        self.configPath = configPath
    
    def df(self, f='g'):
        f = '--mb' if f.lower() == 'm' else '--gb'
        return hp.formatDf([self.megaPath + 'megadf', f, '--config', self.configPath])

    def ls(self, path='/'):
        return hp.ls([self.megaPath + 'megals', '--config', self.configPath, path if path[0] == '/' else '/' + path])
