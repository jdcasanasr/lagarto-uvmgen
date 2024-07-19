import os
import sys

directory_tree = {
    'MISC',
    'RTL',
    'SIM',
    'TB',
}

# Take Path From User.
path = sys.argv[1]

# Check If Template Directories Already Exist. If Not, Create Them.
for directory in directory_tree:
    if not os.path.exists(f'{path}/{directory}'):
        os.makedirs(f'{path}/{directory}')