
import tkinter as tk

class graphicInterface():
	def __init__(self, master):
		self.Master = master;
		master.title("Synthesizer");

        # create a prompt, an input box, an output label,
        # and a button to do the computation
		self.OctiveTitle = tk.Label(master, text="Current Octive", anchor="w")
		#self.entry = tk.Entry(self)
		self.OctiveDisplay = tk.Label(master, text="0")
		#self.submit = tk.Button(self, text="Submit", command = self.showOctive(octive))

        # lay the widgets out on the screen. 
		self.OctiveTitle.pack(side="top", fill="x")
		#self.entry.pack(side="top", fill="x", padx=20)
		self.OctiveDisplay.pack(side="top", fill="x", expand=True)
		#self.submit.pack(side="right")

	def showOctive(self, octive):
		self.OctiveDisplay.configure(text=str(octive))

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
	root = tk.Tk()
	graphicInterface(root).pack(fill="both", expand=True)
	root.mainloop()

