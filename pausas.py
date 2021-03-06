# -*- coding: utf-8 -*-


from Tkinter import *
import tkMessageBox
import Tkinter, tkFileDialog
import os
import ScrolledText
import codecs
import locale
import os
language, output_encoding = locale.getdefaultlocale()

#importa a estrutura filtrada original e as funções de filtro
from filtra_estrutura import *
from configs import * #importa paths



######## funcoes globais DE AVISO TKINTER

def donothing():
	tkMessageBox.showinfo("Pronto!", "Os relatorios ja foram gerados e estao no diretorio " )

def janeladeaviso(texto):
	tkMessageBox.showinfo("Pronto!",texto)


########################### MONTA JANELA PRINCIPAL

root = Tk()
root.title("Tipos de Relatório")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

root.geometry("%dx%d+0+0" % (w, h))


######################### listas das celulas

sujeitos=[]

for i in EstruturaF.keys():
	sujeitos.append(i)

grupos=["Pesquisa","Controle"]
idade=["7 anos","8 anos","9 anos","10 anos"] 
historia=[u'Mecânica1',u'Mecânica2',"Comportamental1","Comportamental2","Intencional"]
gramatica=[u'substantivo', u'adjetivo', u'verbo', u'conjunção', u'preposição', u'pronome',u'artigo', u'ruptura',u'interjeição',u'advérbio',u'indeterminado',u'numeral']
sexo=["Masculino","Feminino"]

########### cores das celulas
cor1="#BFACC5"
cor2="#BFBEA2"
cor3="#FBBEA2"
cor4="#BFAAA2"
cor5="#85ADA2"
cor6="#FBEC5D"
###################################################################################################





######### CLASSE que define a celula de itens com botoes de seleciona tudo/nada e todos itens dentro


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
################################################################### FIM DA CLASSE CÉLULA


#MONTA O FRAME DAS CELULAS DE ESCOLHA##################################

a=Celula(root,0,sujeitos,cor1)
b=Celula (root,1,grupos,cor2)
c=Celula (root,2,idade,cor3)
d=Celula (root,3,historia,cor4)
e=Celula (root,4,gramatica,cor5)
f=Celula (root,5,sexo,cor6)

atual=[a.CELULAtual(),b.CELULAtual(),c.CELULAtual(),d.CELULAtual(),e.CELULAtual(),f.CELULAtual()]
#############################################





############## chama a função que atualizará todas médias
mediaN=MediasTodasNarrativas()

###### funções para converter tags para nome expandido - exemplo: de P para Pesquisa de F para Feminino
def expandeGrupo(tag):
	t=''
	if tag == 'P':
		t='Pesquisa'
	if tag == 'C':
		t='Controle'
	return t

def expandeSexo(tag):
	t=''
	if tag == 'M':
		t='Masculino'
	if tag == 'F':
		t='Feminino'
	return t

def expandeIdade(tag):
	t=''
	t1=tag.split('a')
	t2=t1[1].split('m')
	if t2[0] != '':
		t=t1[0]+" Anos e "+t2[0]+" Meses"
	else:
		t=t1[0]+" Anos"

	return t

def expandeHistoria(tag):
	h=''
	if tag == u'M1':
		h=u'Mecânica1'
	if tag == u'M2':
		h=u'Mecânica2'
	if tag == u'C1':
		h=u'Comportamental1'
	if tag == u'C2':
		h=u'Comportamental2'
	if tag == u'I1':
		h=u'Intencional'
	return h
		

def ordena_amostras(nome):
	a=[]
	
	for k in EstruturaF[nome][0]:
		a.append(("Media "+ expandeHistoria(k['Narrativa'])+ " " + k['Amostra'] , k['MediaGeral']))

	a.sort()
	
	return a


