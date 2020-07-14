import sys
#print sys.path

from fem.staff import model

#nodes
nd = []
L = 100.0
N = 11

#calc node coordinates
for i in  range(N):
    ni = [0.0, 0.0, L / (N - 1) * i ]
    nd.append(ni)
#print "nd=" + str(nd)
#element topology
tp1 = []
for i in range(N - 1):
    tp1.append([i, i + 1])
tp2 = [[0, 1], [1, 2]]
#print "tp=" + str(tp1)
#nodes loads
rr = []
for i in range(len(nd)):
    rri = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    #rri = [0.0, 0.0]
    rr.append(rri)
rr[len(nd) - 1][0] = 0.0
rr[len(nd) - 1][1] = 200.0
rr[len(nd) - 1][2] = 2.0
rr[len(nd) - 1][5] = 41.9874
#rr[len(nd) - 1][1] = 19.099
#rr[len(nd) - 1][2] = 19.099
#rr[len(nd) - 1][5] = 214.243
#print "rr = " + str(rr)
#supports
ng = []
kss = 6
ind = 1
for i in range(len(nd)):
    ngi = []
    for j in range(kss):
        ngi.append(ind)
        ind+= 1
    ng.append(ngi)
for i in range(kss):
    ng[0][i] = 0

#print "ng = " + str(ng)

m = model.model()
m.setData([nd, tp1, rr, ng])
m.calcElems()
#m.checkEl()
m.grossMatrix()
m.grossLoad()
m.support()
m.solve()
m.postproc()
m.unload()
