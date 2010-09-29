# coding: utf-8

from Tkinter import *
import tkMessageBox
import Tkinter, tkFileDialog
import tkMessageBox
import os
import ScrolledText
#from data import *


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


todasamostras=["Mecânica1 (A1)","Mecânica1 (A2)","Mecânica1 (A3)","Mecânica2 (A1)","Mecânica2 (A2)","Mecânica2 (A3)","Comportamental1 (A1)","Comportamental1 (A2)","Comportamental1 (A3)","Comportamental2 (A1)","Comportamental2 (A2)","Comportamental2 (A3)","Intencional (A1)","Intencional (A2)","Intencional (A3)"]

"""


def donothing():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )

######################### listas teste

sujeitos=["Brenda","Felipe Moreno","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina","Marcelo","Jarbas","Jonas","Luana","Solange","Janaina"]
grupos=["Pesquisa","Controle"]
idade=["7 anos","8 anos","9 anos","10 anos"] 
historia=[u'Mecânica1',u'Mecânica2',"Comportamental1","Comportamental2","Intencional"]
gramatica=["substantivo","verbo","adjetivo",u'advérbio',u'conjunção',u'preposição',u'pronome']
sexo=["masculino","feminino"]
##############################

########### cores das celulas
cor1="#BFACC5"
cor2="#BFBEA2"
cor3="#FBBEA2"
cor4="#BFAAA2"
cor5="#85ADA2"
cor6="#FBEC5D"
########################################





######### funcao que define a celula de itens com botoes de seleciona tudo/nada e todos itens dentro


class Celula:
	def __init__(self,root,coluna,listadeitens,cor):
		
		

		F1=Tkinter.Frame(root,width="12",bd="5")
		F1.grid(row=1,column=coluna)

		nomelabels=["Sujeitos","Grupos","Faixa Etária","Tipos de História","Classes de Palavras","Sexo"]
		tiposchave=["sujeitos","grupos","idade","historia","classes","sexo"]

		tipo=tiposchave[coluna] #para uso nos eventos - lembrar que as colunas começam em 1


		label=Tkinter.Label(F1, text=nomelabels[coluna]) #lembrar que s colunas começam em 1
		label.pack()

		scrollbar1 = Scrollbar(F1)
		scrollbar1.pack( side = RIGHT, fill=Y )

		lbox = Listbox(F1,selectmode=MULTIPLE,yscrollcommand = scrollbar1.set, exportselection=1)
		#exportselection=0 para multiplas instancias funcionarem independentes
		#exportselection=1 para multiplas instancias funcionarem individuais

		# insere os elementos na lista
		for i in listadeitens:
			lbox.insert(len(listadeitens), i)
		
		

		#### funções de leitura interna da celula
		tamanhodalista = len(listadeitens)

		self.CELULA={}

		def ativarTUDO():
			lbox.selection_set(0,tamanhodalista)
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			#self.CELULA={tipo:CELitens}
			self.CELULA=CELitens
			#print self.CELULA
			

		def desativarTUDO():
			lbox.selection_clear(0,tamanhodalista)
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			#self.CELULA={tipo:CELitens}
			self.CELULA=CELitens
			#print self.CELULA

		def ler(event):
			#print [lbox.get(i) for i in lbox.curselection()]
			CELitens=[lbox.get(i) for i in lbox.curselection()]
			#self.CELULA={tipo:CELitens}
			self.CELULA=CELitens
			#print self.CELULA

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

	def CELULAlimpa(self):
		self.CELULA=[]
		return self.CELULA
	


#EscolheDIR()

a=Celula(root,0,sujeitos,cor1)
b=Celula (root,1,grupos,cor2)
c=Celula (root,2,idade,cor3)
d=Celula (root,3,historia,cor4)
e=Celula (root,4,gramatica,cor5)
f=Celula (root,5,sexo,cor6)

atual=[a.CELULAtual(),b.CELULAtual(),c.CELULAtual(),d.CELULAtual(),e.CELULAtual(),f.CELULAtual()]





from filtra import *

mediaN=MediasTodasNarrativas()

def filtraSujeito():
	text.delete(0.0,END)
	if a.CELULAtual():
		for celula_item in a.CELULAtual():
			for i in EstruturaF.keys():
				if (celula_item == i):
					text.insert(INSERT, str(EstruturaF[i][1]) + "\nNARRATIVAS: " + str(mediaN[i]) + "\n\n")
	a.CELULAlimpa()	

def filtraGrupo():
	text.delete(0.0,END)
	if b.CELULAtual():
		for celula_item in b.CELULAtual():
			if celula_item == 'Pesquisa':
				grupo='P'
			if celula_item == 'Controle':
				grupo='C'	
			else:
				pass
			for i in EstruturaF.keys():
				if (grupo == EstruturaF[i][1]['Grupo']):
					text.insert(INSERT, str(EstruturaF[i][1]) + "\nNARRATIVAS: " + str(mediaN[i]) + "\n\n")
	b.CELULAlimpa()


def filtraIdade():
	text.delete(0.0,END)
	if c.CELULAtual():	
		for celula_item in c.CELULAtual():
			if celula_item == '7 anos':
				idade='7'
			if celula_item == '8 anos':
				idade='8'
			if celula_item == '9 anos':
				idade='9'
			if celula_item == '10 anos':
				idade='10'
			else:
				pass
			for i in EstruturaF.keys():
				if (idade == ((EstruturaF[i][1]['Idade']).split('a'))[0]): #so a idade em anos corta depois do a
					text.insert(INSERT, str(EstruturaF[i][1]) + "\nNARRATIVAS: " + str(mediaN[i]) + "\n\n")
	c.CELULAlimpa()

def filtraHistoria():
	text.delete(0.0,END)
	if d.CELULAtual():	
		for celula_item in d.CELULAtual():
			if celula_item == u'Mecânica1':
				h='M1'
			if celula_item == u'Mecânica2':
				h='M2'
			if celula_item == u'Comportamental1':
				h='C1'
			if celula_item == u'Comportamental2':
				h='C2'
			if celula_item == u'Intencional':
				h='I1'
			else:
				pass
			
			for i in EstruturaF.keys():
				text.insert(INSERT, str(EstruturaF[i][1]['Nome']) + "\nMedia "+ celula_item +": " + str(mediaN[i][h]) + "\n\n")
	d.CELULAlimpa()

def filtraGramatica():
	text.delete(0.0,END)
	if e.CELULAtual():	
		for celula_item in e.CELULAtual():
			for i in EstruturaF.keys():
				text.insert(INSERT, str(EstruturaF[i][1]['Nome']) + "\nMedia "+ celula_item +": " + str(EstruturaF[i][1]['MediaDasClasses'][celula_item]) + "\n\n")
	e.CELULAlimpa()

def filtraSexo():
	text.delete(0.0,END)
	if f.CELULAtual():
		for celula_item in f.CELULAtual():
			if celula_item == 'masculino':
				sexo='M'
			if celula_item == 'feminino':
				sexo='F'	
			else:
				pass
			for i in EstruturaF.keys():
				if (sexo == EstruturaF[i][1]['Sexo']):
					text.insert(INSERT, str(EstruturaF[i][1]) + "\nNARRATIVAS: " + str(mediaN[i]) + "\n\n")
	f.CELULAlimpa()














def limpa():
	global text
	text.delete(0.0,END)


################### MENU

menubar = Menu(root,bg="#AfAfAf",font=("Arial",12))

GERAR = Menu(menubar, font=("Arial",20),activebackground="yellow", tearoff=0)
GERAR.add_command(label="Relatório por Sujeito", command=filtraSujeito)
GERAR.add_command(label="Relatório por Grupo", command=filtraGrupo)
GERAR.add_command(label="Relatório por Idade", command=filtraIdade)
GERAR.add_command(label="Relatório por História", command=filtraHistoria)
GERAR.add_command(label="Relatório por Gramática", command=filtraGramatica)
GERAR.add_command(label="Relatório por Sexo", command=filtraSexo)
GERAR.add_command(label="Limpa", command=limpa)
menubar.add_cascade(label="Gerar", menu=GERAR)
menubar.add_cascade(label="Salvar")
menubar.add_cascade(label="Salvar", command=limpa)

root.config(menu=menubar)

################################
#Tframe=Tkinter.Frame(root,height="100")
#Tframe.grid(row=3,column=0,columnspan=6,sticky=W)

Tscroll = Scrollbar(root)
Tscroll.grid(row=3,column=0,sticky=N+S+E,ipadx="7")


text = Text(root,wrap=WORD,yscrollcommand=Tscroll.set, width="100",height="18",bd=5,font=("Arial",12))
text.insert(INSERT, atual)
#text.insert(END, "Insere no final")

Tscroll.config(command=text.yview) #ativa o scroll dentro do texto
text.grid(row=3,column=1,columnspan=6,sticky=N+W,)






root.mainloop()

