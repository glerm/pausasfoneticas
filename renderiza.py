# -*- coding: utf-8 -*-

#arquivo teste:
#arq='teste.aup'

from BeautifulSoup import BeautifulSoup
import string
import re
import sys
import codecs
import locale
import os, glob
import numpy




def calendario(): #dia da execucao do codigo, formatado
	import time
	import datetime
	from time import gmtime, strftime
	c=strftime("%A, %d %b %Y %H:%M:%S")
	return c


def label(arq): #extrai a sopa XML label do aup e retorna no formato do Beautiful Soup 
	
	data=[]
	aup = open(arq,"r")
 
	for line in aup.readlines():
		data.append(line)

	soup = BeautifulSoup(''.join(data))

	s=soup.contents[4].contents[5] #localizao exata do label na sopa extraida do .aup

	x=s.findAll('label')

	return s


def tag(arq): #recebe arquivo, extrai a sopa XML tag deste e retorna dicionario
	data=[]
	aup = open(arq,"r")
 
	for line in aup.readlines():
		data.append(line)

	soup = BeautifulSoup(''.join(data))

	s=soup.contents[4].contents[1] #localizacao exata da tag na sopa extraida do .aup

	S=s() #converte a tipo sopa em tipo lista
	d={}
	
	n=0
	for i in S:
		d[s('tag')[n]['name']]=s('tag')[n]['value'] #formata o dicionario
		n=n+1

	#remover as tags indesejadas depois da contrução
	if d.has_key('id3v2'):
		d.pop('id3v2')
	if d.has_key('TRACKNUMBER'):
		d.pop('TRACKNUMBER')
	if d.has_key('YEAR'):
		d.pop('YEAR')
	if d.has_key('GENRE'):
		d.pop('GENRE')
	if d.has_key(u'G\xeanero'):
		d['Sexo']=d.pop(u'G\xeanero') #elimina possibilidade de erro na chave(fazer tambem com acentos e minusculas)


	return d



def pclasses(arq): #recebe arquivo aup e retorna lista ordenada das classes da palavra ja em minusculas

	sopa=label(arq)
	tam=0
	l=[] #lista buffer

	for t in sopa.findAll("label"):
		if( tam % 2 == 0):
			l.append(t['title'])
		tam=tam+1

	l=[x.lower() for x in l] #converte todas as classes para minusculas
	
	return l
	

def palavras(arq): #recebe arquivo aup e retorna lista ordenada das palavras

	sopa=label(arq)
	tam=0
	l=[] #lista buffer

	for t in sopa.findAll("label"):
		if( tam % 2 == 1):
			l.append(t['title'])
		tam=tam+1
	return l

def intervalos(arq): #recebe a arq e retorna lista ordenada de intervalos
	sopa=label(arq)
	
	tam=0
	l=[] #lista buffer de intervalos
	pausas=[] #lista calculada dos intervalos de pausa
	
	for t in sopa.findAll("label"):
		if( tam % 2 == 1):
			l.append([float(t['t']),float(t['t1'])]) #l =[intervalos inicio e fim indexados] 
		tam=tam+1
	
	lastend=float(0) #a primeira palavra comeca no zero
	
	for i in l: # pausas = lista ordenada de pausas
		pausas.append((i[0]-lastend)*1000) #o inicio da palavra menos a posicao final da outra em Milisegundos
		lastend=i[1] #guarda a posicao final para a proxima iteracao

	
	PALAVRAS=palavras(arq) #buscar a lista ordenada de palavras
	CLASSES=pclasses(arq) #buscar lista ordenada de classes
	Izip=zip(PALAVRAS,CLASSES,pausas) #formar uma tupla

	return Izip


def media(arq): #media dos intervalos
	sopa=label(arq)
	
	tam=0
	l=[] #lista buffer de intervalos
	pausas=[] #lista calculada dos intervalos de pausa
	
	for t in sopa.findAll("label"):
		if( tam % 2 == 1):
			l.append([float(t['t']),float(t['t1'])]) #l =[intervalos inicio e fim indexados] 
		tam=tam+1
	
	lastend=float(0) #a primeira palavra comeca no zero
	
	for i in l: # pausas = lista ordenada de pausas
		pausas.append((i[0]-lastend)*1000) #o inicio da palavra menos a posicao final da outra em Milisegundos
		lastend=i[1] #guarda a posicao final para a proxima iteracao

	m=sum(pausas)/len(pausas)


	return m


def listadeclasses():
	return [u'substantivo', u'adjetivo', u'verbo', u'conjunção', u'preposição', u'pronome']

def listadeamostras():
	return ["M1A1","M1A2","M1A3","M2A1","M2A2","M2A3","C1A1","C1A2","C1A3","C2A1","C2A2","C2A3","I1A1","I1A2","I1A3"]
def listadenarrativas():
	return ["M1","M2","C1","C2","I1"]



#buscas

