#[FMX: 1 - [E, nu, G]], modelId, [sectId, [sectParams]], [N, Qy, Qz, My, Mz, Mx]  
import sys
from fem.staff import model
#import model
def runCase(inputdata):
    [matid, fmx, beammod, sectid, sectpar, load] = inputdata
    #nodes
    nd = []
    L = 100.0
    N = 11
    #calc node coordinates
    for i in  range(N):
        ni = [0.0, 0.0, L / (N - 1) * i ]
        nd.append(ni)

    #element topology
    tp1 = []
    for i in range(N - 1):
        tp1.append([i, i + 1])

    #nodes loads
    rr = []
    for i in range(len(nd)):
        rri = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        rr.append(rri)
    rr[len(nd) - 1] = load

    #constrains
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

    m = model.model()
    m.setData([nd, tp1, rr, ng])
    m.calcElems(matid, fmx, beammod, sectid, sectpar)
    m.grossMatrix()
    m.grossLoad()
    m.support()
    m.solve()
    m.postproc()
    m.unload()
    return m.case_result()

