# coding: utf-8

from Tkinter import *
import tkMessageBox
import Tkinter, tkFileDialog
import tkMessageBox
import os
import ScrolledText
from data import * #importa a Estrutura
from filtro import *



homedir = os.path.expanduser('~') 

root = Tk()
root.title("Tipos de Relatório")

#
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#
# use the next line if you also want to get rid of the titlebar
#
#root.overrideredirect(1)
#
root.geometry("%dx%d+0+0" % (w, h))

#var = IntVar()

######## funcoes globais


"""
def newDIR():
	dirname = tkFileDialog.askdirectory(parent=root,initialdir=homedir,title='Selecione o diretorio de trabalho')
	if len(dirname ) > 0:
		msg= "Escolhestes" + dirname 
		print dirname
		#tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " + dirname)
		

def EscolheDIR():
	a=tkMessageBox.askquestion("Confirmar Diretorio", "O diretorio e trabalho é "+ homedir + " ?")
	if a == "no":
		newDIR()
"""

####### Janelas de Aviso:

def donothing():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )




	

######################### listas teste #############################################################################

pesquisa=["Brenda","Jarbas","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina"]
controle=["Felipe Moreno","Tininha","Thiago","Ricardo","Augusto","Manoel"]
idade=["7 anos","8 anos","9 anos","10 anos"] 

#amostras=["Mecânica1 (A1)","Mecânica1 (A2)","Mecânica1 (A3)","Mecânica2 (A1)","Mecânica2 (A2)","Mecânica2 (A3)","Comportamental1 (A1)","Comportamental1 (A2)","Comportamental1 (A3)","Comportamental2 (A1)","Comportamental2 (A2)","Comportamental2 (A3)","Intencional (A1)","Intencional (A2)","Intencional (A3)"]

historia=["Mecânica1","Mecânica2","Comportamental1","Comportamental2","Intencional"]


gramatica=["substantivo","verbo","adjetivo","advérbio","conjunção","preposição","pronome"]
sexo=["masculino","feminino"]
##############################

########### cores das celulas
cor1="#BFACC5"
cor2="#BFBEA2"
cor3="#FBBEA2"
cor4="#BFAAA2"
cor5="#85ADA2"
cor6="#FBEC5D"
#####################################################################################################################





######### Classe que define a celula de itens com botoes de seleciona tudo/nada e todos itens dentro


class Celula:
	def __init__(self,root,coluna,listadeitens,cor,es):
		
		

		F1=Tkinter.Frame(root,width="12",bd="5")
		F1.grid(row=1,column=coluna)

		nomelabels=["Pesquisa","Controle","Faixa Etária","Sexo","Tipos de História","Classes de Palavras"]
		tiposchave=["pesquisa","controle","idade","historia","classes","sexo"]

		tipo=tiposchave[coluna] #para uso nos eventos - lembrar que as colunas começam em 1


		label=Tkinter.Label(F1, text=nomelabels[coluna]) #lembrar que s colunas começam em 1
		label.pack()

		scrollbar1 = Scrollbar(F1)
		scrollbar1.pack( side = RIGHT, fill=Y )

		lbox = Listbox(F1,selectmode=MULTIPLE,yscrollcommand = scrollbar1.set, exportselection=es)
		#exportselection=0 para multiplas instancias funcionarem independentes, 1 para dependentes 

		# insere os elementos na lista
		for i in listadeitens:
			lbox.insert(len(listadeitens), i)
		
		

		#### funções de leitura interna da celula
		tamanhodalista = len(listadeitens)

		self.CELULA={}

		def ativarTUDO():
			lbox.selection_set(0,tamanhodalista)
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			self.CELULA=CELitens
			
			

		def desativarTUDO():
			lbox.selection_clear(0,tamanhodalista)
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			self.CELULA=CELitens
			

		def ler(event):
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			self.CELULA=CELitens
			

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

	def CELULAtual(self):
		return self.CELULA
############################################################################################################

#rotinas da interface	

### detectar se existem 15 amostras ################################

nomes=Nomes()
AUP_ok=ChecarErrosAmostras()

def checkerror():
	for n in AUP_ok:
		if AUP_ok[n] == False:
			tkMessageBox.showerror("Arquivos .aup defeituosos", n + " apresenta erros de digitação:\nConfira novamente as amostras " )


# insere os sujeitos LEMBRE DE MODIFICAR ESTA FUNÇÃO USANDO A EstruturaFiltrada()
pesquisa=[]
controle=[]
antesentrada=''
for entrada in Estrutura:
	if (entrada['Grupo'] == "P"):
		if entrada['Nome'] != antesentrada:
			pesquisa.append(entrada['Nome'])
	if (entrada['Grupo'] == "C"):
		if entrada['Nome'] != antesentrada:
			controle.append(entrada['Nome'])
	antesentrada=entrada['Nome']
	
				








#insere as celulas de filtros Listbox no root frame! #####################################

Pesquisa=Celula(root,0,pesquisa,cor1,0)
Controle=Celula (root,1,controle,cor2,0)
Idade=Celula (root,2,idade,cor3,1)
Historia=Celula (root,4,historia,cor5,1)
Gramatica=Celula (root,5,gramatica,cor6,1)
#########################################################################

	

def filtraSujeito():
	for celula_cheia in [Pesquisa.CELULAtual(),Controle.CELULAtual()]:
		for celula_item in celula_cheia:
			for estrutura_item in Estrutura:
				if (celula_item == estrutura_item['Nome']):
					text.insert(INSERT, str(estrutura_item['Nome']+'\n'))

Amostras_Sujeito=EstruturaFiltrada()

def filtraIdade():
	for celula_item in Idade.CELULAtual():
		for estrutura_item in Estrutura:
			if (celula_item.split(' ')[0] == estrutura_item['Idade'].split('a')[0]): #separa o numero da idade
				text.insert(INSERT, str(estrutura_item['Nome']+'\n'))	

def filtraHistoria():



def filtraGramatica():





			


# imprimindo lista de todos dicionarios com sinal capturado por fora das celulas
def leiatudo():

	filtraSujeito()
	text.insert(INSERT, "\n")
	#text.insert(INSERT, a.CELULAtual())
	#return atual

def limpa():
	global text
	text.delete(0.0,END)




################### MENU

menubar = Menu(root,bg="#AfAfAf",font=("Arial",12))

GERAR = Menu(menubar, font=("Arial",20),activebackground="yellow", tearoff=0)
GERAR.add_command(label="Media por Sujeito", command=filtraSujeito)
GERAR.add_command(label="Media por Idade", command=filtraIdade)
GERAR.add_command(label="Checa erros", command=checkerror)
GERAR.add_command(label="Limpa", command=limpa)
menubar.add_cascade(label="Gerar", menu=GERAR)

root.config(menu=menubar)

################################
#Tframe=Tkinter.Frame(root,height="100")
#Tframe.grid(row=3,column=0,columnspan=6,sticky=W)


Tscroll = Scrollbar(root)
Tscroll.grid(row=3,column=0,sticky=N+S+E,ipadx="7")



text = Text(root,wrap=WORD,yscrollcommand=Tscroll.set, width="100",height="18",bd=5,font=("Arial",12))
#########################################
#text.insert(INSERT, atual)
#text.insert(END, "Insere no final")
#########################################

Tscroll.config(command=text.yview) #ativa o scroll dentro do texto
text.grid(row=3,column=1,columnspan=6,sticky=N+W,)






root.mainloop()

