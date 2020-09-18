from tkinter import *
import os;

root = Tk()
root.title("Shutdown")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e.insert(0,"Enter minutes left until shutdown")

def click():
	#hello = "hello" + e.get()
	#label = Label(root,text=hello)
	#label.pack()
	current = int(e.get())
	shutdown_timer(current)


x = 0;
def shutdown_timer(timeleft):
	x = timeleft;
	#print(type(x));
	x *= 60;
	print("Seconds left until shutdown... " + str(x));
	os.system("cmd /c shutdown -s -t " + str(x));




button = Button(root, text="shutdown", padx=40, pady=20, command=click)
button.grid(row=1, column=1, padx=40, pady=40)
root.mainloop()