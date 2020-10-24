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
Sy = Symbol('Sy') #Integral (E*zdF)
Sz = Symbol('Sz') #Integral (E*ydF)
Iy = Symbol('Iy') #Integral (E*z^2dF)
Iz = Symbol('Iz') #Integral (E*y^2dF)
Ir = Symbol('Ir') #Integral (E*y*zdF)
Ik = Symbol('Ik') #Integral (G*ro^2dF)

#beam stiffness matrix
F = zeros(4,4)
F[0,0] = EF
F[0,1] = Sz
F[0,2] = Sy
F[0,3] = 0
F[1,0] = F[0,1]
F[1,1] = Iz
F[1,2] = Ir
F[1,3] = 0
F[2,0] = F[0,2]
F[2,1] = F[1,2]
F[2,2] = Iy
F[2,3] = 0
F[3,0] = 0
F[3,1] = 0
F[3,2] = 0
F[3,3] = Ik

#grid variables
u0 = Symbol('u0')
v0 = Symbol('v0')
w0 = Symbol('w0')
y0 = Symbol('y0')
z0 = Symbol('z0')
x0 = Symbol('x0')

u1 = Symbol('u1')
v1 = Symbol('v1')
w1 = Symbol('w1')
y1 = Symbol('y1')
z1 = Symbol('z1')
x1 = Symbol('x1')


#grid displacement vector
d = zeros(12,1)
d[0] = u0
d[1] = v0
d[2] = w0
d[3] = y0
d[4] = z0
d[5] = x0
d[6] = u1
d[7] = v1
d[8] = w1
d[9] = y1
d[10] = z1
d[11] = x1


#shape functions
L0 = 1 - x / l
L1 = x / l

ksi1 = 2 * (x / l)**3 - 3 * (x / l)**2 + 1
ksi2 = l * (-(x / l)**3 + 2 * (x / l)**2 - x / l)
ksi3 = -2 * (x / l)**3 + 3 * (x / l)**2
ksi4 = l * (-(x / l)**3 + (x / l)**2)

#displacement matrix
n = zeros(4,12)

n[0,0] = L0
n[0,6] = L1
n[1,1] = ksi1
n[1,4] = -ksi2
n[1,7] = ksi3
n[1,10] = -ksi4
n[2,2] = ksi1
n[2,3] = ksi2
n[2,8] = ksi3
n[2,9] = ksi4
n[3,5] = L0
n[3,11] = L1

nd = n*d

#displacement
u = nd[0,0]
v = nd[1,0]
w = nd[2,0]
fi = nd[3,0]

#strain
ex = diff(u,x) + y * diff(v,x,2) - z * diff(w,x,2)
gama = diff(fi,x)
#strain matrix
b = zeros(4,12)

b[0,0] = diff(L0,x)
b[0,6] = diff(L1,x)
b[1,1] = -diff(ksi1,x,2)
b[1,4] = diff(ksi2,x,2)
b[1,7] = -diff(ksi3,x,2)
b[1,10] = diff(ksi4,x,2)
b[2,2] = -diff(ksi1,x,2)
b[2,3] = -diff(ksi2,x,2)
b[2,8] = -diff(ksi3,x,2)
b[2,9] = -diff(ksi4,x,2)
b[3,5] = diff(L0,x)
b[3,11] = diff(L1,x)

bd = b*d

eps = bd[0,0] + z * bd[2,0] - y * bd[1,0]

e1 = simplify(eps - ex)

pprint(e1)

#specific deformation energy
sw = 1 / 2.0 * eps**2

#stiffness matrix
bdb = b.T*F*b

k = integrate(bdb,(x,0,l))
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


pprint(k - k.T)

#pprint(k)
