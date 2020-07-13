import numpy
class timoshenkoBeam:
	def setData(self, data):
		self.geom = data[0]; #beam length
		self.sect = data[1]; #beam stiffness matrix
		self.fiY = 12 * self.sect[3,3] / self.sect[2,2] / (self.geom[0])**2
		self.fiZ = 12 * self.sect[4,4] / self.sect[1,1] / (self.geom[0])**2
		self.gm = data[2] #geometric characteristic
		print "fiy={}, fiz={}".format(self.fiY, self.fiZ)


	def calc(self):
		K = self.sect;
		l = self.geom[0];
		#fiy = EIy / kGxzF / l**2
		fiy = self.fiY
		#fiz = EIz / kGxyF / l**2		
		fiz = self.fiZ
		M = numpy.zeros((12,12));
		M[0,0] = K[0,0] / l;
		M[0,3] = K[0,3] / l;
		M[0,4] = K[0,4] / l;
		M[0,6] = -K[0,0] / l;
		M[0,9] = -K[0,3] / l;
		M[0,10] = -K[0,4] / l;

		M[1,0] = M[0,1]		
		M[1,1] = 12 * K[4,4] / l**3 / (fiz + 1);
		M[1,2] = -12 * K[3,4] / l**3 / (fiy * fiz + fiy + fiz + 1);
		M[1,3] = 6 * K[3,4] / l**2 / (fiy * fiz + fiy + fiz + 1);
		M[1,4] = 6 * K[4,4] / l**2 / (fiz + 1)
		M[1,5] = K[1,5] * fiz / l / (fiz + 1)
		M[1,7] = -12 * K[4,4] / l**3 / (fiz + 1);
		M[1,8] = 12 * K[3,4] / l**3 / (fiy * fiz + fiy + fiz + 1);
		M[1,9] = 6 * K[3,4] / l**2 / (fiy * fiz + fiy + fiz + 1);
		M[1,10] = 6 * K[4,4] / l**2 / (fiz + 1);
		M[1,11] = -K[1,5] * fiz / l / (fiz + 1)
		
		M[2,0] = M[0,2]		
		M[2,1] = M[1,2];
		M[2,2] = 12 * K[3,3] / l**3 / (fiy + 1);
		M[2,3] = -6 * K[3,3] / l**2 / (fiy + 1);
		M[2,4] = -6 * K[3,4] / l**2 / (fiy * fiz + fiy + fiz + 1);
		M[2,5] = K[2,5] * fiy / l / (fiy + 1)
 		M[2,7] = 12 * K[3,4] / l**3 / (fiy * fiz + fiy + fiz + 1);
		M[2,8] = -12 * K[3,3] / l**3 / (fiy + 1);
		M[2,9] = -6 * K[3,3] / l**2 / (fiy + 1);
		M[2,10] = -6 * K[3,4] / l**2 / (fiy * fiz + fiy + fiz + 1);
		M[2,11] = -K[2,5] * fiy / l / (fiy + 1) 

		M[3,0] =M[0,3];
		M[3,1] = M[1,3];
		M[3,2] = M[2,3];
		M[3,3] = K[3,3] * (fiy + 4) / l / (fiy + 1);
		M[3,4] = K[3,4] * (fiy * fiz + fiy + fiz + 4) / l / (fiy * fiz + fiy + fiz + 1);
		M[3,5] = -K[2,5] * fiy / 2 / (fiy + 1)
		M[3,6] = -K[0,3] / l;
		M[3,7] = -6 * K[3,4] / l**2 / (fiy * fiz + fiy + fiz + 1);
		M[3,8] = 6 * K[3,3] / l**2 / (fiy + 1); 
		M[3,9] = K[3,3] * (2 - fiy)/ l / (fiy + 1); 
		M[3,10] = (fiy * fiz + fiy + fiz - 2) * K[3,4] / l / (fiy * fiz + fiy + fiz + 1);
		M[3,11] = K[0,3] * fiy / 2 / (fiy + 1)

		M[4,0] = M[0,4];
		M[4,1] = M[1,4];
		M[4,2] = M[2,4];
		M[4,3] = M[3,4];
		M[4,4] = (fiz + 4) * K[4,4] / l / (fiz + 1);
		M[4,5] = K[1,5] * fiz / 2 / (fiz + 1)
		M[4,6] = -K[0,4] / l; 
		M[4,7] = -6 * K[4,4] / l**2 / (fiz + 1);
		M[4,8] = 6 * K[3,4] / l**2 / (fiy * fiz + fiy + fiz + 1);
		M[4,9] = -(fiy * fiz + fiy + fiz - 2) * K[3,4] / l / (fiy * fiz + fiy + fiz + 1);
		M[4,10] = (2 - fiz) * K[4,4] / l / (fiz + 1);
		M[4,11] = -K[1,5] * fiz / 2 / (fiz + 1)


		M[5,0] = M[0,5]
		M[5,1] = M[1,5]
		M[5,2] = M[2,5]
		M[5,3] = M[3,5]
		M[5,4] = M[4,5]		
		M[5,5] = K[5,5] / l;
		M[5,7] = -K[1,5] * fiz / l / (fiz + 1)
		M[5,8] = -K[2,5] * fiy / l / (fiy + 1)
		M[5,9] = -K[2,5] * fiy / 2 / (fiy + 1)
		M[5,10] = K[1,5] * fiz / 2/ (fiz + 1)
		M[5,11] = -K[5,5] / l;

		M[6,0] = M[0,6];
		M[6,1] = M[1,6]
		M[6,2] = M[2,6]
		M[6,3] = M[3,6];
		M[6,4] = M[4,6];
		M[6,5] = M[5,6]
		M[6,6] = K[0,0] / l;
		M[6,9] = K[0,3] / l;
		M[6,10] = K[0,4] / l;

		M[7,0] = M[0,7]		
		M[7,1] = M[1,7];
		M[7,2] = M[2,7];
		M[7,3] = M[3,7];
		M[7,4] = M[4,7];
		M[7,5] = M[5,7]
		M[7,6] = M[6,7]
		M[7,7] = 12 * K[4,4] / l**3 / (fiz + 1);
		M[7,8] = -12 * K[3,4] / l**3 / (fiy * fiz + fiy + fiz + 1);
		M[7,9] = -6 * K[3,4] / l**2 / (fiy * fiz + fiy + fiz + 1);
		M[7,10] = -6 * K[4,4] / l**2 / (fiz + 1);
		M[7,11] = K[1,5] * fiz  / l / (fiz + 1)

		M[8,0] = M[0,8]		
		M[8,1] = M[1,8];
		M[8,2] = M[2,8];
		M[8,3] = M[3,8];
		M[8,4] = M[4,8];
		M[8,5] = M[5,8]
		M[8,6] = M[6,8]
 		M[8,7] = M[7,8];
		M[8,8] = 12 * K[3,3] / l**3 / (fiy + 1);
		M[8,9] = 6 * K[3,3] / l**2 / (fiy + 1);
		M[8,10] = 6 * K[3,4] / l**2 / (fiy * fiz + fiy + fiz + 1);
		M[8,11] = K[2,5] * fiy  / 2 / (fiy + 1)

		M[9,0] = M[0,9];
		M[9,1] = M[1,9];
		M[9,2] = M[2,9];
		M[9,3] = M[3,9];
		M[9,4] = M[4,9];
		M[9,5] = M[5,9]
		M[9,6] = M[6,9];
		M[9,7] = M[7,9];
		M[9,8] = M[8,9];
		M[9,9] = (fiy + 4) * K[3,3] / l / (fiy + 1);
		M[9,10] = (fiy * fiz + fiy + fiz + 4) * K[3,4] / l /(fiy * fiz + fiy + fiz + 1);
		M[9,11] = K[2,5] * fiy / 2 / (fiy + 1)

		M[10,0] = M[0,10];
		M[10,1] = M[1,10];
		M[10,2] = M[2,10];
		M[10,3] = M[3,10];
		M[10,4] = M[4,10];
		M[10,5] = M[5,10]
		M[10,6] = M[6,10];
		M[10,7] = M[7,10];
		M[10,8] = M[8,10];
		M[10,9] = M[9,10];
		M[10,10] = (fiz + 4) * K[4,4] / l / (fiz + 1);
		M[10,11] = -K[1,5] * fiz / 2 / (fiz + 1)

		M[11,0] = M[0,11];
		M[11,1] = M[1,11];
		M[11,2] = M[2,11];
		M[11,3] = M[3,11];
		M[11,4] = M[4,11];
		M[11,5] = M[5,11];
		M[11,6] = M[6,11];
		M[11,7] = M[7,11];
		M[11,8] = M[8,11];
		M[11,9] = M[9,11];
		M[11,10] = M[10,11]
		M[11,11] = K[5,5] / l;
		self.K = M;

	def getM(self):
		return self.K;

	def L0(self, x):
		return 1 - x / self.geom[0];

	def L1(self, x):
		return x / self.geom[0];

	def ksi1w(self,x):
		fiy = self.fiY
		l = self.geom[0]
		return 1 / (1 + fiy) * (2 * (x / l)**3 - 3 * (x / l)**2 - fiy * (x / l) + (1 + fiy))

	def ksi2w(self,x):
		fiy = self.fiY
		l = self.geom[0]
		return l / (1 + fiy) * (-(x / l)**3 + (4 + fiy) / 2 * (x /l)**2 - (2 + fiy) / 2 * (x / l))

	def ksi3w(self,x):
		fiy = self.fiY
		l = self.geom[0]
		return 1 / (1 + fiy) * (-2 * (x / l)**3 + 3 * (x / l)**2 + fiy * (x / l) )

	def ksi4w(self,x):
		fiy = self.fiY
		l = self.geom[0]
		return l / (1 + fiy) * (-(x / l)**3 + (2 - fiy) / 2 * (x /l)**2 + fiy / 2 * (x / l))

	def ksi5w(self,x):
		fiy = self.fiY
		l = self.geom[0]
		return 6 / l / (1 + fiy) * (x / l) * (1 - x / l)

	def ksi6w(self,x):
		fiy = self.fiY
		l = self.geom[0]
		return 1 / (1 + fiy) * ( 3 * (x / l)**2 - (4 + fiy) * (x / l) + (1 + fiy))

	def ksi7w(self,x):
		fiy = self.fiY
		l = self.geom[0]
		return  -6 / l / (1 + fiy) * (x / l) * (1 - x / l)

	def ksi8w(self,x):
		fiy = self.fiY
		l = self.geom[0]
		return 1 / (1 + fiy) * ( 3 * (x / l)**2 + (-2 + fiy) * (x / l))

	def ksi1v(self,x):
		fiz = self.fiZ
		l = self.geom[0]
		return 1 / (1 + fiz) * (2 * (x / l)**3 - 3 * (x / l)**2 - fiz * (x / l) + (1 + fiz))

	def ksi2v(self, x):
		fiz = self.fiZ
		l = self.geom[0]
		return l / (1 + fiz) * (-(x / l)**3 + (4 + fiz) / 2 * (x /l)**2 - (2 + fiz) / 2 * (x / l))

	def ksi3v(self, x):
		fiz = self.fiZ
		l = self.geom[0]
		return 1 / (1 + fiz) * (-2 * (x / l)**3 + 3 * (x / l)**2 + fiz * (x / l) )

	def ksi4v(self, x):
		fiz = self.fiZ
		l = self.geom[0]
		return l / (1 + fiz) * (-(x / l)**3 + (2 - fiz) / 2 * (x /l)**2 + fiz / 2 * (x / l))

	def ksi5v(self, x):
		fiz = self.fiZ
		l = self.geom[0]
		return 6 / l / (1 + fiz) * (x / l) * (1 - x / l)

	def ksi6v(self, x):
		fiz = self.fiZ
		l = self.geom[0]
		return 1 / (1 + fiz) * ( 3 * (x / l)**2 - (4 + fiz) * (x / l) + (1 + fiz))

	def ksi7v(self, x):
		fiz = self.fiZ
		l = self.geom[0]
		return -6 / l / (1 + fiz) * (x / l) * (1 - x / l)

	def ksi8v(self, x):
		fiz = self.fiZ
		l = self.geom[0]
		return 1 / (1 + fiz) * ( 3 * (x / l)**2 + (-2 + fiz) * (x / l))

	def dL0(self, x):
		return  -1.0 / self.geom[0];

	def dL1(self, x):
		return 1.0 / self.geom[0];

	def dksi1w(self, x):
		return (6 * x**2 - 6 * x * self.geom[0] - self.fiY * self.geom[0]**2) / (self.fiY + 1) / self.geom[0]**3
	
	def dksi2w(self, x):
		return (-3 * x**2 + self.geom[0] * x * (self.fiY + 4) - self.geom[0]**2 * (self.fiY + 2) / 2) / (self.fiY + 1) / self.geom[0]**2

	def dksi3w(self, x):
		return (-6 * x**2 + 6 * x * self.geom[0] + self.fiY * self.geom[0]**2) / (self.fiY + 1) / self.geom[0]**3

	def dksi4w(self, x):
		return (-3 * x**2 - self.geom[0] * x * (self.fiY - 2) + self.geom[0]**2 * self.fiY / 2) / (self.fiY + 1) / self.geom[0]**2

	def dksi5w(self, x):
		return 6 * (self.geom[0] - 2 * x) / (self.fiY + 1) / self.geom[0]**3

	def dksi6w(self, x):
		return (6 * x - self.geom[0]* (self.fiY + 4)) / (self.fiY + 1) / self.geom[0]**2

	def dksi7w(self, x):
		return 6 * (-self.geom[0] + 2 * x) / (self.fiY + 1) / self.geom[0]**3

	def dksi8w(self, x):
		return (6 * x + self.geom[0]* (self.fiY - 2)) / (self.fiY + 1) / self.geom[0]**2

	def dksi1v(self, x):
		return (6 * x**2 - 6 * x * self.geom[0] - self.fiZ * self.geom[0]**2) / (self.fiZ + 1) / self.geom[0]**3
	
	def dksi2v(self, x):
		return (-3 * x**2 + self.geom[0] * x * (self.fiZ + 4) - self.geom[0]**2 * (self.fiZ + 2) / 2) / (self.fiZ + 1) / self.geom[0]**2

	def dksi3v(self, x):
		return (-6 * x**2 + 6 * x * self.geom[0] + self.fiZ * self.geom[0]**2) / (self.fiZ + 1) / self.geom[0]**3

	def dksi4v(self, x):
		return (-3 * x**2 - self.geom[0] * x * (self.fiZ - 2) + self.geom[0]**2 * self.fiZ / 2) / (self.fiZ + 1) / self.geom[0]**2

	def dksi5v(self, x):
		return 6 * (self.geom[0] - 2 * x) / (self.fiZ + 1) / self.geom[0]**3

	def dksi6v(self, x):
		return (6 * x - self.geom[0]* (self.fiZ + 4)) / (self.fiZ + 1) / self.geom[0]**2

	def dksi7v(self, x):
		return 6 * (-self.geom[0] + 2 * x) / (self.fiZ + 1) / self.geom[0]**3

	def dksi8v(self, x):
		return (6 * x + self.geom[0]* (self.fiZ - 2)) / (self.fiZ + 1) / self.geom[0]**2

	def calcNB(self, x):
		n = numpy.zeros((6,12))
		#print 'in calc nb x=' + str(x)
		n[0,0] = self.L0(x)
		n[0,6] = self.L1(x)
		n[1,1] = self.ksi1v(x)
		n[1,4] = -self.ksi2v(x)
		n[1,7] = self.ksi3v(x)
		n[1,10] = -self.ksi4v(x)
		n[2,2] = self.ksi1w(x)
		n[2,3] = self.ksi2w(x)
		n[2,8] = self.ksi3w(x)
		n[2,9] = self.ksi4w(x)
		n[3,2] = self.ksi5w(x)
		n[3,3] = self.ksi6w(x)
		n[3,8] = self.ksi7w(x)
		n[3,9] = self.ksi8w(x)
		n[4,1] = -self.ksi5v(x)
		n[4,4] = self.ksi6v(x)
		n[4,7] = -self.ksi7v(x)
		n[4,10] = self.ksi8v(x)
		n[5,5] = self.L0(x)
		n[5,11] = self.L1(x)
		
		self.N = numpy.matrix(n);

		b = numpy.zeros((6,12))

		b[0,0] = self.dL0(x)
		b[0,6] = self.dL1(x)
		b[1,1] = -(-self.dksi1v(x) - self.ksi5v(x))
		b[1,4] = -(self.dksi2v(x) + self.ksi6v(x))
		b[1,7] = -(-self.dksi3v(x) - self.ksi7v(x))
		b[1,10] = -(self.dksi4v(x) + self.ksi8v(x))
		b[2,2] = self.dksi1w(x) + self.ksi5w(x)
		b[2,3] = self.dksi2w(x) + self.ksi6w(x)
		b[2,8] = self.dksi3w(x) + self.ksi7w(x)
		b[2,9] = self.dksi4w(x) + self.ksi8w(x)
		b[3,2] = self.dksi5w(x)
		b[3,3] = self.dksi6w(x)
		b[3,8] = self.dksi7w(x)
		b[3,9] = self.dksi8w(x)
		b[4,1] = self.dksi5v(x)
		b[4,4] = -self.dksi6v(x)
		b[4,7] = self.dksi7v(x)
		b[4,10] = -self.dksi8v(x)
		b[5,5] = self.dL0(x)
		b[5,11] = self.dL1(x)

		self.B = numpy.matrix(b)

	def postproc(self,ui,x):
		hd = ['X','UX','UY','UZ','RY','RZ','RX','epsX','gamaXY','gamaXZ','kY','kZ','tetX','N','Qy','Qz','My','Mz','T', 'sx', 't1', 't2', 't3']
		head = '\t'.join(['{:>10}'.format (k) for k in hd]) + '\n'
		self.calcNB(x)
		print "B={}".format(self.N)
		u = numpy.ravel(self.N * ui).T
		eps = numpy.ravel(self.B * ui).T
		sct = self.sect[:6,:6]
		#print "sect = " + str(sct)
		frs = numpy.ravel(sct * self.B * ui).T
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

	

