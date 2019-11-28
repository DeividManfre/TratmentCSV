from tratamento import escrever_sair



class o_programa: #Parte simples onde te dá opção de cancelar a execução ou prosseguir
	
	def verificar():
		print('################################################')
		print('# Programa de tratamento de dados TXT para CSV #')
		print('################################################')

		entrada = input('(1) Processar (2)Sair: ')

		while  entrada == '1':
			o_programa.verificar()

		else:
			print('você saiu')
			exit()


show = o_programa.verificar()







