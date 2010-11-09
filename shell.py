#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os
from Tkinter import *

def rendershell():
	root = Tk()
	root.title("Renderização")
	root.geometry('320x240+230+130')
	t = Text(root,foreground="orange",background="black")
	t.pack()
	p = os.popen("python sleep.py", 'r')
	root.tk.call("update")
	root.focus_set()
	for l in p.xreadlines():
		t.insert(END, '%s\n' % l.rstrip())
		#t.see(END)
		t.tk.call('update')
		#root.call("update")
		#t.update_idletasks()
	root.mainloop()
		



if __name__ == '__main__':
	rendershell()

