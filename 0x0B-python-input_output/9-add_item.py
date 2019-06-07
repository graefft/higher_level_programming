#!/usr/bin/python3
"""Module for save_to_json_file"""

import os
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

new_list = []
json_file = 'add_item.json'

if os.path.exists(json_file):
    new_list = load_from_json_file(json_file)

for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

save_to_json_file(new_list, json_file)
