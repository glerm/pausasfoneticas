#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os
from Tkinter import *
import time

def rendershell():
	root = Tk()
	root.title("Renderização")
	root.geometry('320x240+230+130')
	t = Text(root,foreground="orange",background="black")
	t.pack()
	root.tk.call("update")
	root.focus_set()
	for l in xrange(10):
		time.sleep(1)
		t.insert(END, str(l)+'\n')
		t.tk.call('update')
	root.mainloop()
		



if __name__ == '__main__':
	rendershell()

