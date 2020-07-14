import math
import numpy
import sys

from fem.mat import elastic
from fem.beams import section
from fem.staff import element
from fem.staff import va
                
class model:
    def setData(self, data):
        self.nds = data[0]
        self.top = data[1]
        self.R = data[2]
        self.NG = data[3]
        self.kss = len(self.R[0])

    def calcElems(self):
        e = elastic.elastic()
        #e.setData([75.0e9, 0.3, 28.80e9])
        e.setData([2.0e5, 0.3, 7.69e4])
        e.calc()
        #s = section.Circle();
        s = section.Rectangle()
        #s = section.TwoTavr();
        #r = (10.0 / math.pi)**0.5
        #s.set_data([[r], e.get_a()]); #for circle section
        #s.set_data([[0.5, 0.16, 0.02, 0.014], e.get_a()])
        s.set_data([[10.0, 1.0], e.get_a()])        
        s.calc_stiffness()
        s.calc_geom()
        self.elm = []
        for i in range(len(self.top)):
            #node numbers
            n1 = self.top[i][0]
            n2 = self.top[i][1]
            #elem length
            l = va.dist(self.nds[n1], self.nds[n2])
            ei = element.element()
            ei.setData([2, self.kss, [n1, n2], [[l], s.get_k(), s.get_g()]])
            ei.calc()
            self.elm.append(ei)

    def checkEl(self):
        #print 'ke= '+ str(len(self.elm))
        #for i in range(len(self.elm)):
            #print str(self.elm[i].getK())
            #print;
            pass

    def grossMatrix(self):
        ku = len(self.nds)
        kss = self.kss
        numpy.set_printoptions(precision=3,threshold=sys.maxsize);
        MM = numpy.zeros((ku * kss, ku * kss));
        M = numpy.matrix(MM)
        for i in range(len(self.elm)):
            #self.elm[i].getK() - matrix [KU*KSS,KU*KSS]
            eKU = self.elm[i].KU
            eKSS = self.elm[i].KSS
            for j in range(eKU):
                for k in range(eKU):
                    for p in range(eKSS):
                        for q in range(eKSS):
                            M[self.elm[i].ND[j] * kss + p, self.elm[i].ND[k] * kss + q] += self.elm[i].getK()[p + eKSS * j,q + eKSS * k]
        self.K = M

        f = open('gross.txt','w')
        f.write(str(M))
        f.close()

    def grossLoad(self):
        ku = len(self.nds)
        kss = self.kss;
        import numpy
        self.RR = numpy.zeros((ku * kss,1))
        for i in range(len(self.R)):
            for j in range(kss):
                self.RR[i * kss + j,0] = self.R[i][j]
        #print "RR=" + str(self.RR)

    def support(self):
        ku = len(self.NG)
        kss = len(self.NG[0])
        for i in range(ku):
            for j in range(kss):
                if (self.NG[i][j] == 0):
                    for rc in range(ku * kss):
                        self.K[i * kss + j, rc] = 0
                        self.K[rc, i * kss + j] = 0
                    self.K[i * kss + j, i * kss + j] = 1
                    self.RR[i * kss + j, 0] = 0

        f = open('gross.txt','w')
        f.write(str(self.K))
        f.close()

    def solve(self):
        self.u = self.K.I * self.RR
        #print "eps = " + str(va.norm(numpy.ravel(self.K * self.u - self.RR).T))
        kss = 6
        f = open('displ.txt', 'w')
        for i in range(len(self.u) // 6):
            f.write(' '.join([str(k) for k in numpy.ravel(self.u[i * kss: (i + 1) * kss])]))
            f.write('\n')
        f.close()


        #print 'u=' + str(self.u)

    def postproc(self):
        dsp = []
        eps = []
        frc = []
        kss = self.kss;
        for i in range(len(self.elm)):
            #print 'postproc \n'
            ui = numpy.zeros((2 * kss,1));
            ui = numpy.matrix(ui)
            ind = 0;
            #choose nodes displacmets for current element
            for j in range(len(self.elm[i].ND)):
                nn = self.elm[i].ND[j]
                for k in range(self.elm[i].KSS):
                    ui[ind] = self.u[nn * kss + k]
                    ind += 1
            #disp, strain and force in nodes and in the middle of the element
            dspi = []
            epsi = []
            frci = []
            coord = [0.0, 0.5, 1.0]
            #coord = [0.5]
            for j in range(len(coord)):
                self.elm[i].postproc(ui, coord[j] * self.elm[i].param[0][0], self.nds[self.elm[i].ND[0]][2])

    def unload(self):
        f = open('res.txt','w')
        f.write(self.elm[0].hd[0])
        for i in range(len(self.elm)):
            for j in range(len(self.elm[i].xyz)):
                buf = []
                buf.append(self.elm[i].xyz[j])
                for k in range(len(self.elm[i].dsp[j])):
                    buf.append(self.elm[i].dsp[j][k])
                for k in range(len(self.elm[i].eps[j])):
                    buf.append(self.elm[i].eps[j][k])
                for k in range(len(self.elm[i].frs[j])):
                    buf.append(self.elm[i].frs[j][k])
                for k in range(len(self.elm[i].sig[j])):
                    buf.append(self.elm[i].sig[j][k])
                #print 'buf=' + str(buf)
                f.write('\t'.join(['{:10.5}'.format(k) for k in buf]))
                f.write('\n')

        f.close()
