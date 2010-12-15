# -*- coding: utf-8 -*-


from BeautifulSoup import BeautifulSoup
import string
import re
import sys
import codecs
import locale
import os, glob
import numpy

from trata_arquivos import *

from data import Estrutura




def Nomes():
	nomes=list(set([(i['Nome']) for i in Estrutura]))
	return nomes


def EstruturaFiltrada(Estrutura): ### RETIRE O ARGUMENTO SE DER ERRO!!! 11 NOV 2010
#Cria uma estrutura em dicionario separadando todas amostras numa unica chave de nome do sujeito.
#Retorna par (lista de medias da amostra, ficha ) - "ficha" tem os dados imutaveis - Sexo, Numero,Idade,Grupo
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
				sexo=item.get('Sexo') #troquei pop por get
				numero=item.get('Numero') #troquei pop por get
				idade=item.get('Idade') #troquei pop por get
				grupo=item.get('Grupo') #troquei pop por get
		dDados['Sexo']=sexo
		dDados['Numero']=numero
		dDados['Idade']=idade
		dDados['Grupo']=grupo
		dDados['MediaGeralTotal']=MediaGeralTotal/15
		d[i]=(l,dDados) # par (listadeamostras,ficha)
		#MediaClasses[classe]=0.0
		
		MediaGeralTotal=0.0 #zera para proximo sujeito
		l=[]#zera para proximo sujeito
		dDados={}#zera para proximo sujeito
	#dDados['MediaDasClasses']=MediaClasses
			
	
	return d 	


E=Estrutura
EstruturaF=EstruturaFiltrada(E)


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
	if len(L) != 0:
		return sum(L)/len(L)
	else:
		return 0

	

########TESTES DE CONSISTÊNCIA#########################################

def SepararAmostrasIndividuais(EstruturaF): 
	l=[]
	d={}
	e=EstruturaF
	for key in e:
		for item in e[key][0]:# e[key] contem o par (listadeamostras,ficha)
			l.append(str(item['Narrativa'])+str(item['Amostra']))
			l.sort()
			d[key]=l
		l=[]	
	return d

def SepararErroSexo(EstruturaF): #devolve lista das amostras onde há um erro na chave sexo
	l=[]
	d={}
	e=EstruturaF
	for key in e:
		for item in e[key][0]:# e[key] contem o par (listadeamostras,ficha)
			if ((str(item['Sexo'])) not in ['M','F']):
				l.append(str(item['Narrativa'])+str(item['Amostra'])+": "+str(item['Sexo']))
				d[key]=l
		l=[]
	return d

def SepararErroGrupo(EstruturaF): #devolve lista das amostras onde há um erro na pesquisa
	l=[]
	d={}
	e=EstruturaF
	for key in e:
		for item in e[key][0]:# e[key] contem o par (listadeamostras,ficha)
			if ((str(item['Grupo'])) not in ['P','C']):
				l.append(str(item['Narrativa'])+str(item['Amostra'])+": "+str(item['Grupo']))
				d[key]=l
		l=[]
	return d

def SepararErroIdade(EstruturaF): #devolve lista das amostras onde há um erro na pesquisa
	l=[]
	d={}
	e=EstruturaF
	for key in e:
		for item in e[key][0]:# e[key] contem o par (listadeamostras,ficha)
			if 'a' not in (str(item['Idade'])):
				l.append(str(item['Narrativa'])+str(item['Amostra'])+": "+str(item['Idade']))
				d[key]=l
		l=[]
	return d

def ChecarErrosAmostrasTodas(EstruturaF): 
	dic_erros={}
	erro_nas_amostras=[]
	amostras=SepararAmostrasIndividuais(EstruturaF)
	sexo=SepararErroSexo(EstruturaF)
	grupo=SepararErroGrupo(EstruturaF)
	idade=SepararErroIdade(EstruturaF)
#	chave=SepararErrosChaves(EstruturaF)
	AMOSTRAS_PADRAO=["M1A1","M1A2","M1A3","M2A1","M2A2","M2A3","C1A1","C1A2","C1A3","C2A1","C2A2","C2A3","I1A1","I1A2","I1A3"]
	AMOSTRAS_PADRAO.sort()
	for i in amostras:
		a=amostras[i]
		a.sort()
		if AMOSTRAS_PADRAO != a:
			DIFF=[diff for diff in AMOSTRAS_PADRAO+a if diff not in AMOSTRAS_PADRAO or diff not in a]
			erro_nas_amostras.append((i,DIFF))
#escreve o dicionario
	if erro_nas_amostras:
		dic_erros['Erro_Amostras']=erro_nas_amostras
	else:
		dic_erros['Erro_Amostras']="ok"
	if sexo:
		dic_erros['Erro_Sexo']=sexo
	else:
		dic_erros['Erro_Sexo']="ok"
	if grupo:
		dic_erros['Erro_Grupo']=grupo
	else:
		dic_erros['Erro_Grupo']="ok"
	if idade:
		dic_erros['Erro_Idade']=idade
	else:
		dic_erros['Erro_Idade']="ok"
#	if chave:
#		dic_erros['Erro_Chave']=chave
#	else:
#		dic_erros['Erro_Chave']="Nenhum"

	if (['ok','ok','ok','ok']) == (dic_erros.values()):
		dic_erros = False

	return dic_erros


##########################################################################tentativas anteriores:
'''

def ConfereChavesEstrutura(Estrutura_item): # teste de formatação das chaves do dicionario estrutura basico
		chaves=[u'adjetivo', u'Nome', 'MediaGeral', 'Amostra', u'Narrativa', u'pronome', u'verbo', u'substantivo', u'Numero', u'Sexo', u'Idade', u'preposi\xe7\xe3o', u'Grupo', u'conjun\xe7\xe3o']
		chaves.sort()
		E=Estrutura_item.keys()
		E.sort()
		if E == chaves:
			return True
		else:
			return False

def ChecarErrosAmostras(EstruturaF): #compara padroes dos lotes de arquivo (testar a necessidade de implementar outros casos)
	d={}
	amostras=SepararAmostrasIndividuais(EstruturaF)
	AMOSTRAS_PADRAO=listadeamostras()
	AMOSTRAS_PADRAO.sort()
	for i in amostras:
		a=amostras[i]
		a.sort()
		d[str(i)]=(AMOSTRAS_PADRAO == a)
	return d


def SepararErrosChaves(EstruturaF): #devolve lista das amostras onde há um erro na pesquisa
	l=[]
	d={}
	e=EstruturaF
	chave=['Amostra', u'Grupo', u'Idade', 'MediaGeral', 'MediaGeralTotal', u'Narrativa', u'Nome', u'Numero', u'Sexo', u'adjetivo', u'conjun\xe7\xe3o', u'preposi\xe7\xe3o', u'pronome', u'substantivo', u'verbo']
	for key in e:
		for item in e[key][0]:# e[key] contem o par (listadeamostras,ficha)
			chave_atual=e[key][1].keys() + item.keys()
			l.append( list(set(chave_atual).difference(set(chave))))
			d[key]=l
		l=[]
	return d
'''





