'''
stifness characteristic of section is matrix
[EF 0   0   Esz Esy 0   0]
[0  GxyF    0   0   0   -Gsy    0]
[0  0   GxzF    0   0   GSz 0]
[Esz    0   0   EIy EIr 0   0]
[Esy    0   0   EIr EIz 0   0]
[0  -GSy    GSz 0   0   EIk 0]
[0  0   0   0   0   0   EIw]

geometric characteristic of section is vector
[F, Iy, Iz, Ik, Wy, Wz, Wk]
'''
import numpy
class Section(object):
    def set_data(self, data):
        self.geom = data[0]
        self.mat = data[1]
        #print str(data[1][0,0])

    def calc_stiffness(self):
        E = 1.0 / self.mat[0,0]
        G = 1.0 / self.mat[2,2]
        self.K = numpy.matrix([ [1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0], 
                    [0.0, 1.0, 0.0, 0.0, 0.0, -1.0, 0.0], 
                    [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0], 
                    [1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0],
                    [1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0],
                    [0.0, -1.0, 1.0, 0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])
        #print self.K.shape
    def calc_geom(self):
        self.G = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    def get_k(self):
        return self.K

    def get_g(self):
        return self.G

class Circle(Section):
    def calc_stiffness(self):
        r = self.geom[0]
        F = numpy.pi * r**2
        I = numpy.pi * r**4 / 4
        Ip = numpy.pi * r**4 / 2
        E = 1.0 / self.mat[0,0]
        G = 1.0 / self.mat[2,2]
        #print "G={}".format(G)
        self.K = numpy.matrix([ [E * F,   0.0,   0.0,   0.0,   0.0,    0.0,    0.0],
                    [  0.0, G * F,   0.0,   0.0,   0.0,    0.0,    0.0],
                    [  0.0,   0.0, G * F,   0.0,   0.0,    0.0,    0.0],
                    [  0.0,   0.0,   0.0, E * I,   0.0,    0.0,    0.0], 
                    [  0.0,   0.0,   0.0,   0.0, E * I,    0.0,    0.0], 
                    [  0.0,   0.0,   0.0,   0.0,   0.0, G * Ip,    0.0],
                    [  0.0,   0.0,   0.0,   0.0,   0.0,    0.0, E * Ip]])

    def calc_geom(self):
        r = self.geom[0]
        F = numpy.pi * r**2
        I = numpy.pi * r**4 / 4
        Ip = numpy.pi * r**4 / 2
        W = I / r
        Wp = Ip / r
        S = r**2 / 4
        self.G = [F, I, I, Ip, W, W, Wp, S, S]

class Rectangle(Section):
    def calc_stiffness(self):
        [b, h] = self.geom
        #print "b={}, h={}".format(b,h)
        F = b * h
        Iy = b * h**3 / 12
        Iz = h * b**3 / 12
        x = h / b
        if (x < 1):
            x = 1.0 /x
            (b, h) = (h, b)     
        [a1, b1, c1] = self.calc_abc(x)     
        Ik = b1 * h * b**3
        E = 1.0 / self.mat[0,0]
        G = 1.0 / self.mat[2,2]
        self.K = numpy.matrix([ [E * F,   0.0,   0.0,   0.0,   0.0,    0.0,    0.0],    #ex
                    [  0.0, G * F,   0.0,   0.0,   0.0,    0.0,    0.0],    #gamaXY 
                    [  0.0,   0.0, G * F,   0.0,   0.0,    0.0,    0.0],    #gamaXZ
                    [  0.0,   0.0,   0.0, E * Iy,   0.0,    0.0,    0.0],   #kapaY
                    [  0.0,   0.0,   0.0,   0.0, E * Iz,    0.0,    0.0],   #kapaZ
                    [  0.0,   0.0,   0.0,   0.0,   0.0, G * Ik,    0.0],    #khi
                    [  0.0,   0.0,   0.0,   0.0,   0.0,    0.0, E * Ik]]);  #dkhi

    def calc_geom(self):
        [b, h] = self.geom
        F = b * h
        I1 = b * h**3 / 12
        I2 = h * b**3 / 12
        W1 = b * h**2 / 6
        W2 = h * b**2 / 6
        S1 = h**2 / 8
        S2 = b**2 / 8
        x = h / b
        if (x < 1):
            x = 1.0 /x
            (b, h) = (h, b)     
        [a1, b1, c1] = self.calc_abc(x)     
        Ik = b1 * h * b**3
        Wk = a1 * h * b**2
        #print "Ik={}, Wk={}".format(Ik,Wk)
        self.G = [F, I1, I2, Ik, W1, W2, Wk, S1, S2]

    def calc_abc(self, x):
        T = numpy.matrix([  [  1.0,   1.2,  1.25,   1.5,  1.75,   2.0,   2.5,   3.0,   4.0,   5.0,   6.0,   8.0,  10.0,  10.1],
            [0.208, 0.219, 0.221, 0.231, 0.239, 0.246, 0.258, 0.267, 0.282, 0.291, 0.299, 0.307, 0.312, 0.333],
            [0.141, 0.166, 0.172, 0.196, 0.214, 0.229, 0.249, 0.263, 0.281, 0.291, 0.299, 0.307, 0.312, 0.333],
            [  1.0,  0.93,  0.91,  0.86,  0.82,  0.79,  0.77,  0.75,  0.74,  0.74,  0.74,  0.74,  0.74,  0.74]])
        for i in range(T.shape[1]):
            if (x <= T[0,i]):
                a = (T[1, i] - T[1, i - 1]) / (T[0, i] - T[0, i - 1]) * (x - T[0, i - 1]) + T[1, i - 1]
                b = (T[2, i] - T[2, i - 1]) / (T[0, i] - T[0, i - 1]) * (x - T[0, i - 1]) + T[2, i - 1]
                c = (T[3, i] - T[3, i - 1]) / (T[0, i] - T[0, i - 1]) * (x - T[0, i - 1]) + T[3, i - 1]
                return [a , b, c]
        return [T[1,T.shape[1] - 1], T[2,T.shape[1] - 1], T[3,T.shape[1] - 1]]


class TwoTavr(Section):
    def calc_stiffness(self):
        #for symmetric twotavr section
        [w, h, d, t] = self.geom
        F = 2 * d * h + (w - 2 * d) * t
        Iy = d * h**3 / 6 + (w - 2 * d) * t**3 / 12
        Iz = h / 3 * (w**3 / 4 - 2 *(w / 2 - d)**3) + 2 * t / 3 * (w / 2 -  d)**3
        Ip = Iy + Iz
        Ip = 2 * h * d**3 / 3 + (w - 2 * d) * t**3 / 3
        Iw = h**3 * (w - d)**2 * d / 24
        #print 'Iw=' + str(Iw)
        #print 'Ik=' + str(Ip)
        E = 1.0 / self.mat[0,0]
        G = 1.0 / self.mat[2,2]
        self.K = numpy.matrix([ [E * F,   0.0,   0.0,   0.0,   0.0,    0.0,    0.0],
                    [  0.0, G * F,   0.0,   0.0,   0.0,    0.0,    0.0],
                    [  0.0,   0.0, G * F,   0.0,   0.0,    0.0,    0.0],
                    [  0.0,   0.0,   0.0, E * I,   0.0,    0.0,    0.0], 
                    [  0.0,   0.0,   0.0,   0.0, E * I,    0.0,    0.0], 
                    [  0.0,   0.0,   0.0,   0.0,   0.0, G * Ip,    0.0],
                    [  0.0,   0.0,   0.0,   0.0,   0.0,    0.0, E * Iw]])

