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


def callback():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )

MAINFRAME=Tkinter.Frame(root)
MAINFRAME.pack(side=LEFT)


R1 = Radiobutton(MAINFRAME,text="Relatorio Por Amostra", variable=var, value=1,command=sel)
R1.pack(anchor = W)

R2 = Radiobutton(MAINFRAME, text="Média por Faixa Etária", variable=var, value=2,command=sel)
R2.pack(anchor = W)

R3 = Radiobutton(MAINFRAME, text="Média por Tipos de Histórias", variable=var, value=3,command=sel)
R3.pack( anchor = W)

R4 = Radiobutton(MAINFRAME, text="Média por Classe de palavra", variable=var, value=4,command=sel)
R4.pack( anchor = W)

R5 = Radiobutton(MAINFRAME, text="TODOS", variable=var, value=4,command=sel)
R5.pack( anchor = W)



FRAME=Tkinter.Frame(MAINFRAME)
FRAME.pack()


c = Tkinter.Button(FRAME,text="Gerar relatórios", relief="groove",activebackground="#ED2139", bg="darkred",fg="white",bd=4, command=callback)
c.pack()



F1=Tkinter.Frame(FRAME)
F1.pack()


a=Tkinter.Label(F1, text="Amostras Pesquisa")
a.pack()


scrollbar1 = Scrollbar(F1)
scrollbar1.pack( side = RIGHT, fill=Y )

Lb1 = Listbox(F1,selectmode=MULTIPLE,yscrollcommand = scrollbar1.set, exportselection=0)
Lb1.insert(1, "Geisa")
Lb1.insert(2, "Carlos")
Lb1.insert(3, "Carla")
Lb1.insert(4, "Alexandre")
Lb1.insert(5, "Jean")
Lb1.insert(6, "Dilma")

Lb1.config(bg="#BFBEA2", font=("Helvetica",20,"bold"))

Lb1.pack(side = RIGHT, fill = BOTH)
scrollbar1.config( command = Lb1.yview )

F2=Tkinter.Frame(FRAME)
F2.pack()

b=Tkinter.Label(F2, text="Amostras Controle")
b.pack()

scrollbar2= Scrollbar(F2)
scrollbar2.pack( side = RIGHT, fill=Y )


Lb2 = Listbox(F2,selectmode=MULTIPLE,yscrollcommand = scrollbar2.set, exportselection=0)
Lb2.insert(1, "Geraldo")
Lb2.insert(2, "Camila")
Lb2.insert(3, "Daniel")
Lb2.insert(4, "Monica")
Lb2.insert(5, "João")
Lb2.insert(6, "Marina")

Lb2.pack(side = RIGHT, fill = BOTH)
Lb2.config(bg="#B2A9FF", font="Helvetica")
scrollbar2.config( command = Lb1.yview )






root.mainloop()

