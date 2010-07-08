# coding: utf-8

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

######## funcoes globais

def donothing():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )

##########################################################

pesquisa=["Marcelo","Jarbas","Jonas","Luana","Solange","Janaina"]
controle=["Simone","Tininha","Thiago","Ricardo","Augusto","Manoel"]
idade=["5 anos","7 anos","8 anos","10 anos"] 
historia=["Mecânica 1","Mecânica 2","Comportamental 1","Comportamental 2","Intencional"]
gramatica=["substantivo","verbo","adjetivo","advérbio","conjunção"]

cor1="#BFACC5"
cor2="#BFBEA2"
cor3="#FBBEA2"
cor4="#BFAAA2"
cor5="#00B3A0"



	
#def enche_listbox(lista,lbox):	
#	for i in lista:
#		lbox.insert(len(lista), i)	
		



######### funcao que define a celula de itens com botoes de seleciona tudo/nada e todos itens dentro


class Celula:
	def __init__(self,root,coluna,listadeitens,tipo,cor):


		F1=Tkinter.Frame(root)
		F1.grid(row=1,column=coluna)


		label=Tkinter.Label(F1, text=tipo)
		label.pack()

		scrollbar1 = Scrollbar(F1)
		scrollbar1.pack( side = RIGHT, fill=Y )

		lbox = Listbox(F1,selectmode=MULTIPLE,yscrollcommand = scrollbar1.set, exportselection=0)
		#exportselection=0 para multiplas instancias funcionarem independentes

		for i in listadeitens:
			lbox.insert(len(listadeitens), i)
		tamanhodalista = len(listadeitens)

		#### funções de leitura interna da celula

		def ativarTUDO():
			lbox.selection_set(0,tamanhodalista)
			#print [lbox.get(i) for i in lbox.curselection()]

		def desativarTUDO():
			lbox.selection_clear(0,tamanhodalista)

		def ler():
			print [lbox.get(i) for i in lbox.curselection()]
		#######################################################




		lbox.bind("<ButtonRelease-1>", donothing)




		lbox.config(bg=cor, font=("Helvetica",12) )
		lbox.pack(side = RIGHT, fill = BOTH)
		scrollbar1.config( command = lbox.yview )









		Bframe1=Tkinter.Frame(root)
		Bframe1.grid(row=2,column=coluna)
		btn1a = Tkinter.Button(Bframe1,text="Todos", relief="groove",activebackground="#ED2139", 	            bg="darkred",fg="white",bd=4, command=ativarTUDO)
		btn1a.grid(row=1,column=1)
		btn1b = Tkinter.Button(Bframe1,text="Limpa", relief="groove",activebackground="#ED3921", 	bg="brown",fg="white",bd=4, command=desativarTUDO)
		btn1b.grid(row=1,column=2)

		








a=Celula(root,1,pesquisa,"Pesquisa",cor1)
b=Celula (root,2,controle,"Controle",cor2)
c=Celula (root,3,idade,"Faixa etária",cor3)
d=Celula (root,4,historia,"Tipo de História",cor4)
e=Celula (root,5,gramatica,"Classe de Palavra",cor5)


def leiaA():
	a.leia=True



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
helpmenu.add_command(label="Gerar", command=leiaA)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Gerar", menu=helpmenu)

root.config(menu=menubar)

################################



root.mainloop()

