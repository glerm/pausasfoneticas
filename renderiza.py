# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from filtra_estrutura import *
from configs import * #importa paths
from data import Estrutura
import time

root = Tk()
root.title("Pausas Silentes - Renderização")
# create a toolbar
toolbar = Frame(root)

def Teste_de_Erros():
	status='Confira as tags das amostras.\nForam encontrados erros em:\n---------------\n'
	if Estrutura:
		EF_new=EstruturaFiltrada(Estrutura)
		erros_entrada=ChecarErrosAmostrasTodas(EF_new)
		if erros_entrada:
			status=status+"\n++++ Amostras e Nomes:\n"
			for erros in erros_entrada['Erro_Amostras']:
				status=status+ str(erros) #str(erros[0]) + str(erros[1]) + "\n"
			status=status+"\n++++ Sexo:\n"
			status=status+str(erros_entrada['Erro_Sexo'])+"\n"
			status=status+"\n++++ Grupo:\n"
			status=status+str(erros_entrada['Erro_Grupo'])+"\n"
			status=status+"\n++++ Idade:\n"
			status=status+str(erros_entrada['Erro_Idade'])+"\n"
			#status=status+"\n++++ Chave:\n"
			#status=status+str(erros_entrada['Erro_Chave'])+"\n"
			#mensagem para reiniciar e consertar os erros:
			status=status+u'\nConfira inconsistências nas entradas indicadas acima.\nCorrija os arquivos e reinicie antes de rodar uma nova renderização.'
		else:
			status=u'Aparentemente não existem erros nas amostras. Feche este programa e rode o Gerador de Médias.'
	else:
		status=u'Ainda não foi rodada nenhuma renderização ou esta foi deletada. Rode uma nova renderização'
	return status



status=Teste_de_Erros()




def muda():
	text.delete(0.0,END)
	t=text
	renderizado=[]
	todos=abretudo()
	if not todos[0]: #quando existem arquivos faltantes ou repetidos.aup
		t.insert(END,"\nERRO!!\nExistem arquivos faltantes ou repetidos nas pastas: \n")
		t.tk.call('update')
		for folder_nome in todos[1]:
			t.insert(END,folder_nome +"\n")
			t.tk.call('update')
		t.see(END)
	else:
			
		for i in todos[1]:
				t.insert(END, "\n\nRenderizando arquivo: "+ str(i))
				t.tk.call('update')
				#render_estrutura=estrutura(i) #usar para ver os erros - como comolocar no Tkinter.Text?
				try:
					render_estrutura=estrutura(i)
					renderizado.append(render_estrutura)
					t.insert(END,"\n+++++++ OK!")
					t.tk.call('update')
					t.see(END)
				except:
					t.insert(END,"\n+++++++ ERRO NAS CHAVES OU CLASSES DE PALAVRAS DO ARQUIVO ACIMA!\n As chaves e classes permitidas são:")
					t.insert(END,u'\nAmostra, Grupo, Idade, Narrativa, Nome, Numero, Sexo,')
					t.insert(END,u'substantivo, adjetivo, verbo, conjunção, preposição, pronome, artigo, ruptura, interjeição, advérbio, indeterminado')
					t.insert(END,u'\n\nErros comuns são - falta de acentos, espaços ou o uso de palavras não reservadas ou trocas de letras nestas.\nREVISE ESTE ARQUIVO E RODE NOVAMENTE A RENDERIZAÇÃO!')
					t.tk.call('update')
					t.see(END)
					break
					
		else:
			####ok! grava
			x='Estrutura='+str(renderizado)
			dados=open(PYPATH+'data.py','w')
			dados.write(x)
			t.insert(END, "\n\n**** Gravado arquivo da nova renderização. Reinicie. ***** ")
			tkMessageBox.showinfo("Pronto!", "Gravado arquivo da nova renderização. Reinicie este programa para checar se foi encontrada alguma inconsistência." )
			t.tk.call('update')
			t.see(END)
			
			

scrollbar = Scrollbar(root)
scrollbar.pack(side=LEFT, fill=Y)





text = Text(root,wrap=WORD,width="100",height="30",bd=5,font=("Arial",13), foreground="orange",background="black")
text.insert(INSERT, status)
text.see(END)
text.config(yscrollcommand=scrollbar.set)
text.pack()


b = Button(toolbar, text="Renderização", command=muda)
b.pack(side=LEFT, padx=2, pady=2)

scrollbar.config(command=text.yview)
toolbar.pack(side=TOP, fill=X)

mainloop()
