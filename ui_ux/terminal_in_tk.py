# Reference: https://stackoverflow.com/questions/7253448/how-to-embed-a-terminal-in-a-tkinter-application

from Tkinter import *
import os

root = Tk()
termf = Frame(root, height=400, width=500)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 40x20 -sb &' % wid)

root.mainloop()
