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

######## funcoes gerais

def donothing():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )


def callback():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )


amostraspesquisa=["Marcelo","Marbas","Ronas","Guana","Kotange","Kanaima"]

##### enche a lista
def enche_listbox(lista,lbox):	
	for i in lista:
		lbox.insert(len(lista), i)

######### amostras pesquisa ### linha 1 coluna 1

F1=Tkinter.Frame(root)
F1.grid(row=1,column=1)


a=Tkinter.Label(F1, text="Amostras Pesquisa")
a.pack()

scrollbar1 = Scrollbar(F1)
scrollbar1.pack( side = RIGHT, fill=Y )

Lb1 = Listbox(F1,selectmode=MULTIPLE,yscrollcommand = scrollbar1.set, exportselection=0)


enche_listbox(amostraspesquisa, Lb1)



Lb1.config(bg="#BFBEA2", font=("Helvetica",12) )


def ativado():
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


###### amostras controle


amostrascontrole=["Simone","Tininha","Thiago","Ricardo","Augusto","Manoel"]

Lb2 = Listbox(F2,selectmode=MULTIPLE,yscrollcommand = scrollbar2.set, exportselection=0)
for i in amostrascontrole:
	Lb2.insert(len(amostrascontrole), i)

Lb2.pack(side = RIGHT, fill = BOTH)
Lb2.config(bg="#B2A9FF", font=("Helvetica",12))
scrollbar2.config( command = Lb1.yview )

Bframe1=Tkinter.Frame(root)
Bframe1.grid(row=2,column=1)

btn1a = Tkinter.Button(Bframe1,text="Todos", relief="groove",activebackground="#ED2139", bg="darkred",fg="white",bd=4, command=ativarTUDO)
btn1a.grid(row=1,column=1)
btn1b = Tkinter.Button(Bframe1,text="Limpa", relief="groove",activebackground="#ED3921", bg="darkblue",fg="white",bd=4, command=desativarTUDO)
btn1b.grid(row=1,column=2)

Bframe2=Tkinter.Frame(root)
Bframe2.grid(row=2,column=2)

btn2a = Tkinter.Button(Bframe2,text="Todos", relief="groove",activebackground="#ED2139", bg="darkred",fg="white",bd=4, command=ativarTUDO)
btn2a.grid(row=1,column=1)
btn2b = Tkinter.Button(Bframe2,text="Limpa", relief="groove",activebackground="#ED3921", bg="darkblue",fg="white",bd=4, command=desativarTUDO)
btn2b.grid(row=1,column=2)




################### MENU

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Faixa Etaria", command=donothing)
filemenu.add_command(label="Tipo de História", command=donothing)
filemenu.add_command(label="Classe de Palavra", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Medias", menu=filemenu)



helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Gerar", command=ativado)
helpmenu.add_command(label="About...", command=ativado)
menubar.add_cascade(label="Gerar", menu=helpmenu)

root.config(menu=menubar)

################################



root.mainloop()

