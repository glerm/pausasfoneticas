# -*- coding: utf-8 -*-

#arquivo teste:
#arq='teste.aup'

from BeautifulSoup import BeautifulSoup
import string
import re
import sys
import codecs
import locale
language, output_encoding = locale.getdefaultlocale()




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

	#remover as tags indesejadas
	d.pop('id3v2')
	d.pop('TRACKNUMBER')
	d.pop('YEAR')

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
	return ['substantivo', 'adjetivo', 'verbo', u'conjunção', u'preposição', 'pronome']




def daclasse(classebuscada,classes,palavras): #recebe a classe e busca quais palavras sao da tal classe
	z=zip(classes,palavras) #forma uma lista de tuplas tipo [('substantivo','palavra')...]
	l=[] #lista buffer
	for i in z:
		if i[0] == classebuscada:
			l.append(i[1])
	return l


#FAZER: Organizar em classes?
#FAZER: resolver bem o problema dos acentos
#FAZER: testes de consistencia
#FAZER: abrir arquivos em lote e em busca cruzada de necessidades controle x pesquisa x idade x nome etc.


	



