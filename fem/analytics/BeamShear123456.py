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
Fy = Symbol('Fy') #Integral (GxydF) = 12 * Iy / fiy / l**2 
Fz = Symbol('Fz') #Integral (GxzdF) = 12 * Iz / fiz / l**2
GSy = Symbol('GSy') #Integral (Gxy*zdF)
GSz = Symbol('GSz') #Integral (Gxz*ydF)
Ik = Symbol('Ik') #Integral (G*ro^2dF)
fiy = Symbol('fiy') #fiy = 12EI / kzSGyl^2
fiz = Symbol('fiz') #fiz = 12EI / kzSGzl^2

#beam stiffness matrix
F = zeros(6,6)
F[0,0] = EF
F[0,3] = ESz
F[0,4] = ESy
F[1,1] = 12 * Iz / fiz / l**2
F[1,5] = -GSy
F[2,2] = 12 * Iy / fiy / l**2
F[2,5] = GSz
F[3,0] = ESz
F[3,3] = Iy
F[3,4] = Ir
F[4,0] = ESy
F[4,3] = Ir
F[4,4] = Iz
F[5,1] = -GSy
F[5,2] = GSz
F[5,5] = Ik

#pprint(F)

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

pprint(simplify(diff(ksi1w,x)))
pprint(simplify(diff(ksi2w,x)))
pprint(simplify(diff(ksi3w,x)))
pprint(simplify(diff(ksi4w,x)))
pprint(simplify(diff(ksi5w,x)))
pprint(simplify(diff(ksi6w,x)))
pprint(simplify(diff(ksi7w,x)))
pprint(simplify(diff(ksi8w,x)))
#displacement matrix
n = zeros(6,12)

n[0,0] = L0
n[0,6] = L1
n[1,1] = ksi1v
n[1,4] = -ksi2v
n[1,7] = ksi3v
n[1,10] = -ksi4v
n[2,2] = ksi1w
n[2,3] = ksi2w
n[2,8] = ksi3w
n[2,9] = ksi4w
n[3,2] = ksi5w
n[3,3] = ksi6w
n[3,8] = ksi7w
n[3,9] = ksi8w
n[4,1] = -ksi5v
n[4,4] = ksi6v
n[4,7] = -ksi7v
n[4,10] = ksi8v
n[5,5] = L0
n[5,11] = L1

nd = n*d

#displacement
u = nd[0,0]
v = nd[1,0]
w = nd[2,0]
ty = nd[3,0]
tz = nd[4,0]
fi = nd[5,0]

#strain matrix
b = zeros(6,12)

b[0,0] = diff(L0,x)
b[0,6] = diff(L1,x)
b[1,1] = diff(ksi1v,x) + ksi5v
b[1,4] = -diff(ksi2v,x) - ksi6v
b[1,7] = diff(ksi3v,x) + ksi7v
b[1,10] = -diff(ksi4v,x) - ksi8v
b[2,2] = diff(ksi1w,x) + ksi5w
b[2,3] = diff(ksi2w,x) + ksi6w
b[2,8] = diff(ksi3w,x) + ksi7w
b[2,9] = diff(ksi4w,x) + ksi8w
b[3,2] = diff(ksi5w,x)
b[3,3] = diff(ksi6w,x)
b[3,8] = diff(ksi7w,x)
b[3,9] = diff(ksi8w,x)
b[4,1] = -diff(ksi5v,x)
b[4,4] = diff(ksi6v,x)
b[4,7] = -diff(ksi7v,x)
b[4,10] = diff(ksi8v,x)
b[5,5] = diff(L0,x)
b[5,11] = diff(L1,x)

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

pprint(k - k.T)
#'''
