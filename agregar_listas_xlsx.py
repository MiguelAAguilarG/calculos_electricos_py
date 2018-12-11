import openpyxl

nombre_direccion_libro_1 = r'C:\Users\Miguel\Desktop\NOM'
nombre_libro_1 = 'TABLA 4. PORCENTAJE DISPONIBLE.xlsx'
nombre_hoja_1 = 'Table 1'

wb = openpyxl.load_workbook(nombre_direccion_libro_1 + '\\' + nombre_libro_1)
hoja = wb[nombre_hoja_1]

a = 0
b = 0
c = False
verbs_iregular = []

for i in range(84,90):
	f = hoja.cell(row=i, column=4).value
	verbs_iregular.append(f)

print(verbs_iregular)
print(len(verbs_iregular))