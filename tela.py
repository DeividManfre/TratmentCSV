from tratamento import escrever



class o_programa: #Parte simples onde te dá opção de cancelar a execução ou prosseguir

	def verificar():
		print('################################################')
		print('# Programa de tratamento de dados TXT para CSV #')
		print('################################################')

		entrada = input('(1) Processar (2)Sair: ')

		while entrada == '1':
			es = escrever.escrevendo()
			return print('Processado')
		else:
			print('você saiu')
			exit()





show = o_programa.verificar()
print (show)