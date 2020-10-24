#!/usr/bin/python
from sympy import *

#init_printing()

#beam coordinate system
x = Symbol('x') #beam axis
y = Symbol('y') #section axis 1
z = Symbol('z') #section axis 2

l = Symbol('l') #element length

#section geometric parameters
EF = Symbol('EF') #Integral (EdF)
ESy = Symbol('ESy') #Integral (E*zdF)
ESz = Symbol('ESz') #Integral (E*ydF)
Iy = Symbol('Iy') #Integral (E*z^2dF)
Iz = Symbol('Iz') #Integral (E*y^2dF)
Ir = Symbol('Ir') #Integral (E*y*zdF)
Ik = Symbol('Ik') #Integral (G*ro^2dF)
fiy = Symbol('fiy') #fiy = 12EI / kzSGyl^2
fiz = Symbol('fiz') #fiz = 12EI / kzSGzl^2
Io = Symbol('Io') #Integral (E*omega^2dF), omega - warp function
Eo = Symbol('Eo') #Integral (E*omegadF)
Eoy = Symbol('Eoy') #Integral (E*omega*ydF)
Eoz = Symbol('Eoz') #Integral (E*omega*zdF)

#beam stiffness matrix
F = zeros(7,7)
F[0,0] = EF
F[0,1] = ESz
F[0,2] = ESy
F[0,4] = Eo
F[1,0] = F[0,1]
F[1,1] = Iz
F[1,2] = Ir
F[1,4] = Eoz
F[2,0] = F[0,2]
F[2,1] = F[1,2]
F[2,2] = Iy
F[2,4] = Eoy
F[3,3] = Ik
F[4,0] = F[0,4]
F[4,1] = F[1,4]
F[4,2] = F[2,4]
F[4,4] = Io

#pprint(F)

#grid variables
u0 = Symbol('u0')
v0 = Symbol('v0')
w0 = Symbol('w0')
y0 = Symbol('y0')
z0 = Symbol('z0')
x0 = Symbol('x0')
xx0 = Symbol('xx0')

u1 = Symbol('u1')
v1 = Symbol('v1')
w1 = Symbol('w1')
y1 = Symbol('y1')
z1 = Symbol('z1')
x1 = Symbol('x1')
xx1 = Symbol('xx1')

#grid displacement vector
d = zeros(14,1)
d[0] = u0
d[1] = v0
d[2] = w0
d[3] = y0
d[4] = z0
d[5] = x0
d[6] = xx0
d[7] = u1
d[8] = v1
d[9] = w1
d[10] = y1
d[11] = z1
d[12] = x1
d[13] = xx1

#shape functions
L0 = 1 - x / l
L1 = x / l

ksi1 = 2 * (x / l)**3 - 3 * (x / l)**2 + 1
ksi2 = l * (-(x / l)**3 + 2 * (x / l)**2 - x / l)
ksi3 = -2 * (x / l)**3 + 3 * (x / l)**2
ksi4 = l * (-(x / l)**3 + (x / l)**2)

