from tkinter import *
import os;

root = Tk()
root.title("Cancel Shutdown")



def click():
	#hello = "hello" + e.get()
	#label = Label(root,text=hello)
	#label.pack()
	os.system("cmd /c shutdown /a");








button = Button(root, text="Cancel shutdown", padx=40, pady=20, command=click)
button.grid(row=1, column=1, padx=40, pady=40)
root.mainloop()