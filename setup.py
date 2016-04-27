from Channel import Channel;
from note import Note;

class Setup:
	def __init__(self):
		self.NoteDict = {};
	
	def addNotetoDict(self, key, note):
		self.NoteDict[key] = note;
	
	def getNoteDict(self):
		return self.NoteDict
	
	def createNotes(self):
		sound_1 = Note("C_2", 65.41);
		self.addNotetoDict('z', sound_1);
		
		sound_2 = Note("C#_2", 69.30);
		self.addNotetoDict('s', sound_2);
		
		sound_3 = Note("D_2", 73.42);
		self.addNotetoDict('x', sound_3);
				
		sound_4 = Note("D#_2", 77.78);
		self.addNotetoDict('d', sound_4);
				
		sound_5 = Note("E_2", 82.41);
		self.addNotetoDict('c', sound_5);
				
		sound_6 = Note("F_2", 87.31);
		self.addNotetoDict('v', sound_6);
				
		sound_7 = Note("F#_2", 92.50);
		self.addNotetoDict('g', sound_7);
				
		sound_8 = Note("G_2", 98.00);
		self.addNotetoDict('b', sound_8);
				
		sound_9 = Note("G#_2", 103.83);
		self.addNotetoDict('h', sound_9);
				
		sound_10 = Note("A_2", 110.00);
		self.addNotetoDict('n', sound_10);
				
		sound_11 = Note("A#_2", 116.54);
		self.addNotetoDict('j', sound_11);
				
		sound_12 = Note("B_2", 123.47);
		self.addNotetoDict('m', sound_12);

		
		