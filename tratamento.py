##################################################################################################
# Este desenvolvimento serve como demonstração dos meus conhecimento de orientação a objeto      #													
# focando em como utilizar herança e otimização de alguns bloco de código, consiste em um código #
# simples de facil entendimento / por ser didático essa demonstração as variaveis e classes      #
# estão em portugues Brasil / 													      		     #																																														#	
##################################################################################################
import pandas as pd
import datetime

class entrada: #classe de entrada para o arquivo onde eu leio e retorno  legível para tratar

	def ler():
		abrir = open('teste.txt', 'r')
		ler_arquivo = abrir.read().split(';')
		return ler_arquivo

class tratamento(entrada): #classe de tratamento utiliza por herança a classe entrada para ajustar os dados no padrão CSV

	def tratar():
		ajuste_arquivo = entrada.ler() 
		df = pd.DataFrame([ajuste_arquivo], columns=['name','cpf'])
		return  df

class escrever_sair(tratamento): #classe escrita é a última etapa do codigo onde ele utiliza o retorno do tratamento df "DataFrame" escrever e criar o arquivo CSV

	def escrevendo_saida():
		info = tratamento.tratar()
		atuais = datetime.datetime.now()
		nome = atuais.strftime('%d%m%Y%H%M')
		return info.to_csv('final/'+ nome +'.csv')



					






