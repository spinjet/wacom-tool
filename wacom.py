#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wacom.py
#  
#  Copyright 2016 GoldenPansy <spina95@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os
import re

devices = []


def scanDev():
	scan = "xsetwacom --list devices > devs.tmp"
	os.system(scan)

	f = open("devs.tmp","r")


	data = f.readlines()
	for line in data:
		entries = re.split("\t+",line)
		entries[2] = entries[2].strip()
		dev = {}
		dev["name"] = entries[0]
		dev["id"] = re.split("id: +",entries[1])[1]
		dev["type"] = re.split("type: +",entries[2])[1]
		
		devices.append(dev)

	if not devices:
		print("No Wacom Devices Found")
	else:
		print("Devices Found:")
		for dev in devices:
			s = '''
		NAME: {}
		ID: {}
		TYPE: {}
		'''.format(dev["name"], dev["id"], dev["type"])
			
			print(s)
	

def main(args):
	scanDev()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

