

class Note:
	def __init__(self, name, frequency):
		self.Name = name;
		self.Frequency = frequency;
		self.CurrentFrequency = frequency
		
	def getFrequency(self):
		return self.Frequency;
		
	def getCurrentFrequency(self):
		return self.CurrentFrequency;
		
	def getName(self):
		return self.Name;