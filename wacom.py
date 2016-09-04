#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#
#
#MIT License
#
#Copyright (c) 2016 goldenpansy
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
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

