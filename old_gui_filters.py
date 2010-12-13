mediaN=MediasTodasNarrativas() #quem esta usando esta chamada?

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
	dados=open(CSVpath+'PAUSASHistoria.csv','w')
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
	dados=open(CSVpath+'PAUSASGramatica.csv','w')
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


def rendershell():
	print "preciso ser uma funcao separada de RENDERIZAR"

