import numpy
class classicWarp:
    def setData(self, data):
        self.geom = data[0]; #beam length
        self.sect = data[1]; #beam stiffness matrix
        self.gm = data[2] #geometric characteristic

    def calc(self):
        K = self.sect
        l = self.geom[0]
        M = numpy.zeros((14,14))
        M[0,0] = K[0,0] / l
        M[0,3] = K[0,3] / l
        M[0,4] = -K[0,4] / l
        M[0,6] = K[0,6] / l
        M[0,7] = -K[0,0] / l
        M[0,10] = -K[0,3] / l
        M[0,11] = K[0,4] / l
        M[0,13] = -K[0,6] / l

        M[1,1] = 12 * K[4,4] / l**3
        M[1,2] = 12 * K[3,4] / l**3
        M[1,3] = -6 * K[3,4] / l**2
        M[1,4] = 6 * K[4,4] / l**2
        M[1,5] = -12 * K[4,6] / l**3
        M[1,6] = -6 * K[4,6] / l**2
        M[1,8] = -12 * K[4,4] / l**3
        M[1,9] = -12 * K[3,4] / l**3
        M[1,10] = -6 * K[3,4] / l**2
        M[1,11] = 6 * K[4,4] / l**2
        M[1,12] = 12 * K[4,6] / l**3
        M[1,13] = -6 * K[4,6] / l**2

        M[2,1] = M[1,2]
        M[2,2] = 12 * K[3,3] / l**3
        M[2,3] = -6 * K[3,3] / l**2
        M[2,4] = 6 * K[3,4] / l**2
        M[2,5] = -12 * K[3,6] / l**3
        M[2,6] = -6 * K[3,6] / l**2
        M[2,8] = -12 * K[3,4] / l**3
        M[2,9] = -12 * K[3,3] / l**3
        M[2,10] = -6 * K[3,3] / l**2
        M[2,11] = 6 * K[3,4] / l**2
        M[3,12] = 12 * K[3,6] / l**3
        M[3,13] = -6 * K[3,6] / l**2

        M[3,0] =M[0,3]
        M[3,1] = M[1,3]
        M[3,2] = M[2,3]
        M[3,3] = 4 * K[3,3] / l
        M[3,4] = -4 * K[3,4] / l
        M[3,5] = 6 * K[3,6] / l**2
        M[3,6] = 4 * K[3,6] / l
        M[3,7] = -K[0,3] / l
        M[3,8] = 6 * K[3,4] / l**2
        M[3,9] = 6 * K[3,3] / l**2
        M[3,10] = 2 * K[3,3] / l
        M[3,11] = -2 * K[3,4] / l
        M[3,12] = -6 * K[3,6] / l**2
        M[3,13] = 2 * K[3,6] / l

        M[4,0] = M[0,4]
        M[4,1] = M[1,4]
        M[4,2] = M[2,4]
        M[4,3] = M[3,4]
        M[4,4] = 4 * K[4,4] / l
        M[4,5] = -6 * K[4,6] / l**2
        M[4,6] = -4 * K[4,6] / l
        M[4,7] = K[0,4] / l
        M[4,8] = -6 * K[4,4] / l**2
        M[4,9] = -6 * K[3,4] / l**2
        M[4,10] = -2 * K[3,4] / l
        M[4,11] = 2 * K[4,4] / l
        M[4,12] = 6 * K[4,6] / l**2
        M[4,13] = -2 * K[4,6] / l

        M[5,0] = M[0,5]
        M[5,1] = M[1,5]
        M[5,2] = M[2,5]
        M[5,3] = M[3,5]
        M[5,4] = M[4,5]
        M[5,5] = 6 * K[5,5] / 5 / l + 12 * K[6,6] / l**3
        M[5,6] = K[5,5] / 10 + 6 * K[6,6] / l**2
        M[5,8] = 12 * K[4,6] / l**3
        M[5,9] = 12 * K[3,6] / l**3
        M[5,10] = 6 * K[3,6] / l**2
        M[5,11] = -6 * K[4,6] / l**2
        M[5,12] = -6 * K[5,5] / 5 / l - 12 * K[6,6] / l**3
        M[5,13] = K[5,5] / 10 + 6 * K[6,6] / l**2

        M[6,0] = M[0,6]
        M[6,1] = M[1,6]
        M[6,2] = M[2,6]
        M[6,3] = M[3,6]
        M[6,4] = M[4,6]
        M[6,5] = M[5,6]
        M[6,6] = 2 * K[5,5] * l / 15 + 4 * K[6,6] / l
        M[6,7] = -K[0,6] / l
        M[6,8] = 6 * K[4,6] / l**2
        M[6,9] = 6 * K[3,6] / l**2
        M[6,10] = 2 * K[3,6] / l
        M[6,11] = -2 * K[4,6] / l
        M[6,12] = -K[5,5] / 10 -6 * K[6,6] / l**2
        M[6,13] = -K[5,5] * l / 30 + 2 * K[6,6] / l

        M[7,0] = M[0,7]
        M[7,1] = M[1,7]
        M[7,2] = M[2,7]
        M[7,3] = M[3,7]
        M[7,4] = M[4,7]
        M[7,5] = M[5,7]
        M[7,6] = M[6,7]        
        M[7,7] = K[0,0] / l
        M[7,10] = K[0,3] / l
        M[7,11] = -K[0,4] / l
        M[7,13] = K[0,6] / l

        M[8,0] = M[0,8]
        M[8,1] = M[1,8]
        M[8,2] = M[2,8]
        M[8,3] = M[3,8]
        M[8,4] = M[4,8]
        M[8,5] = M[5,8]
        M[8,6] = M[6,8]
        M[8,7] = M[7,8]
        M[8,8] = 12 * K[4,4] / l**3
        M[8,9] = 12 * K[3,4] / l**3
        M[8,10] = 6 * K[3,4] / l**2
        M[8,11] = -6 * K[4,4] / l**2
        M[8,12] = -12 * K[4,6] / l**3
        M[8,13] = 6 * K[4,6] / l**2

        M[9,0] = M[0,9]
        M[9,1] = M[1,9]
        M[9,2] = M[2,9]
        M[9,3] = M[3,9]
        M[9,4] = M[4,9]
        M[9,5] = M[5,9]
        M[9,6] = M[6,9]
        M[9,7] = M[7,9]
        M[9,8] = M[8,9]
        M[9,9] = 12 * K[3,3] / l**3
        M[9,10] = 6 * K[3,3] / l**2
        M[9,11] = -6 * K[3,4] / l**2
        M[9,12] = -12 * K[3,6] / l**3
        M[9,13] = 6 * K[3,6] / l**2

        M[10,0] = M[0,10]
        M[10,1] = M[1,10]
        M[10,2] = M[2,10]
        M[10,3] = M[3,10]
        M[10,4] = M[4,10]
        M[10,5] = M[5,10]
        M[10,6] = M[6,10]
        M[10,7] = M[7,10]
        M[10,8] = M[8,10]
        M[10,9] = M[9,10]
        M[10,10] = 4 * K[3,3] / l
        M[10,11] = -4 * K[3,4] / l
        M[10,12] = -6 * K[3,6] / l**2
        M[10,13] = 4 * K[3,6] / l

        M[11,0] = M[0,11]
        M[11,1] = M[1,11]
        M[11,2] = M[2,11]
        M[11,3] = M[3,11]
        M[11,4] = M[4,11]
        M[11,5] = M[5,11]
        M[11,6] = M[6,11]
        M[11,7] = M[7,11]
        M[11,8] = M[8,11]
        M[11,9] = M[9,11]
        M[11,10] = M[10,11]
        M[11,11] = 4 * K[4,4] / l
        M[11,12] = 6 * K[4,6] / l**2
        M[11,13] = -4 * K[4,6] / l

        M[12,0] = M[0,12]
        M[12,1] = M[1,12]
        M[12,2] = M[2,12]
        M[12,3] = M[3,12]
        M[12,4] = M[4,12]
        M[12,5] = M[5,12]
        M[12,6] = M[6,12]
        M[12,7] = M[7,12]
        M[12,8] = M[8,12]
        M[12,9] = M[9,12]
        M[12,10] = M[10,12]
        M[12,11] = M[11,12]
        M[12,12] = 6 * K[5,5] / 5 / l + 12 * K[6,6] / l**3
        M[12,13] = -K[5,5] / 10 - 6 * K[6,6] * l**2

        M[13,0] = M[0,13]
        M[13,1] = M[1,13]
        M[13,2] = M[2,13]
        M[13,3] = M[3,13]
        M[13,4] = M[4,13]
        M[13,5] = M[5,13]
        M[13,6] = M[6,13]
        M[13,7] = M[7,13]
        M[13,8] = M[8,13]
        M[13,9] = M[9,13]
        M[13,10] = M[10,13]
        M[13,11] = M[11,13]
        M[13,12] = M[12,13]
        M[13,13] = 2 * K[5,5] * l / 15 + 4 * K[6,6] / l
  
        self.K = M

    def getM(self):
        return self.K

    def L0(self, x):
        return 1 - x / self.geom[0]

    def L1(self, x):
        return x / self.geom[0]

    def ksi1(self, x):
        return 1 - 3 * (x / self.geom[0])**2 + 2 * (x / self.geom[0])**3
    
    def ksi2(self, x):
        return -x / (self.geom[0]**2) * (x - self.geom[0])**2

    def ksi3(self, x):
        return 3 * (x / self.geom[0])**2 - 2 * (x / self.geom[0])**3

    def ksi4(self, x):
        return (x / self.geom[0])**2 * (self.geom[0] - x)
 
    def N1(self, x):
        return (1 - x / self.geom[0])**2 * (1 + 2 * x / self.geom[0])

    def N2(self, x):
        return x * (1 - x / self.geom[0])**2

    def N3(self, x):
        return (x / self.geom[0])**2 * (3 - 2 * x / self.geom[0])

    def N4(self, x):
        return x**2 / self.geom[0] * (x / self.geom[0] - 1)

    def dL0(self, x):
        return  -1.0 / self.geom[0]

    def dL1(self, x):
        return 1.0 / self.geom[0]
    
    def dksi1(self, x):
        return - 6 * x / self.geom[0]**2 + 6 * x**2  / self.geom[0]**3

    def dksi2(self, x):
        return -3 * (x / self.geom[0])**2 + 4 * (x / self.geom[0]) - 1

    def dksi3(self, x):
        return 6 * x / (self.geom[0]**2) * (1 - x / self.geom[0])

    def dksi4(self,x):
        return -3 * (x / self.geom[0])**2 + 2 * x / self.geom[0]

    def dN1(self, x):
        return 6 * x / (self.geom[0])**2 * (x / self.geom[0] - 1)

    def dN2(self, x):
        return 3 * (x / self.geom[0])**2 - 4 * (x / self.geom[0]) + 1

    def dN3(self, x):
        return 6 * x / (self.geom[0])**2 * (1 - x / self.geom[0])
    
    def dN4(self, x):
        return 3 * (x / self.geom[0])**2 - 2 * (x / self.geom[0])

    def d2N1(self, x):
        return 12 * x / (self.geom[0])**3 - 6 / (self.geom[0])**2

    def d2N2(self, x):
        return 6 * x / (self.geom[0])**2 - 4 / self.geom[0]

    def d2N3(self, x):
        return 6 / (self.geom[0])**2 - 12 * x / (self.geom[0])**3

    def d2N4(self, x):
        return 6 * x / (self.geom[0])**2 - 2 / self.geom[0]

    def d3N1(self, x):
        return 12 / (self.geom[0])**3

    def d3N2(self, x):
        return 6 / (self.geom[0])**2

    def d3N3(self, x):
        return -12 / (self.geom[0])**3

    def d3N4(self, x):
        return 6 / (self.geom[0])**2

    def d2ksi1(self, x):
        return 6.0 * (-self.geom[0] + 2 * x) / self.geom[0]**3

    def d2ksi2(self, x):
        return (-6 * x + 4 * self.geom[0]) / self.geom[0]**2

    def d2ksi3(self, x):
        return 6.0 * (self.geom[0] - 2 * x) / self.geom[0]**3

    def d2ksi4(self, x):
        return (-6 * x + 2 * self.geom[0]) / self.geom[0]**2
    
    def d3ksi1(self, x):
        return 12 / self.geom[0]**3

    def d3ksi2(self, x):
        return -6 / self.geom[0]**2

    def d3ksi3(self, x):
        return -12 / self.geom[0]**3

    def d3ksi4(self, x):
        return -6 / self.geom[0]**2

    def calcNB(self, x):
        n = numpy.zeros((7,14))
        #print 'in calc nb x=' + str(x)
        n[0,0] = self.L0(x)
        n[0,7] = self.L1(x)
        n[1,1] = self.ksi1(x)
        n[1,4] = -self.ksi2(x)
        n[1,8] = self.ksi3(x)
        n[1,11] = -self.ksi4(x)
        n[2,2] = self.ksi1(x)
        n[2,3] = self.ksi2(x)
        n[2,9] = self.ksi3(x)
        n[2,10] = self.ksi4(x)
        n[3,2] = -self.dksi1(x) 
        n[3,3] = -self.dksi2(x)
        n[3,9] = -self.dksi3(x)
        n[3,10] = -self.dksi4(x)
        n[4,1] = self.dksi1(x)
        n[4,4] = -self.dksi2(x)
        n[4,8] = self.dksi3(x)
        n[4,11] = -self.dksi4(x)
        n[5,5] = self.N1(x)
        n[5,6] = self.N2(x)
        n[5,12] = self.N3(x)
        n[5,13] = self.N4(x)
        n[6,5] = self.dN1(x)
        n[6,6] = self.dN2(x)
        n[6,12] = self.dN3(x)
        n[6,13] = self.dN4(x)

        self.N = numpy.matrix(n)

        b = numpy.zeros((5,14))

        b[0,0] = self.dL0(x)
        b[0,7] = self.dL1(x)
        b[1,1] = -self.d2ksi1(x)
        b[1,4] = self.d2ksi2(x)
        b[1,8] = -self.d2ksi3(x)
        b[1,11] = self.d2ksi4(x)
        b[2,2] = -self.d2ksi1(x)
        b[2,3] = -self.d2ksi2(x)
        b[2,9] = -self.d2ksi3(x)
        b[2,10] = -self.d2ksi4(x)
        b[3,5] = self.dN1(x)
        b[3,6] = self.dN2(x)
        b[3,12] = self.dN3(x)
        b[3,13] = self.dN4(x)
        b[4,5] = self.d2N1(x)
        b[4,6] = self.d2N2(x)
        b[4,12] = self.d2N3(x)
        b[4,13] = self.d2N4(x)

        self.B = numpy.matrix(b)

        bx = numpy.zeros((5,14))

        bx[1,1] = -self.d3ksi1(x)
        bx[1,4] = self.d3ksi2(x)
        bx[1,8] = -self.d3ksi3(x)
        bx[1,11] = self.d3ksi4(x)
        bx[2,2] = -self.d3ksi1(x)
        bx[2,3] = -self.d3ksi2(x)
        bx[2,9] = -self.d3ksi3(x)
        bx[2,10] = -self.d3ksi4(x)
        bx[3,5] = self.d2N1(x)
        bx[3,6] = self.d2N2(x)
        bx[3,12] = self.d2N3(x)
        bx[3,13] = self.d2N4(x)
        bx[4,5] = self.d3N1(x)
        bx[4,6] = self.d3N2(x)
        bx[4,12] = self.d3N3(x)
        bx[4,13] = self.d3N4(x)

        self.Bx = numpy.matrix(bx)

    def postproc(self,ui,x):
        head = '\t'.join(['{:>10}'.format (k) for k in ['X','UX','UY','UZ','RY','RZ','RX','epsX','kY','kZ','tetX','tetXX','N','Qy','Qz','My','Mz','T','Mw', 'sx', 't1', 't2', 't3']]) + '\n'
        self.calcNB(x)
        #print "ui={}".format(ui)
        #print "N={}".format(self.N)
        u = numpy.ravel(self.N * ui).T
        eps = numpy.ravel(self.B * ui).T
        sct = self.sect[[0,3,4,5],:][:,[0,3,4,5]]
        #print "sect = " + str(sct)
        f = numpy.ravel(sct * self.B * ui).T
        f1 = numpy.ravel(sct * self.Bx * ui).T
        frs = [f[0], f1[2], f1[1], f[1], f[2], f[3]]
        sig = self.beam_tool(frs)
        return [head,u,eps,frs,sig]

    def beam_tool(self,frs):
        #N, Qy, Qz, My, Mz, T   
        #F, Iy, Iz, Ik, Wy, Wz, Wk, S1, S2
        sx = abs(frs[0] / self.gm[0]) + abs(frs[3] / self.gm[4]) + abs(frs[4] / self.gm[5])
        txy = frs[1] * self.gm[7] / self.gm[1]
        txz = frs[2] * self.gm[8] / self.gm[2]
        txf = frs[5] / self.gm[6] 
        return [sx, txy, txz, txf]
