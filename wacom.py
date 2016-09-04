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
screens = []
settings = {"mapScr":"none", "hand":"Right"}



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
	
	f.close()
	
	
	
def printDev():
	
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
	
	a = input("Press a key to continue... ")
	Menu()
			
def scanMonitors():
	scan = 'xrandr | grep "connected" > screen.tmp'
	os.system(scan)
	
	f = open("screen.tmp","r")
	
	data = f.readlines()
	for line in data:
		entries = line.split()
		if entries[1] == "connected":
			screens.append(entries[0])
	
	f.close()
	
def printScr():
	print("Connected screens:\n")
	for scr in screens:
		print("	" + scr + "\n")
	
	a = input("Press a key to continue... ")
	Menu()

def mapScr():
	print("Current mapped screen: {}".format(settings["mapScr"]))
	print("Available screens: ")
	i = 1
	for scr in screens:
		print("{}. {}".format(i, scr))
		i += 1
	
	print("\n")
	
	c = int(input("Choose a screen (1-9): ")) - 1
	
	try:
		for dev in devices:
			cmd ="xsetwacom --set {} MapToOutput {}".format(dev["id"],screens[c])
			os.system(cmd)
			
		settings["mapScr"] = screens[c]
		print("Screen Mapped correctly.")
		
	except Exception as e:
		print(e)
	
	
	
	input("Press a key to continue... ")
	Menu()

def setHand():
	print("Current hand setting is: {}".format(settings["hand"]))
	hand = input("Choose your hand (R/L): ")
	
	if hand == 'R' or hand == 'r':
		rot = "none"
	elif hand == 'L' or hand == 'l':
		rot = "half"
	else:
		setHand()
	
	try:
		for dev in devices:
			if dev["type"] != "PAD":
				cmd = "xsetwacom --set {} rotate {}".format(dev["id"], rot)
				os.system(cmd)
		
		print("Hand set correctly.")
		if hand == 'R' or hand == 'r':
			settings["hand"] = "Right"
		else:
			settings["hand"] = "Left"
	except Exception as e:
		print(e)
		
	input("Press a key to continue... ")
	Menu()

def Menu():
	while True:
		os.system("clear")
		mstr = '''
Welcome to the Wacom Setup Tool.
Please choose an option:

1.	List Connected Devices
2.	List Connected Screens
3.	Set Hand
4.	Map to Monitor
5.	Quit


'''

		print(mstr)
		choice = input("Enter choice: ")
	
		if choice == '1':
			printDev()
		elif choice == '2':
			printScr()
		elif choice == '3':
			setHand()
		elif choice == '4':
			mapScr()
		elif choice == '5':
			return




def main():
	scanDev()
	scanMonitors()
	Menu()
	
	
	
	
	
	return 0

if __name__ == '__main__':
    main()
