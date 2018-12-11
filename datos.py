from math import sqrt

def datos():
	datos_dict = {}

	nodo = '0'
	datos_dict[nodo] = {}
	datos_dict[nodo]['nombre'] = ['Carga 0', 'Nombre']
	datos_dict[nodo]['conecciones'] = [None, 'Conecciones']
	datos_dict[nodo]['sistema'] = ['trifásico', 'Sistema (\'monofásico\',  \'trifásico\')']
	datos_dict[nodo]['voltaje'] = [460, 'Voltaje (V)']
	datos_dict[nodo]['carga'] = [sqrt(3)*515*460*.79, 'Carga (W)']
	datos_dict[nodo]['factor de carga'] = [1.25, 'Factor de carga (nueva carga = Carga*factor de carga)']
	datos_dict[nodo]['factor de potencia'] = [0.79, 'factor de potencia (>0-1)']
	datos_dict[nodo]['caída de tensión'] = [3, 'Caída de tensión (%)']
	datos_dict[nodo]['longitud'] = [55, 'Longitud (m)']
	datos_dict[nodo]['conductores activos adicionales'] = [0, 'Conductores activos adicionales en la misma canalización aparte del circuito calculado. El programa no considera los neutros (sistemas trifásicos) y tierras fisicas del circuito calculado']
	datos_dict[nodo]['temperatura ambiente'] = [40, 'Temperatura ambiente (°C)']
	datos_dict[nodo]['aislante conductor'] = ['THHW', 'Aislante del conductor NOTA: todo en mayusculas']
	datos_dict[nodo]['temperatura del aislante del conductor'] = [75, 'Temperatura del aislante del conductor (°C)']
	datos_dict[nodo]['material del conductor'] = ['cobre', 'Material del conductor (\'cobre\', \'aluminio\')']
	datos_dict[nodo]['conductores por fase'] = [3 , 'Número de conductores por fase, si hay neutro, sera el mismo número de conductores para el neutro']
	datos_dict[nodo]['colocar conductores en la misma canalización'] = ['no', 'Colocar el total de los conductores de fase y neutro en la misma canalización?: (\'si\' Nada recomendable cuando es mas de un conductor por fase,\'no\')']
	datos_dict[nodo]['ajuste interruptor'] = [1 , 'Ajuste hacia abajo en caso de no encontrar interruptor cercano con Factor de carga establecido (nuevo factor = factor de carga-Ajuste) (%)']
	datos_dict[nodo]['ajuste Irating interruptor'] = [80, 'Ajuste Irating interruptor (%)']
	datos_dict[nodo]['interruptor forzado'] = [800, 'Interruptor forzado (A) NOTA: NO APLICA = 0']
	datos_dict[nodo]['canalización'] = ['conduit', 'Canalizacion (\'conduit\',\'charola\')']
	datos_dict[nodo]['material canalización'] = ['pvc', 'Material de la canalizacion: (\'acero\', \'pvc\', \'aluminio\')']
	datos_dict[nodo]['tipo conduit'] = ['EMT', 'Tipo de canalización']
	datos_dict[nodo]['neutro del sistema trifásico'] = ['no', 'Colocar neutro en el sistema trifásico: (\'si\',\'no\')']

	nodo = '1'
	datos_dict[nodo] = {}
	datos_dict[nodo]['nombre'] = ['Carga 0', 'Nombre']
	datos_dict[nodo]['conecciones'] = [None, 'Conecciones']
	datos_dict[nodo]['sistema'] = ['trifásico', 'Sistema (\'monofásico\',  \'trifásico\')']
	datos_dict[nodo]['voltaje'] = [220, 'Voltaje (V)']
	datos_dict[nodo]['carga'] = [5000, 'Carga (W)']
	datos_dict[nodo]['factor de carga'] = [1.25, 'Factor de carga (nueva carga = Carga*factor de carga)']
	datos_dict[nodo]['factor de potencia'] = [0.9, 'factor de potencia (>0-1)']
	datos_dict[nodo]['caída de tensión'] = [3, 'Caída de tensión (%)']
	datos_dict[nodo]['longitud'] = [50, 'Longitud (m)']
	datos_dict[nodo]['conductores activos adicionales'] = [0, 'Conductores activos adicionales en la misma canalización aparte del circuito calculado. El programa no considera los neutros (sistemas trifásicos) y tierras fisicas del circuito calculado']
	datos_dict[nodo]['temperatura ambiente'] = [30, 'Temperatura ambiente (°C)']
	datos_dict[nodo]['aislante conductor'] = ['THHW', 'Aislante del conductor NOTA: todo en mayusculas']
	datos_dict[nodo]['temperatura del aislante del conductor'] = [75, 'Temperatura del aislante del conductor (°C)']
	datos_dict[nodo]['material del conductor'] = ['cobre', 'Material del conductor (\'cobre\', \'aluminio\')']
	datos_dict[nodo]['conductores por fase'] = [1 , 'Número de conductores por fase, si hay neutro, sera el mismo número de conductores para el neutro']
	datos_dict[nodo]['colocar conductores en la misma canalización'] = ['no', 'Colocar el total de los conductores de fase y neutro en la misma canalización?: (\'si\' Nada recomendable cuando es mas de un conductor por fase,\'no\')']
	datos_dict[nodo]['ajuste interruptor'] = [0 , 'Ajuste hacia abajo en caso de no encontrar interruptor cercano con Factor de carga establecido (nuevo factor = factor de carga-Ajuste) (%)']
	datos_dict[nodo]['ajuste Irating interruptor'] = [100, 'Ajuste Irating interruptor (%)']
	datos_dict[nodo]['interruptor forzado'] = [0, 'Interruptor forzado (A) NOTA: NO APLICA = 0']
	datos_dict[nodo]['canalización'] = ['conduit', 'Canalizacion (\'conduit\',\'charola\')']
	datos_dict[nodo]['material canalización'] = ['acero', 'Material de la canalizacion: (\'acero\', \'pvc\', \'aluminio\')']
	datos_dict[nodo]['tipo conduit'] = ['EMT', 'Tipo de canalización']
	datos_dict[nodo]['neutro del sistema trifásico'] = ['si', 'Colocar neutro en el sistema trifásico: (\'si\',\'no\')']

	return datos_dict