from tablas import tablas

def validacion(datos_dict):
	variables_datos_dict = {}
	for x,y in datos_dict.items():
		n_errores = 0
		variables_datos_dict[x] = {}

		if not y.get('sistema') == None:
			Sistema = y.get('sistema')[0]

			if not (Sistema == 'monofásico' or Sistema == 'trifásico'):
				print('!ERROR¡. El sistema ingresado no es correcto. Debe ser \'trifásico\' o \'monofásico\'')
				n_errores = n_errores + 1
			variables_datos_dict[x]['Sistema'] = Sistema
		
		if not y.get('voltaje') == None:
			Voltaje = y.get('voltaje')[0]
			if Voltaje <= 0:
				print('!ERROR¡. El voltaje es menor o igual a 0')
				n_errores = n_errores + 1
			variables_datos_dict[x]['Voltaje'] = Voltaje
		
		if not y.get('carga') == None:
			Carga = y.get('carga')[0]
			if Carga <= 0:
				print('!ERROR¡. La carga es menor o igual a 0')
				n_errores = n_errores + 1
			variables_datos_dict[x]['Carga'] = Carga

		if not y.get('factor de carga') == None:		
			factor_carga = y.get('factor de carga')[0]
			if factor_carga <= 0:
				print('!ERROR¡. El factor de carga es menor o igual a 0')
				n_errores = n_errores + 1
			variables_datos_dict[x]['factor_carga'] = factor_carga
		
		if not y.get('factor de potencia') == None:	
			fp = y.get('factor de potencia')[0]
			if fp < 0:
				print('!ERROR¡. El factor de potencia es menor a 0')
				n_errores = n_errores + 1
			elif fp > 1:
				print('!ERROR¡. El factor de potencia es mayor a 1')
				n_errores = n_errores + 1
			variables_datos_dict[x]['fp'] = fp
			
		if not y.get('caída de tensión') == None:	
			caida_tension = y.get('caída de tensión')[0]
			if caida_tension <= 0:
				print('!ERROR¡. La caída de tensión es menor o igual a 0%')
				n_errores = n_errores + 1
			elif caida_tension > 3:
				print('!ERROR¡. La caída de tensión es mayor a 3%')
				n_errores = n_errores + 1
			variables_datos_dict[x]['caida_tension'] = caida_tension
		
		if not y.get('longitud') == None:
			Longitud = y.get('longitud')[0]
			if Longitud <= 0:
				print('!ERROR¡. La longitud es menor o igual a 0')
				n_errores = n_errores + 1
			variables_datos_dict[x]['Longitud'] = Longitud

		'''n = n + 1; 
		conductores_canalizacion = round(datos(n));
		if conductores_canalizacion < 0
		  print('!ERROR. El numero de conductores es menor a 0');
		  n_errores = n_errores + 1;
		elseif conductores_canalizacion > 50
		  print('!ERROR. El numero de conductores es mayor a 50. Son demasiados conductores');
		  n_errores = n_errores + 1;'''
		if not y.get('temperatura ambiente') == None:
			Tambiente = y.get('temperatura ambiente')[0]
			variables_datos_dict[x]['Tambiente'] = Tambiente
		
		if not y.get('aislante conductor') == None:
			aislante_conductor = y.get('aislante conductor')[0]
			lista_aux1 = []		
			for a in tablas()['dimensiones_cables_tabla_5'].keys():
				lista_aux1 = lista_aux1 + a.split(',')
			lista_aux2 = []
			for a in lista_aux1:
				lista_aux2.append(a.strip())
			if not aislante_conductor in lista_aux2:
				print('!ERROR¡. El aislante del conductor no esta en los datos')
				n_errores = n_errores + 1
			variables_datos_dict[x]['aislante_conductor'] = aislante_conductor
		
		if not y.get('temperatura del aislante del conductor') == None:
			Tconductor = y.get('temperatura del aislante del conductor')[0]
			if not (Tconductor == 60 or Tconductor == 75 or Tconductor == 90):
				print('!ERROR¡. La temperatura del aislante del conductor no es correcta')
				n_errores = n_errores + 1
			variables_datos_dict[x]['Tconductor'] = Tconductor
		
		if not y.get('material del conductor') == None:
			material_conductor = y.get('material del conductor')[0]
			if not (material_conductor == 'cobre' or material_conductor == 'aluminio'):
				print('!ERROR¡. El material del conductor no es correcto')
				n_errores = n_errores + 1
			variables_datos_dict[x]['material_conductor'] = material_conductor

		if not y.get('conductores por fase') == None:
			numero_conductores_por_fase = y.get('conductores por fase')[0]
			if numero_conductores_por_fase <= 0:
				print('!ERROR¡. El numero de conductores por fase es menor o igual a 0')
				n_errores = n_errores + 1
			variables_datos_dict[x]['numero_conductores_por_fase'] = numero_conductores_por_fase
		
		if not y.get('colocar conductores en la misma canalización') == None:
			mismo = y.get('colocar conductores en la misma canalización')[0]
			if not (mismo == 'si' or mismo == 'no'):
				print('!ERROR¡. Dato no valido para colocar conductores de fase y neutro en la misma canalizacion cuando es más de un conductor por fase')
				n_errores = n_errores + 1
			variables_datos_dict[x]['mismo'] = mismo
		
		if not y.get('ajuste interruptor') == None:
			ajuste_factor_carga = y.get('ajuste interruptor')[0]
			if ajuste_factor_carga < 0 or ajuste_factor_carga > 100:
				print('!ERROR¡. Dato no valido. No corresponde a un porcentaje real para ajuste del interruptor')
				n_errores = n_errores + 1
			variables_datos_dict[x]['ajuste_factor_carga'] = ajuste_factor_carga
		
		if not y.get('ajuste Irating interruptor') == None:
			porcentaje_Irating = y.get('ajuste Irating interruptor')[0]
			if porcentaje_Irating <= 0 or porcentaje_Irating > 100:
				print('!ERROR¡. Dato no valido. No corresponde a un porcentaje real para Irating del interruptor')
				n_errores = n_errores + 1
			variables_datos_dict[x]['porcentaje_Irating'] = porcentaje_Irating
		
		if not y.get('interruptor forzado') == None:
			Interruptor_forzado = y.get('interruptor forzado')[0]
			if Interruptor_forzado < 0:
				print('!ERROR¡. Dato no valido. Amperaje de interruptor forzado negativo')
				n_errores = n_errores + 1
			variables_datos_dict[x]['Interruptor_forzado'] = Interruptor_forzado
		
		if not y.get('canalización') == None:
			canalizacion = y.get('canalización')[0]
			if not (canalizacion == 'conduit' or canalizacion == 'charola'):
				print('!ERROR¡. Dato no valido. No es una canalizacion')
				n_errores = n_errores + 1
			variables_datos_dict[x]['canalizacion'] = canalizacion
		
		if not y.get('material canalización') == None:		
			material_canalizacion = y.get('material canalización')[0]
			if not (material_canalizacion == 'acero' or material_canalizacion == 'pvc' or material_canalizacion == 'aluminio'):
				print('!ERROR¡. Dato no valido. No es un material de canalizacion')
				print(material_canalizacion)
				n_errores = n_errores + 1
			variables_datos_dict[x]['material_canalizacion'] = material_canalizacion
		
		if not y.get('tipo conduit') == None:
			tipo_conduit = y.get('tipo conduit')[0]
			if not tipo_conduit in tablas()['dimensiones_tubo_conduit_tabla_4'].keys():
				print('!ERROR¡. El tipo de conduit no esta en los datos')
				n_errores = n_errores + 1
			variables_datos_dict[x]['tipo_conduit'] = tipo_conduit
		
		if not y.get('neutro del sistema trifásico') == None:		
			neutro = y.get('neutro del sistema trifásico')[0]
			if not (neutro == 'si' or neutro == 'no'):
				print('!ERROR¡. Dato no valido para el valor del neutro')
				n_errores = n_errores + 1
			variables_datos_dict[x]['neutro'] = neutro
		
		if n_errores > 0:
			print(f'Numero de errores: {n_errores}')
		variables_datos_dict[x]['n_errores'] = n_errores

		'''variables_datos_dict[x]['Sistema'] = Sistema

		variables_datos_dict[x]['Voltaje'] = Voltaje
		
		variables_datos_dict[x]['Carga'] = Carga

		variables_datos_dict[x]['factor_carga'] = factor_carga

		variables_datos_dict[x]['fp'] = fp

		variables_datos_dict[x]['caida_tension'] = caida_tension

		variables_datos_dict[x]['Longitud'] = Longitud

		variables_datos_dict[x]['Tambiente'] = Tambiente

		variables_datos_dict[x]['aislante_conductor'] = aislante_conductor

		variables_datos_dict[x]['Tconductor'] = Tconductor

		variables_datos_dict[x]['material_conductor'] = material_conductor

		variables_datos_dict[x]['numero_conductores_por_fase'] = numero_conductores_por_fase

		variables_datos_dict[x]['mismo'] = mismo

		variables_datos_dict[x]['ajuste_factor_carga'] = ajuste_factor_carga

		variables_datos_dict[x]['porcentaje_Irating'] = porcentaje_Irating

		variables_datos_dict[x]['Interruptor_forzado'] = Interruptor_forzado

		variables_datos_dict[x]['canalizacion'] = canalizacion
		
		variables_datos_dict[x]['material_canalizacion'] = material_canalizacion

		variables_datos_dict[x]['tipo_conduit'] = tipo_conduit

		variables_datos_dict[x]['neutro'] = neutro

		variables_datos_dict[x]['n_errores'] = n_errores'''

	return variables_datos_dict


	