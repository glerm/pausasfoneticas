#!/usr/bin/python
# -*- coding: utf-8 -*-

remaining = 0

def snooze (secs):
  """
  Snoozes for the given number of seconds. During the snooze, a progress
  dialog is launched notifying the 
  """
  global remaining
  root = Tkinter.Tk()
  prompt = 'hello'
  label1 = Tkinter.Label(root, text=prompt, width=len(prompt))
  label1.pack()

  remaining = secs

def decrement_label ():
  global remaining
  text = "Snoozing %d sec(s)" % remaining
  remaining -= 1
  label1.config(text=text, width=100)
  label1.update_idletasks()

for i in range(1, secs + 1):
  root.after(i * 1000, decrement_label )

root.after((i+1) * 1000, lambda : root.destroy())
root.mainloop()

