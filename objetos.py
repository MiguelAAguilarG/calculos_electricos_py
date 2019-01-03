import datos
import tablas
import calculos
import validacion
import impresores

class Carga():
	'''__init__(self, datos_entrada_dict, datos_entrada_descripcion_dict)'''
	def __init__(self, datos_entrada_dict, datos_entrada_descripcion_dict):

		if not len(datos_entrada_dict) > 1:
			self.datos_entrada_dict = datos_entrada_dict
			self.datos_entrada_descripcion_dict = datos_entrada_descripcion_dict

			self.datos_entrada_dict = validacion.validacion(self.datos_entrada_dict, self.datos_entrada_descripcion_dict)
			impresores.impresor_entrada(self.datos_entrada_dict, self.datos_entrada_descripcion_dict)

			self.error_objeto_datos_tamano = False
		else:
			print('ERROR! Hay más de un conjunto de datos\n')
			self.error_objeto_datos_tamano = True

	def conectar(self):
		'''return I_nom, I_calculada, Carga_corregida'''
		try:
			if not self.error_objeto_datos_tamano:
				return self.datos_entrada_dict[list(self.datos_entrada_dict.keys())[0]]['conecciones']
		except:
			pass

	def corriente(self):
		'''return I_nom, I_calculada, Carga_corregida'''
		try:
			if not self.error_objeto_datos_tamano:
				return calculos.calculador_corriente(self.datos_entrada_dict[list(self.datos_entrada_dict.keys())[0]])
		except:
			pass

	def conductores_canalizacion(self):
		'''OK'''
		try:
			if not self.error_objeto_datos_tamano:
				return calculos.calculador_conductores_canalizacion(self.datos_entrada_dict[list(self.datos_entrada_dict.keys())[0]])
		except:
			pass

	def interruptor(self, Interruptores):
		'''OK'''
		try:
			if not self.error_objeto_datos_tamano:
				return calculos.calculador_interruptor(self.datos_entrada_dict[list(self.datos_entrada_dict.keys())[0]], self.corriente(), Interruptores = Interruptores)
		except:
			pass
class Cable(Carga):
	'''__init__(self, datos_entrada_dict, datos_entrada_descripcion_dict)'''


class Interruptor(Carga):
	"""docstring for ClassName"""
	def __init__(self):
		pass	

class Fuente(Carga):
	"""docstring for ClassName"""
	def __init__(self):
		pass	

if __name__ == '__main__':
	datos_entrada_dict = {}
	
	identificador = '0'
	datos_entrada_dict[identificador] = {}
	datos_entrada_dict[identificador]['nombre'] = 'Carga 0'
	datos_entrada_dict[identificador]['conecciones'] = ['0.0']
	datos_entrada_dict[identificador]['Sistema'] = 'trifásico'
	datos_entrada_dict[identificador]['Voltaje'] = 220
	datos_entrada_dict[identificador]['Carga'] = 10000
	datos_entrada_dict[identificador]['factor_carga'] = 1.25
	datos_entrada_dict[identificador]['fp'] = 0.9
	datos_entrada_dict[identificador]['caida_tension'] = 3
	datos_entrada_dict[identificador]['Longitud'] = 50
	datos_entrada_dict[identificador]['Tambiente'] = 30
	datos_entrada_dict[identificador]['aislante_conductor'] = 'THHW'
	datos_entrada_dict[identificador]['Tconductor'] = 60
	datos_entrada_dict[identificador]['material_conductor'] = 'cobre'
	datos_entrada_dict[identificador]['numero_conductores_por_fase'] = 1
	datos_entrada_dict[identificador]['mismo'] ='no'
	datos_entrada_dict[identificador]['ajuste_factor_carga'] = 1
	datos_entrada_dict[identificador]['porcentaje_Irating'] = 100
	datos_entrada_dict[identificador]['Interruptor_forzado'] = 0
	datos_entrada_dict[identificador]['canalizacion'] = 'conduit'
	datos_entrada_dict[identificador]['material_canalizacion'] = 'pvc'
	datos_entrada_dict[identificador]['tipo_conduit'] = 'EMT'
	datos_entrada_dict[identificador]['neutro'] = 'no'

	carga_1 = Carga(datos_entrada_dict, datos.descripcion())
	print(carga_1.corriente())
	print(carga_1.conductores_canalizacion())
	print(carga_1.interruptor(Interruptores = tablas.tablas()['Interruptores']))
	print(carga_1.conectar())
	print(carga_1.__main__)



		