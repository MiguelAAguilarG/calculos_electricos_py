from tablas import tablas

def validacion(datos_entrada_dict, datos_entrada_descripcion_dict):

	for x,y in datos_entrada_dict.items():
		print(f'Identificador: {x}')
		n_errores = 0

		if not y.get('Sistema') == None:
			Sistema = y.get('Sistema').lower()

			if not (Sistema == 'monofásico' or Sistema == 'trifásico'):
				print('!ERROR¡. El sistema ingresado no es correcto. Debe ser \'trifásico\' o \'monofásico\'')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['Sistema'] = Sistema
		
		if not y.get('Voltaje') == None:
			Voltaje = float(y.get('Voltaje'))
			if Voltaje <= 0:
				print('!ERROR¡. El voltaje es menor o igual a 0')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['Voltaje'] = Voltaje
		
		if not y.get('Carga') == None:
			Carga = float(y.get('Carga'))
			if Carga <= 0:
				print('!ERROR¡. La carga es menor o igual a 0')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['Carga'] = Carga

		if not y.get('factor_carga') == None:		
			factor_carga = float(y.get('factor_carga'))
			if factor_carga <= 0:
				print('!ERROR¡. El factor de carga es menor o igual a 0')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['factor_carga'] = factor_carga
		
		if not y.get('fp') == None:	
			fp = float(y.get('fp'))
			if fp < 0:
				print('!ERROR¡. El factor de potencia es menor a 0')
				n_errores = n_errores + 1
			elif fp > 1:
				print('!ERROR¡. El factor de potencia es mayor a 1')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['fp'] = fp
			
		if not y.get('caida_tension') == None:	
			caida_tension = float(y.get('caida_tension'))
			if caida_tension <= 0:
				print('!ERROR¡. La caída de tensión es menor o igual a 0%')
				n_errores = n_errores + 1
			elif caida_tension > 3:
				print('!ERROR¡. La caída de tensión es mayor a 3%')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['caida_tension'] = caida_tension
		
		if not y.get('Longitud') == None:
			Longitud = float(y.get('Longitud'))
			if Longitud <= 0:
				print('!ERROR¡. La longitud es menor o igual a 0')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['Longitud'] = Longitud

		'''n = n + 1; 
		conductores_canalizacion = round(datos(n));
		if conductores_canalizacion < 0
		  print('!ERROR. El numero de conductores es menor a 0');
		  n_errores = n_errores + 1;
		elseif conductores_canalizacion > 50
		  print('!ERROR. El numero de conductores es mayor a 50. Son demasiados conductores');
		  n_errores = n_errores + 1;'''
		if not y.get('Tambiente') == None:
			Tambiente = float(y.get('Tambiente'))
			datos_entrada_dict[x]['Tambiente'] = Tambiente
		
		if not y.get('aislante_conductor') == None:
			aislante_conductor = y.get('aislante_conductor').upper()
			lista_aux1 = []		
			for a in tablas()['dimensiones_cables_tabla_5'].keys():
				lista_aux1 = lista_aux1 + a.split(',')
			lista_aux2 = []
			for a in lista_aux1:
				lista_aux2.append(a.strip())
			if not aislante_conductor in lista_aux2:
				print('!ERROR¡. El aislante del conductor no esta en los datos')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['aislante_conductor'] = aislante_conductor
		
		if not y.get('Tconductor') == None:
			Tconductor = int(y.get('Tconductor'))
			if not (Tconductor == 60 or Tconductor == 75 or Tconductor == 90):
				print('!ERROR¡. La temperatura del aislante del conductor no es correcta')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['Tconductor'] = Tconductor
		
		if not y.get('material_conductor') == None:
			material_conductor = y.get('material_conductor').lower()
			if not (material_conductor == 'cobre' or material_conductor == 'aluminio'):
				print('!ERROR¡. El material del conductor no es correcto')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['material_conductor'] = material_conductor

		if not y.get('numero_conductores_por_fase') == None:
			numero_conductores_por_fase = int(y.get('numero_conductores_por_fase'))
			if numero_conductores_por_fase <= 0:
				print('!ERROR¡. El numero de conductores por fase es menor o igual a 0')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['numero_conductores_por_fase'] = numero_conductores_por_fase
		
		if not y.get('mismo') == None:
			mismo = y.get('mismo').lower()
			if not (mismo == 'si' or mismo == 'no'):
				print('!ERROR¡. Dato no valido para colocar conductores de fase y neutro en la misma canalizacion cuando es más de un conductor por fase')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['mismo'] = mismo
		
		if not y.get('ajuste_factor_carga') == None:
			ajuste_factor_carga = float(y.get('ajuste_factor_carga'))
			if ajuste_factor_carga < 0 or ajuste_factor_carga > 100:
				print('!ERROR¡. Dato no valido. No corresponde a un porcentaje real para ajuste del interruptor')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['ajuste_factor_carga'] = ajuste_factor_carga
		
		if not y.get('porcentaje_Irating_1') == None:
			porcentaje_Irating_1 = float(y.get('porcentaje_Irating_1'))
			if porcentaje_Irating_1 <= 0 or porcentaje_Irating_1 > 100:
				print('!ERROR¡. Dato no valido. No corresponde a un porcentaje real para Irating del interruptor 1')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['porcentaje_Irating_1'] = porcentaje_Irating_1
		
		if not y.get('Interruptor_forzado_1') == None:
			Interruptor_forzado_1 = y.get('Interruptor_forzado_1')
			if Interruptor_forzado_1 < 0:
				print('!ERROR¡. Dato no valido. Amperaje de interruptor 1 forzado menor a 0')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['Interruptor_forzado_1'] = Interruptor_forzado_1
		
		if not y.get('porcentaje_Irating_2') == None:
			porcentaje_Irating_2 = float(y.get('porcentaje_Irating_2'))
			if porcentaje_Irating_2 <= 0 or porcentaje_Irating_2 > 100:
				print('!ERROR¡. Dato no valido. No corresponde a un porcentaje real para Irating del interruptor 2')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['porcentaje_Irating_2'] = porcentaje_Irating_2
		
		if not y.get('Interruptor_forzado_2') == None:
			Interruptor_forzado_2 = y.get('Interruptor_forzado_2')
			if Interruptor_forzado_2 < 0:
				print('!ERROR¡. Dato no valido. Amperaje de interruptor 2 forzado menor a 0')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['Interruptor_forzado_2'] = Interruptor_forzado_2

		if not y.get('mismo_amperaje') == None:
			mismo_amperaje = y.get('mismo_amperaje')
			if not isinstance(Interruptor_forzado_2, bool):
				print('!ERROR¡. Dato no valido. El valor para igual amperaje en los dos interruptures debe de ser True o False')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['mismo_amperaje'] = mismo_amperaje

		if not y.get('canalizacion') == None:
			canalizacion = y.get('canalizacion').lower()
			if not (canalizacion == 'conduit' or canalizacion == 'charola'):
				print('!ERROR¡. Dato no valido. No es una canalizacion')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['canalizacion'] = canalizacion
		
		if not y.get('material_canalizacion') == None:		
			material_canalizacion = y.get('material_canalizacion').lower()
			if not (material_canalizacion == 'acero' or material_canalizacion == 'pvc' or material_canalizacion == 'aluminio'):
				print('!ERROR¡. Dato no valido. No es un material de canalizacion')
				print(material_canalizacion)
				n_errores = n_errores + 1
			datos_entrada_dict[x]['material_canalizacion'] = material_canalizacion
		
		if not y.get('tipo_conduit') == None:
			tipo_conduit = y.get('tipo_conduit')
			if not tipo_conduit in tablas()['dimensiones_tubo_conduit_tabla_4'].keys():
				print('!ERROR¡. El tipo de conduit no esta en los datos')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['tipo_conduit'] = tipo_conduit
		
		if not y.get('neutro') == None:		
			neutro = y.get('neutro').lower()
			if not (neutro == 'si' or neutro == 'no'):
				print('!ERROR¡. Dato no valido para el valor del neutro')
				n_errores = n_errores + 1
			datos_entrada_dict[x]['neutro'] = neutro
		
		datos_entrada_dict[x]['n_errores'] = n_errores
		datos_entrada_descripcion_dict['n_errores'] = 'número de errores'

		'''variables_datos_entrada_dict[x]['Sistema'] = Sistema

		variables_datos_entrada_dict[x]['Voltaje'] = Voltaje
		
		variables_datos_entrada_dict[x]['Carga'] = Carga

		variables_datos_entrada_dict[x]['factor_carga'] = factor_carga

		variables_datos_entrada_dict[x]['fp'] = fp

		variables_datos_entrada_dict[x]['caida_tension'] = caida_tension

		variables_datos_entrada_dict[x]['Longitud'] = Longitud

		variables_datos_entrada_dict[x]['Tambiente'] = Tambiente

		variables_datos_entrada_dict[x]['aislante_conductor'] = aislante_conductor

		variables_datos_entrada_dict[x]['Tconductor'] = Tconductor

		variables_datos_entrada_dict[x]['material_conductor'] = material_conductor

		variables_datos_entrada_dict[x]['numero_conductores_por_fase'] = numero_conductores_por_fase

		variables_datos_entrada_dict[x]['mismo'] = mismo

		variables_datos_entrada_dict[x]['ajuste_factor_carga'] = ajuste_factor_carga

		variables_datos_entrada_dict[x]['porcentaje_Irating'] = porcentaje_Irating

		variables_datos_entrada_dict[x]['Interruptor_forzado'] = Interruptor_forzado

		variables_datos_entrada_dict[x]['canalizacion'] = canalizacion
		
		variables_datos_entrada_dict[x]['material_canalizacion'] = material_canalizacion

		variables_datos_entrada_dict[x]['tipo_conduit'] = tipo_conduit

		variables_datos_entrada_dict[x]['neutro'] = neutro

		variables_datos_entrada_dict[x]['n_errores'] = n_errores'''

	return datos_entrada_dict


	