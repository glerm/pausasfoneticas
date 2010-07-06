# coding: utf-8

from Tkinter import *
from Tkinter import *
import tkMessageBox
import Tkinter



def sel():
   selection = "SELECIONADO -> " + str(var.get())
   label.config(text = selection)

root = Tk()
root.title("Tipos de Relatório")
root
var = IntVar()

def donothing():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Faixa Etaria", command=donothing)
filemenu.add_command(label="Tipo de História", command=donothing)
filemenu.add_command(label="Classe de Palavra", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Medias", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)



def callback():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )



F1=Tkinter.Frame(root)
F1.grid(row=1,column=1)


a=Tkinter.Label(F1, text="Amostras Pesquisa")
a.pack()


scrollbar1 = Scrollbar(F1)
scrollbar1.pack( side = RIGHT, fill=Y )







Lb1 = Listbox(F1,selectmode=MULTIPLE,yscrollcommand = scrollbar1.set, exportselection=0)
Lb1.insert(1, "T O D O S")
Lb1.insert(2, "Carlos")
Lb1.insert(3, "Carla")
Lb1.insert(4, "Alexandre")
Lb1.insert(5, "Jean")
Lb1.insert(6, "Dilma")

Lb1.config(bg="#BFBEA2", font=("Helvetica",12) )

#
def ativado():
# get selected line index
#
	itens= Lb1.curselection()
	for i in itens:
		lista = Lb1.get(i)	
		print lista

def ativarTUDO():
	Lb1.selection_set(0,6)

def desativarTUDO():
	Lb1.selection_clear(0,6)





Lb1.pack(side = RIGHT, fill = BOTH)
scrollbar1.config( command = Lb1.yview )

F2=Tkinter.Frame(root)
F2.grid(row=1,column=2)

b=Tkinter.Label(F2, text="Amostras Controle")
b.pack()

scrollbar2= Scrollbar(F2)
scrollbar2.pack( side = RIGHT, fill=Y )


Lb2 = Listbox(F2,selectmode=MULTIPLE,yscrollcommand = scrollbar2.set, exportselection=0)
Lb2.insert(1, "---(todos)---")
Lb2.insert(2, "Camila")
Lb2.insert(3, "Daniel")
Lb2.insert(4, "Monica")
Lb2.insert(5, "João")
Lb2.insert(6, "Marina")

Lb2.pack(side = RIGHT, fill = BOTH)
Lb2.config(bg="#B2A9FF", font=("Helvetica",12))
scrollbar2.config( command = Lb1.yview )

Bframe1=Tkinter.Frame(root)
Bframe1.grid(row=2,column=1)

btn1a = Tkinter.Button(Bframe1,text="Todos", relief="groove",activebackground="#ED2139", bg="darkred",fg="white",bd=4, command=ativarTUDO)
btn1a.grid(row=1,column=1)
btn1b = Tkinter.Button(Bframe1,text="Limpa", relief="groove",activebackground="#ED3921", bg="darkblue",fg="white",bd=4, command=desativarTUDO)
btn1b.grid(row=1,column=2)

btn2 = Tkinter.Button(root,text="Gerar relatórios", relief="groove",activebackground="#ED2139", bg="darkred",fg="white",bd=4, command=callback)
btn2.grid(row=2,column=2)



root.mainloop()

