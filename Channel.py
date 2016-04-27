from note import Note;


class Channel:
	def __init__(self, name):
		self.Name = name;
		self.Notes = [];
	
	def getNotes(self):
		return self.Notes;
	
	def addNote(self, note):
		self.Notes.append(note);
		#print(self.Notes);
		
	def playNotes(self):
		return
		
	
	
	