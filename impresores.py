def impresor_entrada(datos_dict):
	for n,m in datos_dict.items():
		print(f'-> Nodo: {n}')
		c = 0 
		for x,y in m.items():
			print(f'{c+1}. {y[1]}: {y[0]}')
			c = c + 1
		print('')

