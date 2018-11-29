from math import sqrt

def calcular_corriente(Sistema, Voltaje, Carga, fp, factor_carga):
	if Sistema == 'monofásico':
		I_nom = Carga/(Voltaje*fp)
		I_calculada = I_nom*factor_carga

	if Sistema == 'trifásico':
		I_nom = Carga/(sqrt(3)*Voltaje*fp)
		I_calculada = I_nom*factor_carga

	Carga_corregida = Carga*factor_carga

	return I_nom, I_calculada, Carga_corregida

def calcular_conductores_canalizacion(Sistema, numero_conductores_por_fase, mismo, neutro):
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

def calcular_interruptor(I_calculada, I_nom, Interruptores, Interruptor_forzado, porcentaje_Irating, factor_carga, ajuste_factor_carga):
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

def calcular_factor_temperatura(Tconductor, Tambiente, Tambiente_tablas):

	factor_temperatura = sqrt((Tconductor-Tambiente)/(Tconductor-Tambiente_tablas))

	return factor_temperatura

def calcular_factor_agrupamiento(conductores_canalizacion, tabla_factor_agrupamiento, Longitud):

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

