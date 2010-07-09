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

######################### listas teste

pesquisa=["Marcelo","Jarbas","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina"]
controle=["Simone","Tininha","Thiago","Ricardo","Augusto","Manoel"]
idade=["2 anos","3 anos","4 anos","5 anos","6 anos","7 anos","8 anos","9 anos","10 anos"] 
historia=["Mecânica1 (A1)","Mecânica1 (A2)","Mecânica1 (A3)","Mecânica2 (A1)","Mecânica2 (A2)","Mecânica2 (A3)","Comportamental1 (A1)","Comportamental1 (A2)","Comportamental1 (A3)","Comportamental2 (A1)","Comportamental2 (A2)","Comportamental2 (A3)","Intencional (A1)","Intencional (A2)","Intencional (A3)"]
gramatica=["substantivo","verbo","adjetivo","advérbio","conjunção","preposição","pronome"]
##############################

########### cores das celulas
cor1="#BFACC5"
cor2="#BFBEA2"
cor3="#FBBEA2"
cor4="#BFAAA2"
cor5="#85ADA2"
########################################





######### funcao que define a celula de itens com botoes de seleciona tudo/nada e todos itens dentro


class Celula:
	def __init__(self,root,coluna,listadeitens,cor):


		F1=Tkinter.Frame(root)
		F1.grid(row=1,column=coluna)

		nomelabels=["Pesquisa","Controle","Faixa Etária","Tipos de História","Classes de Palavras"]
		tiposchave=["pesquisa","controle","idade","historia","classes"]

		tipo=tiposchave[coluna -1] #para uso nos eventos - lembrar que as colunas começam em 1


		label=Tkinter.Label(F1, text=nomelabels[coluna-1]) #lembrar que s colunas começam em 1
		label.pack()

		scrollbar1 = Scrollbar(F1)
		scrollbar1.pack( side = RIGHT, fill=Y )

		lbox = Listbox(F1,selectmode=MULTIPLE,yscrollcommand = scrollbar1.set, exportselection=0)
		#exportselection=0 para multiplas instancias funcionarem independentes

		# insere os elementos na lista
		for i in listadeitens:
			lbox.insert(len(listadeitens), i)
		
		

		#### funções de leitura interna da celula
		tamanhodalista = len(listadeitens)

		self.CELULA={}

		def ativarTUDO():
			lbox.selection_set(0,tamanhodalista)
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			self.CELULA={tipo:CELitens}
			print self.CELULA
			

		def desativarTUDO():
			lbox.selection_clear(0,tamanhodalista)
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			self.CELULA={tipo:CELitens}
			print self.CELULA

		def ler(event):
			#print [lbox.get(i) for i in lbox.curselection()]
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			self.CELULA={tipo:CELitens}
			print self.CELULA

		#######################################################




		lbox.bind("<ButtonRelease-1>", ler ) #le o botao do mouse quando solta

		lbox.config(bg=cor, font=("Helvetica",12) ) #configs da lista

		####### fecha a celula e o scroll
		lbox.pack(side = RIGHT, fill = BOTH)
		scrollbar1.config( command = lbox.yview )
		
		
		####### botoes#####################
		Bframe1=Tkinter.Frame(root)
		Bframe1.grid(row=2,column=coluna)
		btn1a = Tkinter.Button(Bframe1,text="Todos", relief="groove",activebackground="#ED2139", 	            bg=cor,fg="#050505",bd=4, command=ativarTUDO)
		btn1a.grid(row=1,column=1)
		btn1b = Tkinter.Button(Bframe1,text="Limpa", relief="groove",activebackground="#ED3921", 	bg=cor,fg="#050505",bd=4, command=desativarTUDO)
		btn1b.grid(row=1,column=2)

		








a=Celula(root,1,pesquisa,cor1)
b=Celula (root,2,controle,cor2)
c=Celula (root,3,idade,cor3)
d=Celula (root,4,historia,cor4)
e=Celula (root,5,gramatica,cor5)


def leiatudo():
	pass




################### MENU

menubar = Menu(root,bg="#AfAfAf",font=("Arial",12))

GERAR = Menu(menubar, font=("Arial",20),activebackground="yellow", tearoff=0)
GERAR.add_command(label="Média entre os selecionados abaixo", command=leiatudo)
GERAR.add_command(label="Relatório Geral dos selecionados abaixo", command=donothing)
menubar.add_cascade(label="Gerar", menu=GERAR)

root.config(menu=menubar)

################################



root.mainloop()

