from math import *
from datos import datos
from tablas import tablas
from validacion import validacion
from impresores import impresor_entrada, impresor_salida
import calculos

if __name__ == '__main__':
	datos_dict = datos()
	variables_datos_dict = validacion(datos_dict)
	impresor_entrada(datos_dict)
	salida_dict = {}

	for x in datos_dict.keys():
		print(f'En el nodo: {x}')
		if variables_datos_dict[x]['n_errores'] <= 0:
			print('BIEN. Los datos no tienen errores')
		else:
			print('Mal. Los datos tienen errores')

	for key,value in variables_datos_dict.items():
		print(f'\nnodo: {key}')
		I_nom, I_calculada, Carga_corregida = calculos.calculador_corriente(
			Sistema = value['Sistema'], 
			Voltaje = value['Voltaje'], 
			Carga = value['Carga'], 
			fp = value['fp'], 
			factor_carga = value['factor_carga'])
		conductores_canalizacion = calculos.calculador_conductores_canalizacion(
			Sistema = value['Sistema'], 
			numero_conductores_por_fase = value['numero_conductores_por_fase'], 
			mismo = value['mismo'], 
			neutro = value['neutro'])
		Interruptor = calculos.calculador_interruptor(
			I_calculada = I_calculada, 
			I_nom = I_nom,  
			Interruptores = tablas()['Interruptores'], 
			Interruptor_forzado = value['Interruptor_forzado'], 
			porcentaje_Irating = value['porcentaje_Irating'], 
			factor_carga = value['factor_carga'], 
			ajuste_factor_carga = value['ajuste_factor_carga'])
		factor_temperatura = calculos.calculador_factor_temperatura(
			Tconductor = value['Tconductor'], 
			Tambiente = value['Tambiente'], 
			Tambiente_tablas = tablas()['Ampacidad_tabla_310_15_b16']['Temperatura ambiente'])
		factor_agrupamiento = calculos.calculador_factor_agrupamiento(
			conductores_canalizacion = conductores_canalizacion, 
			tabla_factor_agrupamiento = tablas()['tabla_factor_agrupamiento'], 
			Longitud = value['Longitud'])
		indice_Ampacidad, calibre_Ampacidad, Area_Ampacidad, Ampacidad, Ampacidad_corregida = calculos.calculador_cable_ampacidad(
			tabla_de_Ampacidades = tablas()['Ampacidad_tabla_310_15_b16'], 
			calibre_tabla = tablas()['calibres_tabla'], 
			Area_conductor_tabla = tablas()['Area_conductor_tabla'], 
			Interruptor = Interruptor, 
			numero_conductores_por_fase = value['numero_conductores_por_fase'], 
			material_conductor = value['material_conductor'], 
			Tconductor = value['Tconductor'], 
			factor_agrupamiento = factor_agrupamiento, 
			factor_temperatura = factor_temperatura)
		indice_caida, calibre_caida, Area_caida, Ze, caida_tension_calculada = calculos.calculador_cable_caida_de_tension(
			tabla_de_impedancias = tablas()['impedancia_tabla_9'], 
			calibre_tabla = tablas()['calibres_tabla'], 
			Area_conductor_tabla  = tablas()['Area_conductor_tabla'], 
			Sistema = value['Sistema'], 
			fp = value['fp'], 
			Longitud = value['Longitud'], 
			I_nom = I_nom, 
			Voltaje = value['Voltaje'], 
			caida_tension = value['caida_tension'], 
			numero_conductores_por_fase = value['numero_conductores_por_fase'], 
			material_conductor = value['material_conductor'], 
			material_canalizacion = value['material_canalizacion'])
		
		if indice_Ampacidad > indice_caida:
			calibre = calibre_Ampacidad
		else:
			calibre = calibre_caida

		indice, calibre, Area_conductor, Ampacidad, Ampacidad_corregida = calculos.calculador_cable_ampacidad(
			calibre = calibre, 
			tabla_de_Ampacidades = tablas()['Ampacidad_tabla_310_15_b16'], 
			calibre_tabla = tablas()['calibres_tabla'], 
			Area_conductor_tabla = tablas()['Area_conductor_tabla'], 
			Interruptor = Interruptor, 
			numero_conductores_por_fase = value['numero_conductores_por_fase'], 
			material_conductor = value['material_conductor'], 
			Tconductor = value['Tconductor'], 
			factor_agrupamiento = factor_agrupamiento, 
			factor_temperatura = factor_temperatura)
		indice, calibre, Area_conductor, Ze, caida_tension_calculada = calculos.calculador_cable_caida_de_tension(
			calibre = calibre, 
			tabla_de_impedancias = tablas()['impedancia_tabla_9'], 
			calibre_tabla = tablas()['calibres_tabla'], 
			Area_conductor_tabla  = tablas()['Area_conductor_tabla'], 
			Sistema = value['Sistema'], 
			fp = value['fp'], 
			Longitud = value['Longitud'], 
			I_nom = I_nom, 
			Voltaje = value['Voltaje'], 
			caida_tension = value['caida_tension'], 
			numero_conductores_por_fase = value['numero_conductores_por_fase'], 
			material_conductor = value['material_conductor'], 
			material_canalizacion = value['material_canalizacion'])

		calibre_tierra_fisica, Area_tierra_fisica = calculos.calculador_cable_tierra_fisica(
			interruptor_tierra_fisica_tabla = tablas()['interruptor_tierra_fisica_tabla_250_122'], 
			tierra_fisica_tabla = tablas()['tierra_fisica_tabla_250_122'],  
			calibre_tabla = tablas()['calibres_tabla'], 
			Area_tierra_tabla  = tablas()['Area_conductor_tabla'], 
			Interruptor = Interruptor, 
			material_conductor_tierra = value['material_conductor'], 
			canalizacion = value['canalizacion'])

		medida_tuberia_pulg, medida_tuberia_mm, Area_total_conductores, Area_conduit, porcentaje_ocupacion_calculado, Area_cable, Area_tierra_fisica = calculos.calculador_tamano_conduit(
			designacion_tubo_conduit = tablas()['designacion_tubo_conduit_tabla_4'],
			dimensiones_tubo_conduit = tablas()['dimensiones_tubo_conduit_tabla_4'],
			dimensiones_cables = tablas()['dimensiones_cables_tabla_5'], 
			conductores_canalizacion = conductores_canalizacion,
			aislante_conductor = value['aislante_conductor'],
			tipo_conduit = value['tipo_conduit'],
			indice_conductor = indice, 
			calibre_tierra_fisica = calibre_tierra_fisica, 
			Area_tierra_fisica = Area_tierra_fisica)
	
		salida_dict[key] = {}
		salida_dict[key]['I nominal (A)'] = I_nom
		salida_dict[key]['I calculada (A)'] = I_calculada
		salida_dict[key]['Carga corregida (W)'] = Carga_corregida
		salida_dict[key]['conductores en la canalizacion (activos)'] = conductores_canalizacion
		salida_dict[key]['Interruptor (A)'] = Interruptor
		salida_dict[key]['factor de temperatura'] = factor_temperatura
		salida_dict[key]['factor de agrupamiento'] = factor_agrupamiento
		salida_dict[key]['calibre'] = calibre
		salida_dict[key]['Area del conductor (mm2)'] = Area_conductor
		salida_dict[key]['Ampacidad (A)'] = Ampacidad
		salida_dict[key]['Ampacidad corregida (A)'] = Ampacidad_corregida
		salida_dict[key]['Ze (ohm)'] = Ze
		salida_dict[key]['caída de tensión calculada (%)'] = caida_tension_calculada
		salida_dict[key]['calibre tierra física'] = calibre_tierra_fisica
		salida_dict[key]['conduit (pulg)'] = medida_tuberia_pulg
		salida_dict[key]['conduit (mm)'] = medida_tuberia_mm
		salida_dict[key]['Area total de los condutores en tubo conduit (mm2)'] = Area_total_conductores
		salida_dict[key]['Area tubo conduit (mm2)'] = Area_conduit
		salida_dict[key]['ocupación del tubo conduit (%)'] = porcentaje_ocupacion_calculado
		salida_dict[key]['Area del cable (fases y neutros) (mm2)'] = Area_cable
		salida_dict[key]['Area del cable de tierra fisica (mm2)'] = Area_tierra_fisica

	impresor_salida(salida_dict)
	input('FIN')