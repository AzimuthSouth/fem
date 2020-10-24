import numpy
        
class elastic:
    def setData(self, data):
        self.mat = data
        
    def calc(self):
        E = self.mat[0]
        nu = self.mat[1]
        G = self.mat[2]
        self.a = numpy.matrix([[1.0/E, -nu/E, 0.0],[-nu/E, 1.0/E, 0.0],[0.0, 0.0, 1.0/G]])
        
    def get_a(self):
        return self.a

    def get_E(self):
        return self.mat[0]

    def get_G(self):
        return self.mat[2]

    def get_nu(self):
        return self.mat[1]
