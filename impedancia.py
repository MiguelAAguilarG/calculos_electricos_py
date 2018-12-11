from math import sqrt
from math import log1p
from math import pi
from math import pow
from math import exp

d_in = 2.95
d_ext = 4.47

'''d_in = 13.41
d_ext = 17.48
d_ext = 30'''

f = 60
Longitud = 1


DAB = d_ext
DBC = d_ext
DAC = d_ext

DMG = pow(DAB*DBC*DAC,1/3)

RMG = d_in/2*exp(-1/4)

L = 2*1e-4*log1p(DMG/RMG) #H/km
XL = 2*pi*f*L*Longitud
####################################
'''for x in range(1,100,1):
	d_ext = x

	DAB = d_ext
	DBC = d_ext
	DAC = d_ext

	DMG = pow(DAB*DBC*DAC,1/3)

	RMG = d_in/2*exp(-1/4)

	L = 2*1e-4*log1p(DMG/RMG) #H/km
	XL = 2*pi*f*L*Longitud

	print(XL)'''

'''for x in range(1,100,1):
	d_in = x
	Ys = 7.5*(f**2)*((d_in/10)**4)*1e-7
	print(Ys)'''

Ys = 7.5*(f**2)*((d_in/10)**4)*1e-7
Ys = 9
Tc = 75
Ta = 30
deltaTd = 0
Rca = 90
Rcc = 3.9*1e-3*1e-2
#Rcc = 0.203*10e-5

I = sqrt((Tc-(Ta+deltaTd))/(Rcc*(1+Ys)*Rca))

print('Ys: ',Ys)
print('XL: ',XL)
print('I: ',I)
