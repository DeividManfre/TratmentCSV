from tratamento import Tratamento



class o_programa:
	
	def verificar():
		print('################################################')
		print('# Programa de tratamento de dados TXT para CSV #')
		print('################################################')
		entrada = input('(1) Processar (2)Sair: ')

		while  entrada == '1':
			Tratamento.ler()
			return print('Processado')  
		else:
			print('você saiu')
			exit()
		
		


show = o_programa.verificar()