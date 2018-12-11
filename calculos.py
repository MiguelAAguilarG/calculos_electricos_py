from math import *

def calculador_corriente(
	Sistema, 
	Voltaje, 
	Carga, 
	fp, 
	factor_carga):

	if Sistema == 'monofásico':
		I_nom = Carga/(Voltaje*fp)
		I_calculada = I_nom*factor_carga

	if Sistema == 'trifásico':
		I_nom = Carga/(sqrt(3)*Voltaje*fp)
		I_calculada = I_nom*factor_carga

	Carga_corregida = Carga*factor_carga

	return I_nom, I_calculada, Carga_corregida

def calculador_conductores_canalizacion(
	Sistema, 
	numero_conductores_por_fase, 
	mismo, 
	neutro):

	if neutro == 'si':
		neutro = 1
	if neutro == 'no':
		neutro = 0

	if Sistema == 'monofásico':
		neutro = 1

		if mismo == 'si':
			conductores_canalizacion = numero_conductores_por_fase*mismo + neutro*numero_conductores_por_fase*mismo
		if mismo == 'no':
			conductores_canalizacion = 1 + neutro

	if Sistema == 'trifásico':
		if mismo == 'si':
			conductores_canalizacion = 3*numero_conductores_por_fase*mismo + neutro*numero_conductores_por_fase*mismo
		if mismo == 'no':
			conductores_canalizacion = 3 + neutro

	return conductores_canalizacion

def calculador_interruptor(
	I_calculada, 
	I_nom, 
	Interruptores, 
	Interruptor_forzado, 
	porcentaje_Irating, 
	factor_carga, 
	ajuste_factor_carga):
	Interruptor_forzado = Interruptor_forzado*porcentaje_Irating/100

	for x in Interruptores:
		if I_calculada <= x:
	  		Interruptor = x
	  		break
		if I_nom*(factor_carga-ajuste_factor_carga/100) <= x:
			Interruptor = x
			break
	else:
		print('No se encontro interruptor tan grande. Aumenta el nivel de voltaje para esa carga')
	
	if not Interruptor_forzado == 0:
		if Interruptor_forzado >= I_calculada or Interruptor_forzado >= I_nom*(factor_carga-ajuste_factor_carga/100):
			Interruptor = Interruptor_forzado
			print(f'Se forzo interruptor para la carga. Interruptor forzado = {Interruptor_forzado}')#modificar cuando se hagan clases
		else:
			print(f'Se forzo interruptor para la carga. Pero el interruptor forzado es muy pequeño. Interruptor forzado = {Interruptor_forzado}. Interruptor seleccionado = {Interruptor}')#modificar cuando se hagan clases

	return Interruptor

def calculador_factor_temperatura(
	Tconductor, 
	Tambiente, 
	Tambiente_tablas):

	factor_temperatura = sqrt((Tconductor-Tambiente)/(Tconductor-Tambiente_tablas))

	return factor_temperatura

def calculador_factor_agrupamiento(
	conductores_canalizacion, 
	tabla_factor_agrupamiento, 
	Longitud):

	if Longitud <= 0.6:#Factor de agrupamiento no aplica para 60 cm o menos. 310-15.(b)(3)(a)(2)
		factor_agrupamiento = 1
	else:
		for x,y in tabla_factor_agrupamiento.items(): #Determinar factor de agrupamiento NOTA: Ir a la Tabla 310-15(b)(3)(a)
			if conductores_canalizacion <= x:
				factor_agrupamiento = y
				break
		else:
			print('Demasiados conductores en la canalizacion')#modificar cuando se hagan clases
			factor_agrupamiento = 0

	return factor_agrupamiento

