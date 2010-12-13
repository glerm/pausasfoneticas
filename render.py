# -*- coding: utf-8 -*-


from Tkinter import *
import tkMessageBox
import Tkinter, tkFileDialog
import tkMessageBox
import os
import ScrolledText
import codecs
import locale
import os
language, output_encoding = locale.getdefaultlocale()

#importa a estrutura filtrada original
from filtra_estrutura import *
from configs import * #importa paths


def rendershell(root):
	c = Toplevel(root)
	c.title("Renderização")
	c.geometry('500x400+230+130')
	t = Text(c,foreground="orange",background="black")
	t.pack()
	c.tk.call('update')
	renderizado=[]
	todos=abretudo()
	if not todos[0]: #quando existem arquivos faltantes ou repetidos.aup
		t.insert(END,"\nERRO!!\nExistem arquivos faltantes ou repetidos nas pastas: \n")
		t.tk.call('update')
		for folder_nome in todos[1]:
			t.insert(END,folder_nome +"\n")
			t.tk.call('update')
		t.see(END)
		c.tk.call('update')
		c.focus_set()
	else:
			
		for i in todos[1]:
				t.insert(END, "\n\nRenderizando arquivo: "+ str(i))
				t.tk.call('update')
				renderizado.append(estrutura(i))
				t.insert(END,"\n+++++++ OK!")
				t.tk.call('update')
				t.see(END)
		EF_new=EstruturaFiltrada(renderizado)
		erros_entrada=ChecarErrosAmostras(EF_new)
		t.insert(END, "\nrenderizado: " + str(erros_entrada))
		t.tk.call('update')
		t.see(END)
				
		if (False in erros_entrada.itervalues()):
			t.insert(END, "\n**********ERRO!!!!!!*********\nErros na entrada de dados - Repetição da Chave Narrativa nas amostras:\n")
			t.tk.call('update')
			for val in erros_entrada.items():
				if not val[1]: #se o valor not(False) isto é - havia inconsistencia
					t.insert(END, "++++ "+ str(val[0]) + " +++++\n")
					t.tk.call('update')
			t.insert(END, "\n\nCheque se há entradas repetidas ou erradas no campo Narrativa de suas fichas.\n")
			t.tk.call('update')
			t.see(END)
		else:
			####ok! grava
			x='Estrutura='+str(renderizado)
			dados=open(PYPATH+'data.py','w')
			dados.write(x)
			t.insert(END, "\n\n**** Gravado arquivo da nova renderização ***** ")
			t.tk.call('update')
			t.see(END)
	c.tk.call('update')
	c.focus_set()
	
