import calculos
import validacion

datos_dict = {}

class Carga():
	"""__init__(self,dict,nodo,nombre,conecciones,sistema,voltaje,carga,factor_de_carga,factor_de_potencia)"""
	def __init__(self,
		datos_dict,
		nodo,
		nombre,
		conecciones,
		sistema,
		voltaje,
		carga,
		factor_de_carga,
		factor_de_potencia):
		
		self.nodo = nodo
		self.datos_dict = datos_dict
		self.datos_dict[self.nodo] = {}
		self.datos_dict[self.nodo]['nombre'] = [nombre, 'Nombre']
		self.datos_dict[self.nodo]['conecciones'] = [conecciones, 'Conecciones']
		self.datos_dict[self.nodo]['sistema'] = [sistema, 'Sistema (\'monofásico\',  \'trifásico\')']
		self.datos_dict[self.nodo]['voltaje'] = [voltaje, 'Voltaje (V)']
		self.datos_dict[self.nodo]['carga'] = [carga, 'Carga (W)']
		self.datos_dict[self.nodo]['factor de carga'] = [factor_de_carga, 'Factor de carga (nueva carga = Carga*factor de carga)']
		self.datos_dict[self.nodo]['factor de potencia'] = [factor_de_potencia, 'factor de potencia (>0-1)']

		self.variables_datos_dict = validacion.validacion(self.datos_dict)

	def corriente(self):
		'''return I_nom, I_calculada, Carga_corregida'''
		return calculos.calculador_corriente(
		self.variables_datos_dict[self.nodo]['Sistema'], 
		self.variables_datos_dict[self.nodo]['Voltaje'], 
		self.variables_datos_dict[self.nodo]['Carga'], 
		self.variables_datos_dict[self.nodo]['fp'], 
		self.variables_datos_dict[self.nodo]['factor_carga'])

class Cable():
	"""docstring for ClassName"""
	def __init__(self):
		pass	

class Interruptor():
	"""docstring for ClassName"""
	def __init__(self):
		pass	

class Fuente():
	"""docstring for ClassName"""
	def __init__(self):
		pass	



carga_1 = Carga(datos_dict, '1', 'carga_1', None, 'trifásico', 220, 5000, 1.25, 0.9)

print(carga_1.corriente())


		