def calculador_cable_ampacidad(
	tabla_de_Ampacidades, 
	calibre_tabla, 
	Area_conductor_tabla, 
	Interruptor, 
	numero_conductores_por_fase, 
	material_conductor, 
	Tconductor, 
	factor_agrupamiento, 
	factor_temperatura, 
	calibre = False):

	Ampacidad_tabla = tabla_de_Ampacidades[material_conductor][Tconductor]
	Ampacidad_corregida_tabla = [x*factor_agrupamiento*factor_temperatura for x in Ampacidad_tabla]

	if calibre in calibre_tabla:

		indice = calibre_tabla.index(calibre)
		Area = Area_conductor_tabla[indice]
		Ampacidad = Ampacidad_tabla[indice]
		Ampacidad_corregida = Ampacidad_corregida_tabla[indice]

		return indice, calibre, Area, Ampacidad, Ampacidad_corregida

	while True:
		for indice, Ampacidad_corregida in enumerate(Ampacidad_corregida_tabla):
			if Ampacidad_corregida >= Interruptor/numero_conductores_por_fase:
				calibre = calibre_tabla[indice]
				Area = Area_conductor_tabla[indice]
				Ampacidad = Ampacidad_tabla[indice]

				if Area < 53 and numero_conductores_por_fase > 1:
					print('Ampacidad')
					print('!ERROR. Tamano de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
					print(f'Conductor elegido por ampacidad menor a 1/0: {calibre}')
					print('')
				else:
					return indice, calibre, Area, Ampacidad, Ampacidad_corregida
		else:
			print('Ampacidad')
			print('!ERROR. Tamano de conductor demasiado grande. Fuera de rango de las tablas.')
			print('Se recomienda aumentar numero de conductores por fase')
			print('')

			while True:
				print('caída de tensión')
				numero_conductores_por_fase = imput('Nuevo número de conductores por fase: ')
				if numero_conductores_por_fase <= 0:
					print('caída de tensión')
					print('!ERROR¡. El numero de conductores por fase es menor o igual a 0')
				else:
					break

def calculador_cable_caida_de_tension(
	tabla_de_impedancias, 
	calibre_tabla, 
	Area_conductor_tabla, 
	Sistema, 
	fp, 
	Longitud, 
	I_nom, 
	Voltaje, 
	caida_tension, 
	numero_conductores_por_fase, 
	material_conductor, 
	material_canalizacion, 
	calibre = False):

	resistencia_tabla = tabla_de_impedancias['resistencia'][material_conductor][material_canalizacion]
	reactancia_tabla = tabla_de_impedancias['reactancia'][material_conductor][material_canalizacion]
	
	if calibre in calibre_tabla:

		indice = calibre_tabla.index(calibre)
		Area = Area_conductor_tabla[indice]

		Ze = (resistencia_tabla[indice]*fp + reactancia_tabla[indice]*sin(acos(fp)))/1000

		if Sistema == 'monofásico':
			caida_tension_calculada = 2*Ze*Longitud*I_nom*100/Voltaje/numero_conductores_por_fase
		elif Sistema == 'trifásico':
			caida_tension_calculada = sqrt(3)*Ze*Longitud*I_nom*100/Voltaje/numero_conductores_por_fase

		return indice, calibre_tabla[indice], Area, Ze, caida_tension_calculada

	while True:
		for indice, Area in enumerate(Area_conductor_tabla):
			Ze = (resistencia_tabla[indice]*fp + reactancia_tabla[indice]*sin(acos(fp)))/1000

			if Sistema == 'monofásico':
				caida_tension_calculada = 2*Ze*Longitud*I_nom*100/Voltaje/numero_conductores_por_fase
			elif Sistema == 'trifásico':
				caida_tension_calculada = sqrt(3)*Ze*Longitud*I_nom*100/Voltaje/numero_conductores_por_fase
		
			if caida_tension_calculada <= caida_tension:

				if Area < 53 and numero_conductores_por_fase > 1:
					print('caída de tensión')
					print('!ERROR. Tamaño de conductor menor a 1/0. No se puede poner ese tamaño de conductor en paralelo.')
					print(f'Conductor elegido por ampacidad menor a 1/0: {calibre_tabla[indice]}')
					print('')
				else:
					return indice, calibre_tabla[indice], Area, Ze, caida_tension_calculada
		else:
			print('caída de tensión')
			print('!ERROR. Tamaño de conductor demasiado grande. Fuera de rango de las tablas.')
			print('Se recomienda aumentar numero de conductores por fase')
			print('')

			while True:
				print('caída de tensión')
				numero_conductores_por_fase = imput('Nuevo número de conductores por fase: ')
				if numero_conductores_por_fase <= 0:
					print('caída de tensión')
					print('!ERROR¡. El número de conductores por fase es igual o menor a 0')
				else:
					break

#def seleccionador_cable(indices,factores):

def calculador_cable_tierra_fisica(
	interruptor_tierra_fisica_tabla, 
	tierra_fisica_tabla,  
	calibre_tabla, 
	Area_tierra_tabla, 
	Interruptor, 
	material_conductor_tierra, 
	canalizacion):

	for x,y in enumerate(interruptor_tierra_fisica_tabla):
		if Interruptor <= y:
			calibre_tierra_fisica = tierra_fisica_tabla[material_conductor_tierra][x]
			Area_tierra_fisica = Area_tierra_tabla[calibre_tabla.index(calibre_tierra_fisica)]

			if Area_tierra_fisica < 21.2 and canalizacion == 'charola':
				print('Tierra física')
				print('Tamaño de conductor menor a 4. No se puede poner ese tamaño de conductor en una charola.')
				print(f'Conductor de tierra fisica elegido: {calibre_tierra_fisica}')
				print(f'Material de tierra fisica: {material_conductor_tierra}')
				print('')

				tierra = '4'
				Area_tierra_fisica = Area_tierra_tabla[calibre_tabla.index(calibre_tierra_fisica)]
		
			return calibre_tierra_fisica, Area_tierra_fisica
			

def calculador_tamano_conduit(
	designacion_tubo_conduit,
	dimensiones_tubo_conduit,
	dimensiones_cables, 
	conductores_canalizacion,
	aislante_conductor,
	tipo_conduit,
	indice_conductor, 
	calibre_tierra_fisica, 
	Area_tierra_fisica,
	porcentaje_ocupacion_forzado = 0
	):

	lista_aislantes = []
	for indice1, key in enumerate(dimensiones_cables.keys()):
		lista_aislantes.append([])
		lista_aislantes[indice1] = key.split(',')
		for indice2, elemento in enumerate(lista_aislantes[indice1]):
			lista_aislantes[indice1][indice2] = elemento.strip()

		if aislante_conductor in lista_aislantes[indice1]:
			key_aislante_conductor = key

	Area_cable = (dimensiones_cables[key_aislante_conductor][indice_conductor]/2)**2*pi
	Area_total_conductores = conductores_canalizacion*Area_cable + Area_tierra_fisica

	tuberia_tabla = ['1/2', '3/4', '1', '1 1/4', '1 1/2', '2', '2 1/2', '3', '3 1/2', '4', '5', '6']
	for indice, x in enumerate(dimensiones_tubo_conduit[tipo_conduit]):
		Area_conduit = (x/2)**2*pi
		porcentaje_ocupacion_calculado = Area_total_conductores*100/Area_conduit

		if not porcentaje_ocupacion_forzado == 0:
			porcentaje_ocupacion = porcentaje_ocupacion_forzado
		else:
			porcentaje_ocupacion =  40

		if porcentaje_ocupacion_calculado <= porcentaje_ocupacion:
			medida_tuberia_pulg = tuberia_tabla[indice]
			medida_tuberia_mm = designacion_tubo_conduit[medida_tuberia_pulg]

			return medida_tuberia_pulg, medida_tuberia_mm, Area_total_conductores, Area_conduit, porcentaje_ocupacion_calculado, Area_cable, Area_tierra_fisica

	
		
