from math import *
import datos
from tablas import tablas
from validacion import validacion
from impresores import impresor_entrada, impresor_salida
import calculos

if __name__ == '__main__':
	datos_entrada_dict = datos.datos()
	datos_entrada_descripcion_dict = datos.descripcion()
	datos_entrada_dict = validacion(datos_entrada_dict, datos_entrada_descripcion_dict)
	impresor_entrada(datos_entrada_dict, datos_entrada_descripcion_dict)
	datos_salida_dict = {}
	datos_salida_descripcion_dict = {}

	for x in datos_entrada_dict.keys():
		print(f'En el identificador: {x}')
		if datos_entrada_dict[x]['n_errores'] <= 0:
			print('BIEN. Los datos no tienen errores')
		else:
			print('Mal. Los datos tienen errores')

	for key, value in datos_entrada_dict.items():
		datos_salida_dict[key] = {}
		print(f'\nIdentificador: {key}')

		datos_salida_dict[key].update(calculos.calculador_corriente(datos_entrada_dict[key], datos_salida_dict[key]))
		datos_salida_dict[key].update(calculos.calculador_conductores_canalizacion(datos_entrada_dict[key], datos_salida_dict[key]))
		datos_salida_dict[key].update(calculos.calculador_interruptor(datos_entrada_dict[key], datos_salida_dict[key], Interruptores = tablas()['Interruptores']))
		datos_salida_dict[key].update(calculos.calculador_factor_temperatura(datos_entrada_dict[key], datos_salida_dict[key], Tambiente_tablas = tablas()['Ampacidad_tabla_310_15_b16']['Temperatura ambiente']))
		datos_salida_dict[key].update(calculos.calculador_factor_agrupamiento(datos_entrada_dict[key], datos_salida_dict[key], tabla_factor_agrupamiento = tablas()['tabla_factor_agrupamiento']))
		datos_salida_dict[key].update(calculos.calculador_cable_ampacidad(datos_entrada_dict[key], datos_salida_dict[key], tabla_de_Ampacidades = tablas()['Ampacidad_tabla_310_15_b16'], calibre_tabla = tablas()['calibres_tabla'], Area_conductor_tabla = tablas()['Area_conductor_tabla']))
		datos_salida_dict[key].update(calculos.calculador_cable_caida_de_tension(datos_entrada_dict[key], datos_salida_dict[key], tabla_de_impedancias = tablas()['impedancia_tabla_9'], calibre_tabla = tablas()['calibres_tabla'], Area_conductor_tabla  = tablas()['Area_conductor_tabla']))

		if datos_salida_dict[key]['indice_ampacidad'] > datos_salida_dict[key]['indice_caida']:
			datos_salida_dict[key]['calibre'] = datos_salida_dict[key]['calibre_ampacidad']
			datos_salida_dict[key]['indice'] = datos_salida_dict[key]['indice_ampacidad']
			datos_salida_dict[key]['Area_conductor'] = datos_salida_dict[key]['Area_ampacidad']
		else:
			datos_salida_dict[key]['calibre'] = datos_salida_dict[key]['calibre_caida']
			datos_salida_dict[key]['indice'] = datos_salida_dict[key]['indice_caida']
			datos_salida_dict[key]['Area_conductor'] = datos_salida_dict[key]['Area_caida']

		datos_salida_dict[key].update(calculos.calculador_cable_ampacidad(datos_entrada_dict[key], datos_salida_dict[key], tabla_de_Ampacidades = tablas()['Ampacidad_tabla_310_15_b16'], calibre_tabla = tablas()['calibres_tabla'], Area_conductor_tabla = tablas()['Area_conductor_tabla']))
		datos_salida_dict[key].update(calculos.calculador_cable_caida_de_tension(datos_entrada_dict[key], datos_salida_dict[key], tabla_de_impedancias = tablas()['impedancia_tabla_9'], calibre_tabla = tablas()['calibres_tabla'], Area_conductor_tabla  = tablas()['Area_conductor_tabla']))

		datos_salida_dict[key].update(calculos.calculador_cable_tierra_fisica(datos_entrada_dict[key], datos_salida_dict[key], interruptor_tierra_fisica_tabla = tablas()['interruptor_tierra_fisica_tabla_250_122'], tierra_fisica_tabla = tablas()['tierra_fisica_tabla_250_122'], calibre_tabla = tablas()['calibres_tabla'], Area_tierra_tabla  = tablas()['Area_conductor_tabla']))
		datos_salida_dict[key].update(calculos.calculador_tamano_conduit(datos_entrada_dict[key], datos_salida_dict[key], designacion_tubo_conduit_tabla = tablas()['designacion_tubo_conduit_tabla_4'], dimensiones_tubo_conduit_tabla = tablas()['dimensiones_tubo_conduit_tabla_4'], dimensiones_cables_tabla = tablas()['dimensiones_cables_tabla_5']))

		datos_salida_descripcion_dict = {}
		datos_salida_descripcion_dict['I_nom'] = 'I nominal (A)'
		datos_salida_descripcion_dict['I_calculada'] = 'I calculada (A)'
		datos_salida_descripcion_dict['Carga_corregida'] = 'Carga corregida (W)'
		datos_salida_descripcion_dict['conductores_canalizacion'] = 'conductores en la canalizacion (activos)'
		datos_salida_descripcion_dict['Interruptor_1'] = 'Interruptor 1 (A)'
		datos_salida_descripcion_dict['porcentaje_Irating_1_salida'] = 'Ajuste Irating 1 (%)'
		datos_salida_descripcion_dict['Interruptor_2'] = 'Interruptor 2 (A)'
		datos_salida_descripcion_dict['porcentaje_Irating_2_salida'] = 'Ajuste Irating 2 (%)'
		datos_salida_descripcion_dict['factor_temperatura'] = 'factor de temperatura'
		datos_salida_descripcion_dict['factor_agrupamiento'] = 'factor de agrupamiento'
		datos_salida_descripcion_dict['calibre'] = 'calibre'
		datos_salida_descripcion_dict['Area_conductor'] = 'Area del conductor (mm2)'
		datos_salida_descripcion_dict['Ampacidad'] = 'Ampacidad (A)'
		datos_salida_descripcion_dict['Ampacidad_corregida'] = 'Ampacidad corregida (A)'
		datos_salida_descripcion_dict['Ze'] = 'Ze (ohm)'
		datos_salida_descripcion_dict['caida_tension_calculada'] = 'caída de tensión calculada (%)'
		datos_salida_descripcion_dict['calibre_tierra_fisica'] = 'calibre tierra física'
		datos_salida_descripcion_dict['medida_tuberia_pulg'] = 'conduit (pulg)'
		datos_salida_descripcion_dict['medida_tuberia_mm'] = 'conduit (mm)'
		datos_salida_descripcion_dict['Area_total_conductores'] = 'Area total de los condutores en tubo conduit (mm2)'
		datos_salida_descripcion_dict['Area_conduit'] = 'Area tubo conduit (mm2)'
		datos_salida_descripcion_dict['porcentaje_ocupacion_calculado'] = 'ocupación del tubo conduit (%)'
		datos_salida_descripcion_dict['Area_cable'] = 'Area del cable (fases y neutros) (mm2)'
		datos_salida_descripcion_dict['Area_tierra_fisica'] = 'Area del cable de tierra fisica (mm2)'

	impresor_salida(datos_salida_dict, datos_salida_descripcion_dict)
	input('FIN')