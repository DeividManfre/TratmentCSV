import pandas as pd
import datetime

class Tratamento:
	
	def ler():
		abrir = open('teste.txt', 'r')
		ler_arquivo = abrir.read().split(';')
		df = pd.DataFrame([ler_arquivo], columns=['name','cpf'])
		atuais = datetime.datetime.now()
		nome = atuais.strftime('%d%m%Y%H%M%s')
		return df.to_csv('final/'+ nome +'.csv')







