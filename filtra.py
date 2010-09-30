# -*- coding: utf-8 -*-


from BeautifulSoup import BeautifulSoup
import string
import re
import sys
import codecs
import locale
import os, glob
import numpy

from renderiza import *

from data2 import EstruturaF



def MediasTodasNarrativas():
	nomes=Nomes()
	narrativas=listadenarrativas()
	E=EstruturaF
	l=[]
	d={}
	l2=[]
	for nome in nomes: #MEDIA DE TODAS AS AMOSTRAS NUMA LISTA
		for item in E[nome][0]:
			for narrativa in narrativas:
				if item['Narrativa'] == narrativa:					
					l.append( (item['Nome'],narrativa,str(item['Amostra']),item['MediaGeral']) )

	d = {}
	for x,y,z,a in l: #separa todas as amostras num dicionario {sujeito:[amostras]}
	    d.setdefault(x, []).append((y,z,a))
	
	dN= {} #dicionario d narrativas e suas 3 amostras
	for key in d.iterkeys():
		dN[key]={}
		for x,y,z in d[key]:
			dN[key].setdefault(x, []).append(z)

	d={}
	for key in dN.iterkeys(): #dicionario Sujeito:{media entre as tres amostras da Narrativa para cada}
		d[key]={}
		for i in dN[key].iterkeys():
			#d[key].setdefault(i, []).append(numpy.mean(dN[key][i]))
			d[key][i]=(numpy.mean(dN[key][i]))


	return d


def MediasGramaticas(estrutura,nome,classe_gramatical):
	L=[]
	for i in range (len(estrutura[nome][0])):
		if estrutura[nome][0][i][classe_gramatical][1] != 0:
			L.append(estrutura[nome][0][i][classe_gramatical][1])

	return sum(L)/len(L)

	

########TESTES DE CONSISTÊNCIA

def SepararAmostrasIndividuais():
	l=[]
	d={}
	e=EstruturaF
	for key in e:
		for item in e[key][0]:# e[key] contem o par (listadeamostras,ficha)
			l.append(str(item['Narrativa'])+str(item['Amostra']))
			d[key]=l
		l=[]	
	return d


def ChecarErrosAmostras(): #compara padroes dos lotes de arquivo (testar a necessidade de implementar outros casos)
	d={}
	amostras=SepararAmostrasIndividuais()
	AMOSTRAS_PADRAO=listadeamostras()
	AMOSTRAS_PADRAO.sort()
	for i in amostras:
		a=amostras[i]
		a.sort()
		d[str(i)]=(AMOSTRAS_PADRAO == a)
		#d={str(i):AMOSTRAS == a}
	
	return d



		
