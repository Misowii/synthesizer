from note import Note;


class Channel:
	def __init__(self, name):
		self.Name = name;
		self.NoteList = [];
	
	def getNotes(self):
		return self.NoteList;
	
	def addNote(self, note):
		self.NoteList.append(note);
		#print(self.Notes);
		
	def playNotes(self):
		return
		
	
	
	