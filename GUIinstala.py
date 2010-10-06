#! /usr/bin/env python

# -*- coding: utf-8 -*-


import Tkinter, tkFileDialog
import tkMessageBox
from barra import *
from renderiza import *


root = Tkinter.Tk()
root.title("Gerador")
F=Tkinter.Frame(root)
F.pack()

photo= Tkinter.PhotoImage(file="pausaswav.gif")

root.geometry("350x300")



def callback():
	dirname = tkFileDialog.askdirectory(parent=root,initialdir="~",title='Selecione o diretorio de trabalho')
	#GUIrenderiza()
	tkMessageBox.showinfo("Pronto! relatorios .pdf foram gerados e estao no diretorio " + dirname, "Nenhum erro")
	GUIrenderiza()
	#tkMessageBox.showerror("Nada a fazer!", "Nao existem arquivos .aup \n no diretorio "+ dirname)	



w = Tkinter.Label(F, text=" Instalador \n Filtro de Pausas Silentes ", font=("Helvetica",20,"bold"),bg="darkgrey",fg="black")
w.pack()

b=Tkinter.Label(F,image=photo)
b.pack()

a=Tkinter.Label(F, text="Este programa pega todos arquivos .aup\n de um diretorio e gera relatorios .pdf  \n com dados detalhados sobre pausas \n entre palavras previamente selecionadas \n no editor Audacity.")
a.pack()

c = Tkinter.Button(F, text="Selecione aqui o diretorio com os arquivos .aup", relief="groove",activebackground="#ED2139", bg="darkred",fg="white",bd=4, command=callback)
c.pack()



Tkinter.mainloop()