ordem_amostras=u'\"Media Comportamental1 A1\",\"Media Comportamental1 A2\",\"Media Comportamental1 A3\",\"Media Comportamental2 A1\",\"Media Comportamental2 A2\",\"Media Comportamental2 A3\",\"Media Intencional A1\",\"Media Intencional A2\",\"Media Intencional A3\",\"Media Mec\xe2nica1 A1\",\"Media Mec\xe2nica1 A2\",\"Media Mec\xe2nica1 A3\",\"Media Mec\xe2nica2 A1\",\"Media Mec\xe2nica2 A2\",\"Media Mec\xe2nica2 A3\"'




############ filtros do clipboard

def filtraSujeito():
	text.delete(0.0,END)
	if a.CELULAtual():
		for celula_item in a.CELULAtual():
			for i in EstruturaF.keys():
				if (celula_item == i): 
					text.insert(INSERT, 
					"Nome: "+ i +"\n" +
					"Idade: "+ expandeIdade(EstruturaF[i][1]['Idade']) + "\n"+
					"Sexo: "+ expandeSexo(EstruturaF[i][1]['Sexo']) + "\n"+
					"Grupo: "+ expandeGrupo(EstruturaF[i][1]['Grupo']) + "\n" +
					"Media Geral: " + str(EstruturaF[i][1]['MediaGeralTotal'])+"\n"
					)
					o=ordena_amostras(i)
					for k in o:
						text.insert (INSERT, k[0] + " " + str(k[1]) + "\n")
			text.insert(INSERT,"\n")



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
			text.insert(INSERT, celula_item +"\n----------------\n")
			for i in EstruturaF.keys():
				if (grupo == (EstruturaF[i][1]['Grupo'])): 
					text.insert(INSERT, 
					"Nome: "+ i +"\n" +
					"Idade: "+ expandeIdade(EstruturaF[i][1]['Idade']) + "\n"+
					"Sexo: "+ expandeSexo(EstruturaF[i][1]['Sexo']) + "\n"+
					"Grupo: "+ expandeGrupo(EstruturaF[i][1]['Grupo']) + "\n" +
					"Media Geral: " + str(EstruturaF[i][1]['MediaGeralTotal'])+"\n\n"
					)
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
			text.insert(INSERT, celula_item +"\n----------------\n")
			for i in EstruturaF.keys():
				if (idade == ((EstruturaF[i][1]['Idade']).split('a'))[0]): #so a idade em anos corta depois
					text.insert(INSERT, 
					"Nome: "+ i +"\n" +
					"Idade: "+ expandeIdade(EstruturaF[i][1]['Idade']) + "\n"+
					"Sexo: "+ expandeSexo(EstruturaF[i][1]['Sexo']) + "\n"+
					"Grupo: "+ expandeGrupo(EstruturaF[i][1]['Grupo']) + "\n" +
					"Media Geral: " + str(EstruturaF[i][1]['MediaGeralTotal'])+"\n\n"
					)
	c.CELULAlimpa()


def filtraHistoria():
	text.delete(0.0,END)
	if d.CELULAtual():
		for i in EstruturaF.keys():
			text.insert(INSERT, "Nome: "+ i + "\n------------------\n")
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
				text.insert(INSERT, "Media "+ celula_item +": " + str(mediaN[i][h]) + "\n")
			text.insert(INSERT, "\n")
	d.CELULAlimpa()



def filtraGramatica():
	text.delete(0.0,END)
	if e.CELULAtual():
		for i in EstruturaF.keys():
			text.insert(INSERT, "Nome:"+ i + "\n"+"----------------\n")
			for celula_item in e.CELULAtual():
				text.insert(INSERT, "Media "+ celula_item +": " + str(MediasGramaticas(EstruturaF,i,celula_item)) + "\n")
			text.insert(INSERT, "\n")
	e.CELULAlimpa()

