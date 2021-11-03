#!/usr/bin/env python3
import os

output = os.popen('ls -la')
executable_binary_name = 'main.cpython-38.pyc'

files_with_permissions = output.read().splitlines()

binary_was_present = False

for i in range(len(files_with_permissions)):
    if executable_binary_name in files_with_permissions[i]:
        binary_was_present = True
        executable_binary_info = files_with_permissions[i]
        indexed_details = executable_binary_info.split(' ')
        if not 'x' in indexed_details[0]:
            os.system('chmod +x ./{}'.format(executable_binary_name))
        os.system('python3 ./{}'.format(executable_binary_name))

if not binary_was_present:
    print('The required binary is not present')
