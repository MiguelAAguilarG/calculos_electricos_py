def impresor_entrada(datos_entrada_dict, datos_entrada_descripcion_dict):
	for key_identificador in datos_entrada_dict.keys():
		print(f'-> Identificador: {key_identificador}')
		for n, key_datos in enumerate(datos_entrada_dict[key_identificador].keys()):
			print(f'{n+1}. {datos_entrada_descripcion_dict[key_datos]}: {datos_entrada_dict[key_identificador][key_datos]}')
		print()

def impresor_salida(datos_salida_dict, datos_salida_descripcion_dict):
	for key_identificador in datos_salida_dict.keys():
		print(f'-> Identificador: {key_identificador}')
		for n, key_datos in enumerate(datos_salida_descripcion_dict.keys()):
			print(f'{n+1}. {datos_salida_descripcion_dict[key_datos]}: {datos_salida_dict[key_identificador][key_datos]}')
		print()		

'''def impresor_salida(salida_dict):
	for n,m in salida_dict.items():
		print(f'-> Nodo: {n}')
		c = 0 
		for x,y in m.items():
			print(f'{c+1}. {x}: {y}')
			c = c + 1
		print('')'''