def filtraSexo():
	text.delete(0.0,END)
	if f.CELULAtual():
		for celula_item in f.CELULAtual():
			if celula_item == 'Masculino':
				sexo='M'
			if celula_item == 'Feminino':
				sexo='F'	
			else:
				pass
			text.insert(INSERT, celula_item +"\n----------------\n")
			for i in EstruturaF.keys():
				if (sexo == EstruturaF[i][1]['Sexo']):
					text.insert(INSERT, 
					"Nome: "+ i +"\n" +
					"Idade: "+ expandeIdade(EstruturaF[i][1]['Idade']) + "\n"+
					"Grupo: "+ expandeGrupo(EstruturaF[i][1]['Grupo']) + "\n" +
					"Media Geral: " + str(EstruturaF[i][1]['MediaGeralTotal'])+"\n\n"
					)
	f.CELULAlimpa()

################# CSV #################################################


def CSVfiltraSujeito():
	text.delete(0.0,END)
	csv="Nome,Idade,Grupo,Sexo,\"Media Geral\","+ordem_amostras+"\n"
	if a.CELULAtual():
		for celula_item in a.CELULAtual():
			for i in EstruturaF.keys():
				if (celula_item == i): 
					csv=csv+ str("\""+i +"\""+","+ "\""+expandeIdade(EstruturaF[i][1]['Idade'])+"\""+ ","+expandeGrupo(EstruturaF[i][1]['Grupo']) + "," + expandeSexo(EstruturaF[i][1]['Sexo']) + "," + str(EstruturaF[i][1]['MediaGeralTotal']))

					o=ordena_amostras(i)
					for k in o:
						csv=csv+","+str(k[1])
			csv=csv+"\n"
	
	csv=csv.encode('utf-8')
	msg="Gravado arquivo PAUSASporSujeito.csv"
	text.insert(INSERT, msg)
	dados=open(CSVpath+'PAUSASporSujeito.csv','w')
	dados.write(csv)
	janeladeaviso(msg)
	a.CELULAlimpa()


def CSVfiltraGrupo():
	text.delete(0.0,END)
	csv="Nome,Idade,Grupo,Sexo,\"Media Geral\"\n"
	if b.CELULAtual():
		for celula_item in b.CELULAtual():
			if celula_item == 'Pesquisa':
				grupo='P'
			if celula_item == 'Controle':
				grupo='C'	
			else:
				pass
			for i in EstruturaF.keys():
				if (grupo == (EstruturaF[i][1]['Grupo'])): 
					csv=csv+str("\""+i +"\""+","+ "\""+expandeIdade(EstruturaF[i][1]['Idade'])+"\""+ ","
					+expandeGrupo(EstruturaF[i][1]['Grupo']) + "," + expandeSexo(EstruturaF[i][1]['Sexo']) + "," +str(EstruturaF[i][1]['MediaGeralTotal'])+ "\n")

	csv=csv.encode('utf-8')
	msg="Gravado arquivo PAUSASporGrupo.csv"
	text.insert(INSERT, msg)
	dados=open(CSVpath+'PAUSASporGrupo.csv','w')
	dados.write(csv)
	janeladeaviso(msg)
	b.CELULAlimpa()


def CSVfiltraIdade():
	text.delete(0.0,END)
	csv="Nome,Idade,Grupo,Sexo,\"Media Geral\"\n"
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
				if (idade == ((EstruturaF[i][1]['Idade']).split('a'))[0]): #so a idade em anos corta depois
					csv=csv+str("\""+i +"\""+","+ "\""+expandeIdade(EstruturaF[i][1]['Idade'])+"\""+ ","
					+expandeGrupo(EstruturaF[i][1]['Grupo']) + "," + expandeSexo(EstruturaF[i][1]['Sexo']) + "," +str(EstruturaF[i][1]['MediaGeralTotal'])+ "\n")

	csv=csv.encode('utf-8')
	msg="Gravado arquivo PAUSASporIdade.csv"
	text.insert(INSERT, msg)
	dados=open(CSVpath+'PAUSASporIdade.csv','w')
	dados.write(csv)
	janeladeaviso(msg)
	c.CELULAlimpa()


