# -*- coding: utf-8 -*-

from configs import * #importa paths
from Tkinter import *
import tkMessageBox
import Tkinter, tkFileDialog
import tkMessageBox

from gui_filters import *



root = Tk()
root.title("Tipos de Relatório")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


######## AVISOS

def donothing():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )

def janeladeaviso(texto):
	tkMessageBox.showinfo("Pronto!",texto)

######################### listas teste
sujeitos=["Nome", "Nome2", "Nome3", "Guilherme"]
grupos=["Pesquisa","Controle"]
idade=["7 anos","8 anos","9 anos","10 anos"] 
historia=[u'Mecânica1',u'Mecânica2',"Comportamental1","Comportamental2","Intencional"]
gramatica=["substantivo","verbo","adjetivo",u'conjunção',u'preposição',u'pronome']
sexo=["Masculino","Feminino"]
##############################

########### cores das celulas
cor1="#BFACC5"
cor2="#BFBEA2"
cor3="#FBBEA2"
cor4="#BFAAA2"
cor5="#85ADA2"
cor6="#FBEC5D"
##############




######### funcao que define a celula de itens com botoes de seleciona tudo/nada e todos itens dentro


class Celula:
	def __init__(self,root,coluna,listadeitens,cor):
# instancia o frame e monta as celulas
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

SALVAR = Menu(menubar, font=("Arial",20),activebackground="yellow", tearoff=0)
SALVAR.add_command(label="Relatório por Sujeito", command=CSVfiltraSujeito)
SALVAR.add_command(label="Relatório por Grupo", command=CSVfiltraGrupo)
SALVAR.add_command(label="Relatório por Idade", command=CSVfiltraIdade)
SALVAR.add_command(label="Relatório por História", command=CSVfiltraHistoria)
SALVAR.add_command(label="Relatório por Gramática", command=CSVfiltraGramatica)
SALVAR.add_command(label="Relatório por Sexo", command=CSVfiltraSexo)
SALVAR.add_command(label="Limpa", command=limpa)
menubar.add_cascade(label="Salvar", menu=SALVAR)

RENDER = Menu(menubar, font=("Arial",20),activebackground="red", tearoff=0)
RENDER.add_command(label="Nova Renderização", command=rendershell)
menubar.add_cascade(label="R​enderiza", menu=RENDER)




root.config(menu=menubar)

################################
#Tframe=Tkinter.Frame(root,height="100")
#Tframe.grid(row=3,column=0,columnspan=6,sticky=W)



Tscroll = Scrollbar(root)
Tscroll.grid(row=3,column=0,sticky=N+S+E,ipadx="7")



text = Text(root,wrap=WORD,yscrollcommand=Tscroll.set, width="100",height="18",bd=5,font=("Arial",12))
#text.insert(INSERT, atual)
#text.delete(0.0,END) #limpa

Tscroll.config(command=text.yview) #ativa o scroll dentro do texto
text.grid(row=3,column=1,columnspan=6,sticky=N+W,)

root.mainloop()



