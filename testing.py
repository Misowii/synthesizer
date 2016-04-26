import winsound;
import time;
import msvcrt;
import sys;

"""
	winsound plays tones ranging from 37 - 32,767. Second paramater being time in miliseconds
	This is just for a start. We will have to find another package that allows for frequencies
	of something so we can get the exact sounds we need.
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

"""
	Functions that just play a specific sound for 1 second. Mainly just for testing.
"""
def playSoundOne():
	winsound.Beep(200, 1000);
	return

def playSoundTwo():
	winsound.Beep(300, 1000);
	return

def playSoundThree():
	winsound.Beep(100, 1000);
	return

	
	
	
x = True

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
		if temp == '`':
			sys.exit();
		elif temp == 'a':
			playSoundOne();
		elif temp == 's':
			playSoundTwo();
		elif temp == 'd':
			playSoundThree();
		else:
			print(temp);
		