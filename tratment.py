import pandas as pd
import datetime

class Tratment:
	
	def read():
		open_archive = open('teste.txt', 'r')
		read_archive = open_archive.read().split(';')
		df = pd.DataFrame([read_archive], columns=['name','cpf'])
		actual = datetime.datetime.now()
		name = actual.strftime('%d%m%Y%H%M%s')
		return df.to_csv('finish/'+ name +'.csv')