'''
ksi1w = 1 / (1 + fiy) * (2 * (x / l)**3 - 3 * (x / l)**2 - fiy * (x / l) + (1 + fiy))
ksi2w = l / (1 + fiy) * (-(x / l)**3 + (4 + fiy) / 2 * (x /l)**2 - (2 + fiy) / 2 * (x / l))
ksi3w = 1 / (1 + fiy) * (-2 * (x / l)**3 + 3 * (x / l)**2 + fiy * (x / l) )
ksi4w = l / (1 + fiy) * (-(x / l)**3 + (2 - fiy) / 2 * (x /l)**2 + fiy / 2 * (x / l))

ksi5w = 6 / l / (1 + fiy) * (x / l) * (1 - x / l)
ksi6w = 1 / (1 + fiy) * ( 3 * (x / l)**2 - (4 + fiy) * (x / l) + (1 + fiy))
ksi7w = -6 / l / (1 + fiy) * (x / l) * (1 - x / l)
ksi8w = 1 / (1 + fiy) * ( 3 * (x / l)**2 + (-2 + fiy) * (x / l))

ksi1v = 1 / (1 + fiz) * (2 * (x / l)**3 - 3 * (x / l)**2 - fiz * (x / l) + (1 + fiz))
ksi2v = l / (1 + fiz) * (-(x / l)**3 + (4 + fiz) / 2 * (x /l)**2 - (2 + fiz) / 2 * (x / l))
ksi3v = 1 / (1 + fiz) * (-2 * (x / l)**3 + 3 * (x / l)**2 + fiz * (x / l) )
ksi4v = l / (1 + fiz) * (-(x / l)**3 + (2 - fiz) / 2 * (x /l)**2 + fiz / 2 * (x / l))

ksi5v = 6 / l / (1 + fiz) * (x / l) * (1 - x / l)
ksi6v = 1 / (1 + fiz) * ( 3 * (x / l)**2 - (4 + fiz) * (x / l) + (1 + fiz))
ksi7v = -6 / l / (1 + fiz) * (x / l) * (1 - x / l)
ksi8v = 1 / (1 + fiz) * ( 3 * (x / l)**2 + (-2 + fiz) * (x / l))
'''
N1 = (1 - x / l)**2 * (1 + 2 * x / l)
N2 = x * (1 - x / l)**2
N3 = (x / l)**2 * (3 - 2 * x / l)
N4 = x**2 / l * (x /l - 1)
'''
pprint(simplify(diff(N1,x,2) - 12 * x / l**3 + 6 / l**2))
pprint(simplify(diff(N2,x,2) - 6 * x / l**2 + 4 / l))
pprint(simplify(diff(N3,x,2) - 6 / l**2 + 12*x / l**3))
pprint(simplify(diff(N4,x,2) - 6*x/ l**2 + 2 / l))
pprint(simplify(diff(ksi5w,x)))
pprint(simplify(diff(ksi6w,x)))
pprint(simplify(diff(ksi7w,x)))
pprint(simplify(diff(ksi8w,x)))
'''
#displacement matrix
n = zeros(7,14)

n[0,0] = L0
n[0,7] = L1
n[1,1] = ksi1
n[1,4] = -ksi2
n[1,8] = ksi3
n[1,11] = -ksi4
n[2,2] = ksi1
n[2,3] = ksi2
n[2,9] = ksi3
n[2,10] = ksi4
n[3,2] = -diff(ksi1,x)
n[3,3] = -diff(ksi2,x)
n[3,9] = -diff(ksi3,x)
n[3,10] = -diff(ksi4,x)
n[4,1] = diff(ksi1,x)
n[4,4] = -diff(ksi2,x)
n[4,8] = diff(ksi3,x)
n[4,11] = -diff(ksi4,x)
n[5,5] = N1
n[5,6] = N2
n[5,12] = N3
n[5,13] = N4
n[6,5] = diff(N1,x)
n[6,6] = diff(N2,x)
n[6,12] = diff(N3,x)
n[6,13] = diff(N4,x)

nd = n*d

#displacement
u = nd[0,0]
v = nd[1,0]
w = nd[2,0]
ty = nd[3,0]
tz = nd[4,0]
fi = nd[5,0]
fixx = nd[6,0]

#strain matrix
b = zeros(7,14)

b[0,0] = diff(L0,x)
b[0,7] = diff(L1,x)
b[1,1] = -diff(ksi1,x,2)
b[1,4] = diff(ksi2,x,2)
b[1,8] = -diff(ksi3,x,2)
b[1,11] = diff(ksi4,x,2)
b[2,2] = -diff(ksi1,x,2)
b[2,3] = -diff(ksi2,x,2)
b[2,9] = -diff(ksi3,x,2)
b[2,10] = -diff(ksi4,x,2)
b[3,5] = diff(N1,x)
b[3,6] = diff(N2,x)
b[3,12] = diff(N3,x)
b[3,13] = diff(N4,x)
b[4,5] = diff(N1,x,2)
b[4,6] = diff(N2,x,2)
b[4,12] = diff(N3,x,2)
b[4,13] = diff(N4,x,2)

bd = b*d
'''
print "bd=\n"
pprint(simplify(bd))
print "\n"
'''
#stiffness matrix
bdb = b.T*F*b

k = simplify(integrate(bdb,(x,0,l)))

pprint(k[0,:])
pprint(k[1,1:])
pprint(k[2,2:])
pprint(k[3,3:])
pprint(k[4,4:])
pprint(k[5,5:])
pprint(k[6,6:])
pprint(k[7,7:])
pprint(k[8,8:])
pprint(k[9,9:])
pprint(k[10,10:])
pprint(k[11,11:])
pprint(k[12,12:])
pprint(k[13,13:])
pprint(k - k.T)
#'''