def CSVfiltraHistoria():
	text.delete(0.0,END)
	csv=''
	if d.CELULAtual():
		for i in EstruturaF.keys():
			csv=csv+u'Nome,'+"\""+ i +"\""+"\n"
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
				csv=csv+celula_item +"," + str(mediaN[i][h]) + "\n"
			csv=csv+"\n"
		
	csv=csv.encode('utf-8')
	msg="Gravado arquivo PAUSASHistoria.csv"
	text.insert(INSERT, msg)
	dados=open(CSVpath+'PAUSASporHistoria.csv','w')
	dados.write(csv)
	dados.close()
	janeladeaviso(msg)
	d.CELULAlimpa()

def CSVfiltraGramatica():
	text.delete(0.0,END)
	csv=''
	if e.CELULAtual():
		for i in EstruturaF.keys():
			csv=csv+u'Nome,'+"\""+ i +"\""+"\n"
			for celula_item in e.CELULAtual():
				csv=csv+celula_item+","+ str(MediasGramaticas(EstruturaF,i,celula_item)) +"\n"
			csv=csv+"\n"

	csv=csv.encode('utf-8')
	msg="Gravado arquivo PAUSASGramatica.csv"
	text.insert(INSERT, msg)
	dados=open(CSVpath+'PAUSASporGramatica.csv','w')
	dados.write(csv)
	dados.close()
	janeladeaviso(msg)
	e.CELULAlimpa()


def CSVfiltraSexo():
	text.delete(0.0,END)
	csv="Nome,Idade,Grupo,Sexo,\"Media Geral\"\n"
	if f.CELULAtual():
		for celula_item in f.CELULAtual():
			if celula_item == 'Masculino':
				sexo='M'
			if celula_item == 'Feminino':
				sexo='F'	
			else:
				pass
			for i in EstruturaF.keys():
				if (sexo == EstruturaF[i][1]['Sexo']):
					csv=csv+str("\""+i +"\""+","+ "\""+expandeIdade(EstruturaF[i][1]['Idade'])+"\""+ ","
					+expandeGrupo(EstruturaF[i][1]['Grupo']) + "," + celula_item + "," +
					str(EstruturaF[i][1]['MediaGeralTotal'])+ "\n"
					)

	csv=csv.encode('utf-8')
	msg="Gravado arquivo PAUSASporSexo.csv"
	text.insert(INSERT, msg)
	dados=open(CSVpath+'PAUSASporSexo.csv','w')
	dados.write(csv)
	janeladeaviso(msg)
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

SALVAR = Menu(menubar, font=("Arial",20),activebackground="yellow", tearoff=0)
SALVAR.add_command(label="Relatório por Sujeito", command=CSVfiltraSujeito)
SALVAR.add_command(label="Relatório por Grupo", command=CSVfiltraGrupo)
SALVAR.add_command(label="Relatório por Idade", command=CSVfiltraIdade)
SALVAR.add_command(label="Relatório por História", command=CSVfiltraHistoria)
SALVAR.add_command(label="Relatório por Gramática", command=CSVfiltraGramatica)
SALVAR.add_command(label="Relatório por Sexo", command=CSVfiltraSexo)
SALVAR.add_command(label="Limpa", command=limpa)
menubar.add_cascade(label="Salvar", menu=SALVAR)

root.config(menu=menubar)

################################ CLIPBOARD
#Tframe=Tkinter.Frame(root,height="100")
#Tframe.grid(row=3,column=0,columnspan=6,sticky=W)



Tscroll = Scrollbar(root)
#Tscroll.grid(row=3,column=0,sticky=N+S+E,ipadx="7")



text = Text(root,wrap=WORD,yscrollcommand=Tscroll.set, foreground="black",background="white", width="100",height="18",bd=5,font=("Arial",12))
#text.insert(INSERT, atual)
#text.delete(0.0,END) #limpa

Tscroll.config(command=text.yview) #ativa o scroll dentro do texto
text.grid(row=3,column=1,columnspan=6,sticky=N+W,)

####################### LOOP Tkinter ROOT

root.mainloop()



