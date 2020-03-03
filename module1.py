import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter import messagebox


class SaveProject:
    

    def __init__(self, master): #creating an initialization for the window
 
        self.master = master 
        self.textFrame = ScrolledText(self.master, width=50, bd=10, relief="raised") #textbox generation through tkinter
        self.textFrame.pack() #sorting the grid for us
 
        self.save_btn = tk.Button(self.master, text='Output .ncc File', command=self.save) #output text on the button function within tkinter
        self.save_btn.pack()

    def save(self): #creating the definition for what happens when you want to .save
        messagebox.showinfo('Submission Complete', 'Your G-code has been created into a file!') #creates a window that has this as the title and message
        self.saveText = self.textFrame.get('1.0', tk.END)  # Gets all text in widget.
        print('self.saveText:', self.saveText) #prints within the system the text that is being saved to output.ncc
        fl = open("output.ncc", "w") #this actually saves the files and writes (not appends)
        fl.write(self.saveText)


root = Tk() #generating a window
root.geometry('650x450') #size of program
root.title("Welcome to ARM 05 Jr Design 2 Python GUI G-Code Interpreter!") #title for the program
#lbl = Label(root, text="Welcome to ARM 05 Jr Design 2 Python GUI G-Code Interpreter!")

project = SaveProject(root)
root.mainloop()