def daclasse(classebuscada,classes,palavras): #recebe a classe e busca quais palavras sao da tal classe
	z=zip(classes,palavras) #forma uma lista de tuplas tipo [('substantivo','palavra')...]
	l=[] #lista buffer
	for i in z:
		if i[0] == classebuscada:
			l.append(i[1])
	return l

def mediadaclasse(arq,pclasse): #recebe arquivo e classe buscada e retorna tupla (peso,media)
	itv=intervalos(arq)
	x=0.0 #soma dos intervalos em que aparece a classe
	peso=0 #n de vezes que aparece a classe 
	media=0
	for i in itv:
		if i[1]==pclasse:
			x=x+i[2]
			peso=peso+1
	if peso > 0:
		media=x/peso
	
	Mclasse = (peso,media)

	return Mclasse

####################### melhorar:
def estrutura (arq): #inserir a contrução da tag aqui dentro mesmo? ele nao precisa abrir o arq - 3x mudar isso
	classes=[u'substantivo', u'adjetivo', u'verbo', u'conjunção', u'preposição', u'pronome']
	E=tag(arq)
	E['MediaGeral']=media(arq)
	for i in classes:
		E[i]=mediadaclasse(arq,i)
	E['Amostra']=E['Narrativa'][2]+E['Narrativa'][3]# separando Narrativa de Amostra
	E['Narrativa']=E['Narrativa'][0]+E['Narrativa'][1] # separando Narrativa de Amostra
	return E
##########################################################################			
	

################# abrindo e escrevendo o dicionario

homedir = os.path.expanduser('~')

ROOTpath = homedir+'/fonoaudiologia/novas_amostras/'

#retorna todos diretorios dentro de um diretorio numa lista 
def sujeitos(): 
	sujeitosDIR=[d for d in glob.glob( os.path.join(ROOTpath, '*')) if os.path.isdir(d)]
	return sujeitosDIR

def abretudo(): #lista com todos paths de arquivo
	tudo=[]
	for i in sujeitos():
		for infile in glob.glob( os.path.join(i, '*.aup')):
			tudo.append(infile)
	
	return tudo

def renderiza():
	renderizado=[]
	todos=abretudo()
	for i in todos:
		renderizado.append(estrutura(i))
	return renderizado

def DATAFILErenderiza():
	x='Estrutura='+str(renderiza())
	dados=open('data.py','w')
	dados.write(x)


from data import *

def Nomes():
	nomes=list(set([(i['Nome']) for i in Estrutura]))
	return nomes

def ConfereChavesEstrutura(Estrutura_item): # teste de formatação das chaves do dicionario estrutura basico
		chaves=[u'adjetivo', u'Nome', 'MediaGeral', 'Amostra', u'Narrativa', u'pronome', u'verbo', u'substantivo', u'Numero', u'Sexo', u'Idade', u'preposi\xe7\xe3o', u'Grupo', u'conjun\xe7\xe3o']
		chaves.sort()
		E=Estrutura_item.keys()
		E.sort()
		if E == chaves:
			return True
		else:
			return False


def EstruturaFiltrada(): #cria uma estrutura em dicionario separadando todas amostras numa unica chave de nome do sujeito
# retorna par (lista de medias da amostra, ficha ) - "ficha" tem os dados imutaveis - Sexo, Numero,Idade,Grupo
	from data import Estrutura #LEMBRE DE ESCREVER ESTA ESTRUTURA NO ARQUIVO - VAI FACILITAR	
	n=Nomes()
	d={}
	dDados={}
	l=[]
	MediaGeralTotal=0.0
	lc=listadeclasses()
	MediaClasses={}
	cSOMA=0.0
	pSOMA=0.0
	for i in n:
		for item in Estrutura:
			if item['Nome']==i:
				l.append(item)
				MediaGeralTotal = MediaGeralTotal + item['MediaGeral']
				sexo=item.pop('Sexo')
				numero=item.pop('Numero')
				idade=item.pop('Idade')
				grupo=item.pop('Grupo')
				#for classe in lc:
				#	cSOMA=(item[classe][0]*item[classe][1])+cSOMA
				#	pSOMA=item[classe][0]+pSOMA
				#	MediaClasses[classe]=cSOMA/pSOMA
				#	dDados['MediaDasClasses']=MediaClasses
				#cSOMA=0.0
				#pSOMA=0.0
		
		dDados['Sexo']=sexo				
		dDados['Numero']=numero
		dDados['Idade']=idade
		dDados['Grupo']=grupo
		dDados['MediaGeralTotal']=MediaGeralTotal/15
		d[i]=(l,dDados) # par (listadeamostras,ficha)
		MediaClasses[classe]=0.0
		
		MediaGeralTotal=0.0 #zera para proximo sujeito
		l=[]#zera para proximo sujeito
		dDados={}#zera para proximo sujeito
	dDados['MediaDasClasses']=MediaClasses
			
	
	return d 	


def DATAFILE2renderiza():
	x='EstruturaF='+str(EstruturaFiltrada())
	dados=open('data2.py','w')
	dados.write(x)