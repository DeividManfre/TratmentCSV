from tratment import Tratment



class The_Program:
	
	def checkg():
		print('################################################')
		print('# Data Processing Program TXT for CSV #')
		print('################################################')
		input_value = input('(1) Process (2)Exit: ')

		while  input_value == '1':
			Tratment.read()
			return print('Processed')  
		else:
			print('You Exit')
			exit()
		
		


show = The_Program.checkg()