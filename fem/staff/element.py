import numpy
from fem.beams import classicBeam
from fem.beams import timoshenkoBeam
class element:
	def setData(self, data):
		self.KU = data[0] 		#node count for element
		self.KSS = data[1] 	#degree of freedom count
		self.ND = data[2] 		#node numbers
		self.param = data[3] 	#length and stiffness
		self.dsp = []
		self.eps = []
		self.frs = []
		self.xyz = []
		self.hd = []
		self.sig = []

	def calc(self):
		#import classicWarp1;
		#self.cb = classicWarp1.classicWarp();
		self.cb = timoshenkoBeam.timoshenkoBeam()
		#self.cb = classicBeam.classicBeam()		
		self.cb.setData(self.param)
		self.cb.calc()
		self.K = self.cb.getM()

	def getK(self):
		return self.K

	def postproc(self, u, x, x0):
		self.xyz.append(x0 + x)
		#displacements
		#print 'n=' + str(self.cb.B)
		#print 'Bx*u=' + str(self.cb.sect * self.cb.Bx * u)
		[h,d,e,f,s] = self.cb.postproc(u,x)
		self.hd.append(h)
		self.dsp.append(d)
		#print 'dsp=' + str((self.cb.N * u).T)
		#strain
		self.eps.append(e)
		#print 'eps=' + str((self.cb.B * u).T)
		#print 'eps=' + str(self.eps)
		#forces
		#calc [N, My, Mz, T] and [dN, dMy = Qz, dMz = Qy, dT]
		self.frs.append(f)
		self.sig.append(s)
		#print 'frc=' + str((self.cb.sect * self.cb.B * u).T)
		#print 'frc={}'.format(self.frs)
	
