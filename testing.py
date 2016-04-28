import winsound;
import time;
import msvcrt;
import sys;
import tkinter as tk
from Channel import Channel;
from note import Note;
from setup import Setup;
from GUI import graphicInterface;
"""
	winsound plays tones ranging from 37 - 32,767 Hertz. Second paramater being time in miliseconds
	This is just for a start. We might have to find another package that allows for frequencies
	acurate to the .0000 so we can get the exact sounds we need. Will also have to play with timings to make
	it sound better. Will also look into having the program notice when a key is released and try playing
	the sound while the key is down then stopping once released. Apparently key listeners is harder than I 
	thought. Might be easier to just import pygame to handle the key listeners. Its already set up to do 
	key down and key released listening.
"""
#winsound.Beep(37, 3000);
#time.sleep(3);
#winsound.Beep(50, 3000);
#time.sleep(3)
#winsound.Beep(70, 3000);    #testing sound ranges
#time.sleep(3);
#winsound.Beep(100, 3000);
#time.sleep(3);
#winsound.Beep(150, 3000);
#time.sleep(3)
#winsound.Beep(200, 3000);


def kbfunc(): 
	""" 
		Function for reading key input. Listens for a key to be pushed. Once pushed returns the string
		of that key. Such as 'a' for the key A.
	"""
	x = msvcrt.kbhit();
	if x:
		ret = msvcrt.getch().decode('utf-8'); #built in function getch() returns byte string. The "decode" decodes it to the normal string
	else: 
		ret = 0; #returns 0 while no key is being pushed.
	return ret

def determineNote(keyString, Dict):
	return Dict[keyString];
	

SetUp = Setup();
SetUp.createNotes();
NoteDict = SetUp.getNoteDict();

root = tk.Tk()
Gui = graphicInterface(root);
#root.mainloop()
root.update()

channel_1 = Channel("channel_1");

currentOctive = 0;
currentFrequency = 0;

x = True;

while(x):
	"""
	Program Loops until tilde("`") is pushed. Continues to read keyboard for keys to be hit.
	kbfunc() returns 0 each iteration of the loop where a key is not hit. Once a key is hit 
	the program determines which key and if it matches one set to play a specific sound. 
	Program does queue key presses, such that if one presses 's' while a sound is being played
	the program will play the sound matching 's' emediately after.
	"""

	
	temp = kbfunc();
	if temp != 0:
		if temp != '`':
			if temp == ']':
				currentOctive = currentOctive + 1;
				Gui.showOctive(currentOctive);
				root.update();
				
			elif temp == '[':
				if currentOctive == 0:
					print("Octive is already at 0 (2)");
				else:
					currentOctive = currentOctive - 1;
					Gui.showOctive(currentOctive);
					root.update();
					
				
			else:
				try:
					newNote = determineNote(temp, NoteDict);
					if currentOctive == 0:
						currentFrequency = int(round(newNote.getFrequency()));
					else:
						currentFrequency = int(round(newNote.getFrequency() * (2 * currentOctive)));
					winsound.Beep(currentFrequency, 3000);
				
					channel_1.addNote(temp);
				
				except KeyError:
					print(temp);
					print("Key not mapped");

		else:
			print(channel_1.getNotes());
			sys.exit();
				
				
				
				
				