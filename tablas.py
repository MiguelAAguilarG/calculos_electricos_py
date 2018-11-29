def tablas():

	Area_conductor_tabla = [2.08, 3.31, 5.26, 8.37, 13.3, 21.2, 26.7, 33.6, 42.4, 53.49, 67.43, 85.01, 107.2, 127.0, 152.0, 177.0, 203.0, 253.0, 304.0, 355.0, 380.0, 405.0, 456.0, 507.0, 633.0, 700.0, 887.0, 1013.0]

	calibres_tabla = ['14', '12', '10', '8', '6', '4', '3', '2', '1', '1/0', '2/0', '3/0', '4/0', '250', '300', '350', '400', '500', '600', '700', '750', '800', '900', '1000', '1250', '1500', '1750', '2000']

	Interruptores = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 125, 150, 175, 200, 225, 250, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600, 2000]

	tabla_factor_agrupamiento = {3:1, 6:0.8, 9:0.7, 20:0.5, 30:0.45, 40:0.4, 50:0.35}

	Ampacidad_tabla_310_15_b16 = []
	Ampacidad_tabla_310_15_b16.append({'Temperatura ambiente':30, 'numero maximo de conductores portadores de corriente':3, 'voltaje maximo':2000})
	Ampacidad_tabla_310_15_b16.append([])
	Ampacidad_tabla_310_15_b16[1].append([])
	Ampacidad_tabla_310_15_b16[1].append([])
	Ampacidad_tabla_310_15_b16[1][0].append([60, 75, 90])#Temperatura del aislante del conductor
	Ampacidad_tabla_310_15_b16[1][0].append([15, 20, 30, 40, 55, 70, 85, 90, 110, 125, 145, 165, 195, 215, 240, 260, 280, 320, 350, 385, 400, 410, 435, 455, 495, 525, 545, 555])
	Ampacidad_tabla_310_15_b16[1][0].append([20, 25, 35, 50, 65, 85, 100, 115, 130, 150, 175, 200, 230, 255, 285, 310, 335, 380, 420, 460, 475, 490, 520, 545, 590, 625, 650, 665])
	Ampacidad_tabla_310_15_b16[1][0].append([25, 30, 40, 55, 75, 95, 115, 130, 145, 170, 195, 225, 260, 290, 320, 350, 380, 430, 475, 520, 535, 555, 585, 615, 665, 705, 735, 750])
	Ampacidad_tabla_310_15_b16[1][1].append([60, 75, 90])#Temperatura del aislante del conductor
	Ampacidad_tabla_310_15_b16[1][1].append([0, 0, 0, 0, 40, 55, 65, 75, 85, 100, 115, 130, 150, 170, 195, 210, 225, 260, 285, 315, 320, 330, 355, 375, 405, 435, 455, 470])
	Ampacidad_tabla_310_15_b16[1][1].append([0, 0, 0, 0, 50, 65, 75, 90, 100, 120, 135, 155, 180, 205, 230, 250, 270, 310, 340, 375, 385, 395, 425, 445, 485, 520, 545, 560])
	Ampacidad_tabla_310_15_b16[1][1].append([0, 0, 0, 0, 55, 75, 85, 100, 115, 135, 150, 175, 205, 230, 260, 280, 305, 350, 385, 425, 435, 445, 480, 500, 545, 585, 615, 630])

	interruptor_tierra_fisica_tabla_250_122 = [15, 20, 60, 100, 200, 300, 400, 500, 600, 800, 1000, 1200, 1600, 2000, 2500, 3000, 400, 4000, 5000, 6000]

	tierra_fisica_tabla_250_122 = []
	tierra_fisica_tabla_250_122.append(['14', '12', '10', '8', '6', '4', '2', '2', '1', '1/0', '2/0', '3/0', '4/0', '250', '350', '400', '500', '700', '800'])
	tierra_fisica_tabla_250_122.append(['0', '0', '0', '0', '4', '2', '1', '1/0', '2/0', '3/0', '4/0', '250', '350', '400', '600', '600', '750', '1200', '1200'])

	dimensiones_cables_tabla_5 = []
	dimensiones_cables_tabla_5.append(['tipo de cable','diametro','area'])
	dimensiones_cables_tabla_5.append([])
	dimensiones_cables_tabla_5[1].append(['THW','THHW','THW-2'])
	dimensiones_cables_tabla_5.append([])
	dimensiones_cables_tabla_5[2].append([3.378, 3.861, 4.470, 5.994, 7.722, 8.941, 9.652, 10.46, 12.50, 13.51, 14.68, 16.00, 17.48, 19.43, 20.83, 22.12, 23.32, 25.48, 28.27, 30.07, 30.94, 31.75, 33.38, 34.85, 39.09, 42.21, 45.1, 47.80])
	dimensiones_cables_tabla_5.append([])
	dimensiones_cables_tabla_5[3].append([8.968, 11.68, 15.68, 28.19, 46.84, 62.77, 73.16, 86.00, 122.60, 143.40, 169.30, 201.1, 239.90, 296.5, 340.7, 384.40, 427.00, 509.70, 627.7, 710.3, 751.7, 791.7, 874.9, 953.8, 1200, 1400, 1598, 1795])

	tablas_dict = {}

	tablas_dict['Area_conductor_tabla'] = Area_conductor_tabla
	tablas_dict['calibres_tabla'] = calibres_tabla
	tablas_dict['Interruptores'] = Interruptores
	tablas_dict['tabla_factor_agrupamiento'] = tabla_factor_agrupamiento
	tablas_dict['Ampacidad_tabla_310_15_b16'] = Ampacidad_tabla_310_15_b16
	tablas_dict['interruptor_tierra_fisica_tabla_250_122'] =  interruptor_tierra_fisica_tabla_250_122
	tablas_dict['tierra_fisica_tabla_250_122'] = tierra_fisica_tabla_250_122
	tablas_dict['dimensiones_cables_tabla_5'] = dimensiones_cables_tabla_5

	return tablas_dict