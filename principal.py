from math import sqrt
from datos import datos
from tablas import tablas
from validacion import validacion
from impresores import impresor_entrada
import calculos

if __name__ == '__main__':
	datos_dict = datos()
	variables_datos_dict = validacion(datos_dict)
	impresor_entrada(datos_dict)

	for x in datos_dict.keys():
		print(f'En el nodo: {x}')
		if variables_datos_dict[x]['n_errores'] <= 0:
			print('BIEN. Los datos no tienen errores')
		else:
			print('Mal. Los datos tienen errores')

	for key,value in variables_datos_dict.items():
		I_nom, I_calculada, Carga_corregida = calculos.calcular_corriente(Sistema = value['Sistema'], Voltaje = value['Voltaje'], Carga = value['Carga'], fp = value['fp'], factor_carga = value['factor_carga'])
		conductores_canalizacion = calculos.calcular_conductores_canalizacion(Sistema = value['Sistema'], numero_conductores_por_fase = value['numero_conductores_por_fase'], mismo = value['mismo'], neutro = value['neutro'])
		Interruptor = calculos.calcular_interruptor(I_calculada = I_calculada, I_nom = I_nom,  Interruptores = tablas()['Interruptores'], Interruptor_forzado = value['Interruptor_forzado'], porcentaje_Irating = value['porcentaje_Irating'], factor_carga = value['factor_carga'], ajuste_factor_carga = value['ajuste_factor_carga'])
		factor_temperatura = calculos.calcular_factor_temperatura(Tconductor = value['Tconductor'], Tambiente = value['Tambiente'], Tambiente_tablas = tablas()['Ampacidad_tabla_310_15_b16'][0]['Temperatura ambiente'])
		factor_agrupamiento = calculos.calcular_factor_agrupamiento(conductores_canalizacion = conductores_canalizacion, tabla_factor_agrupamiento = tablas()['tabla_factor_agrupamiento'], Longitud = value['Longitud'])

	input('FIN')