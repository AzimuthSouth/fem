import numpy
class classicBeam:
    def setData(self, data):
        self.geom = data[0]; #beam length
        self.sect = data[1]; #beam stiffness matrix
        self.gm = data[2] #geometric characteristic

    def calc(self):
        K = self.sect
        l = self.geom[0]
        M = numpy.zeros((12,12))
        M[0,0] = K[0,0] / l
        M[0,3] = K[0,3] / l
        M[0,4] = -K[0,4] / l
        M[0,6] = -K[0,0] / l
        M[0,9] = -K[0,3] / l
        M[0,10] = K[0,4] / l

        M[1,1] = 12 * K[4,4] / l**3
        M[1,2] = 12 * K[3,4] / l**3
        M[1,3] = -6 * K[3,4] / l**2
        M[1,4] = 6 * K[4,4] / l**2
        M[1,7] = -12 * K[4,4] / l**3
        M[1,8] = -12 * K[3,4] / l**3
        M[1,9] = -6 * K[3,4] / l**2
        M[1,10] = 6 * K[4,4] / l**2

        M[2,1] = M[1,2]
        M[2,2] = 12 * K[3,3] / l**3
        M[2,3] = -6 * K[3,3] / l**2
        M[2,4] = 6 * K[3,4] / l**2
        M[2,7] = -12 * K[3,4] / l**3
        M[2,8] = -12 * K[3,3] / l**3
        M[2,9] = -6 * K[3,3] / l**2
        M[2,10] = 6 * K[3,4] / l**2

        M[3,0] =M[0,3]
        M[3,1] = M[1,3]
        M[3,2] = M[2,3]
        M[3,3] = 4 * K[3,3] / l
        M[3,4] = -4 * K[3,4] / l
        M[3,6] = -K[0,3] / l
        M[3,7] = 6 * K[3,4] / l**2
        M[3,8] = 6 * K[3,3] / l**2
        M[3,9] = 2 * K[3,3] / l
        M[3,10] = -2 * K[3,4] / l

        M[4,0] = M[0,4]
        M[4,1] = M[1,4]
        M[4,2] = M[2,4]
        M[4,3] = M[3,4]
        M[4,4] = 4 * K[4,4] / l
        M[4,6] = K[0,4] / l
        M[4,7] = -6 * K[4,4] / l**2
        M[4,8] = -6 * K[3,4] / l**2
        M[4,9] = -2 * K[3,4] / l
        M[4,10] = 2 * K[4,4] / l

        M[5,5] = K[5,5] / l
        M[5,11] = -K[5,5] / l

        M[6,0] = M[0,6]
        M[6,3] = M[3,6]
        M[6,4] = M[4,6]
        M[6,6] = K[0,0] / l
        M[6,9] = K[0,3] / l
        M[6,10] = -K[0,4] / l

        M[7,1] = M[1,7]
        M[7,2] = M[2,7]
        M[7,3] = M[3,7]
        M[7,4] = M[4,7]
        M[7,7] = 12 * K[4,4] / l**3
        M[7,8] = 12 * K[3,4] / l**3
        M[7,9] = 6 * K[3,4] / l**2
        M[7,10] = -6 * K[4,4] / l**2

        M[8,1] = M[1,8]
        M[8,2] = M[2,8]
        M[8,3] = M[3,8]
        M[8,4] = M[4,8]
        M[8,7] = M[7,8]
        M[8,8] = 12 * K[3,3] / l**3
        M[8,9] = 6 * K[3,3] / l**2
        M[8,10] = -6 * K[3,4] / l**2

        M[9,0] = M[0,9]
        M[9,1] = M[1,9]
        M[9,2] = M[2,9]
        M[9,3] = M[3,9]
        M[9,4] = M[4,9]
        M[9,6] = M[6,9]
        M[9,7] = M[7,9]
        M[9,8] = M[8,9]
        M[9,9] = 4 * K[3,3] / l
        M[9,10] = -4 * K[3,4] / l

        M[10,0] = M[0,10]
        M[10,1] = M[1,10]
        M[10,2] = M[2,10]
        M[10,3] = M[3,10]
        M[10,4] = M[4,10]
        M[10,6] = M[6,10]
        M[10,7] = M[7,10]
        M[10,8] = M[8,10]
        M[10,9] = M[9,10]
        M[10,10] = 4 * K[4,4] / l

        M[11,5] = -K[5,5] / l
        M[11,11] = K[5,5] / l
        self.K = M

    def getM(self):
        return self.K

    def L0(self, x):
        return 1 - x / self.geom[0]

    def L1(self, x):
        return x / self.geom[0]

    def N0(self, x):
        return 1 - 3 * (x / self.geom[0])**2 + 2 * (x / self.geom[0])**3

    def N1(self, x):
        return 3 * (x / self.geom[0])**2 - 2 * (x / self.geom[0])**3

    def F0(self, x):
        return x / (self.geom[0]**2) * (x - self.geom[0])**2

    def F1(self, x):
        return (x / self.geom[0])**2 * (x - self.geom[0])

    def dL0(self, x):
        return  -1.0 / self.geom[0]

    def dL1(self, x):
        return 1.0 / self.geom[0]
    
    def dN0(self,x):
        return - 6 * x / self.geom[0]**2 + 6 * x**2  / self.geom[0]**3

    def dN1(self,x):
        return 6 * x / self.geom[0]**2 - 6 * x**2 / self.geom[0]**3

    def dF0(self,x):
        return (x - self.geom[0])**2 / self.geom[0]**2 + 2 * x * (x - self.geom[0]) / self.geom[0]**2

    def dF1(self,x):
        return 2 * x * (x - self.geom[0]) / self.geom[0]**2 + (x / self.geom[0])**2

    def d2N0(self, x):
        return  6.0 * (-self.geom[0] + 2 * x) / self.geom[0]**3

    def d2N1(self, x):
        return -6.0 * (-self.geom[0] + 2 * x) / self.geom[0]**3

    def d2F0(self, x):
        return (6 * x - 4 * self.geom[0]) / self.geom[0]**2

    def d2F1(self, x):
        return (6 * x - 2 * self.geom[0]) / self.geom[0]**2

    def d3N0(self,x):
        return 12 / self.geom[0]**3

    def d3N1(self,x):
        return -12 / self.geom[0]**3

    def d3F0(self,x):
        return 6 / self.geom[0]**2

    def d3F1(self,x):
        return 6 / self.geom[0]**2

    def calcNB(self, x):
        n = numpy.zeros((6,12))
        #print 'in calc nb x=' + str(x)
        n[0,0] = self.L0(x)
        n[0,6] = self.L1(x)
        n[1,1] = self.N0(x)
        n[1,4] = self.F0(x)
        n[1,7] = self.N1(x)
        n[1,10] = self.F1(x)
        n[2,2] = self.N0(x)
        n[2,3] = -self.F0(x)
        n[2,8] = self.N1(x)
        n[2,9] = -self.F1(x)
        n[3,2] = self.dN0(x) 
        n[3,3] = -self.dF0(x)
        n[3,8] = self.dN1(x)
        n[3,9] = -self.dF1(x)
        n[4,1] = self.dN0(x)
        n[4,4] = self.dF0(x)
        n[4,7] = self.dN1(x)
        n[4,10] = self.dF1(x)
        n[5,5] = self.L0(x)
        n[5,11] = self.L1(x)

        self.N = numpy.matrix(n)

        b = numpy.zeros((4,12))

        b[0,0] = self.dL0(x)
        b[0,6] = self.dL1(x)
        b[1,2] = -self.d2N0(x)
        b[1,3] = self.d2F0(x)
        b[1,8] = -self.d2N1(x)
        b[1,9] = self.d2F1(x)
        b[2,1] = -self.d2N0(x)
        b[2,4] = -self.d2F0(x)
        b[2,7] = -self.d2N1(x)
        b[2,10] = -self.d2F1(x)
        b[3,5] = self.dL0(x)
        b[3,11] = self.dL1(x)

        self.B = numpy.matrix(b)

        bx = numpy.zeros((4,12))

        bx[1,2] = -self.d3N0(x)
        bx[1,3] = self.d3F0(x)
        bx[1,8] = -self.d3N1(x)
        bx[1,9] = self.d3F1(x)
        bx[2,1] = -self.d3N0(x)
        bx[2,4] = -self.d3F0(x)
        bx[2,7] = -self.d3N1(x)
        bx[2,10] = -self.d3F1(x)
        
        self.Bx = numpy.matrix(bx)

    def postproc(self,ui,x):
        head = '\t'.join(['{:>10}'.format (k) for k in ['X','UX','UY','UZ','RY','RZ','RX','epsX','kY','kZ','tetX','N','Qy','Qz','My','Mz','T', 'sx', 't1', 't2', 't3']]) + '\n'
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
