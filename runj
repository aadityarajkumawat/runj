#!/usr/bin/env python3
import os
import sys
file_location = os.path.dirname(__file__)
pwd = os.getcwd()
executable_binary_name = 'maincpython-38.pyc'
arg = ''
if len(sys.argv) > 1:
    arg = sys.argv[1]
os.system('cd {} && python3 ./{} {} {}'.format(file_location,
                                               executable_binary_name, arg, pwd))
