from fem.staff import runcase
import math
import numpy as np
from fem.staff import va
from fem.beams import section
from fem.mat import elastic
from fem.analytics import KonsoleB

#Bernulli beam
print "Bernulli beam"
#circle section
test = [[1, [2.0e5, 0.3, 7.69e4], 1, 1, [(10.0 / math.pi)**0.5 ], [2.0e4, 19.099, 0.0, 0.0, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 1, [(10.0 / math.pi)**0.5 ], [2.0e4, 0.0, 19.099, 0.0, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 1, [(10.0 / math.pi)**0.5 ], [2.0e4, 0.0, 0.0, 1273.24, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 1, [(10.0 / math.pi)**0.5 ], [2.0e4, 0.0, 0.0, 0.0, 1273.24, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 1, [(10.0 / math.pi)**0.5 ], [2.0e4, 19.099, 19.099, 1273.24, 1273.24, 214.243]], 
       ]
res = [np.array(runcase.runCase(t).T).reshape(-1,).tolist() for t in test] 
e = elastic.elastic()
e.setData(test[0][1])   
e.calc()
sect = section.Circle()
sect.set_data([test[0][4], e.get_a()])

ans = [KonsoleB.dispKonsole(e, sect, t[5], 100.0) for t in test]

print "Circle section"
for i in range(len(res)):
    print va.variance(res[i],ans[i])
#rectangular section
test = [[1, [2.0e5, 0.3, 7.69e4], 1, 2, [ 10.0, 1.0 ], [2.0e4, 19.099, 0.0, 0.0, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 2, [ 10.0, 1.0 ], [2.0e4, 0.0, 19.099, 0.0, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 2, [ 10.0, 1.0 ], [2.0e4, 0.0, 0.0, 1273.24, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 2, [ 10.0, 1.0 ], [2.0e4, 0.0, 0.0, 0.0, 1273.24, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 2, [ 10.0, 1.0 ], [2.0e4, 19.099, 19.099, 1273.24, 1273.24, 214.243]], 
       ]
res = [np.array(runcase.runCase(t).T).reshape(-1,).tolist() for t in test] 
e = elastic.elastic()
e.setData(test[0][1])   
e.calc()
sect = section.Rectangle()
sect.set_data([test[0][4], e.get_a()])

ans = [KonsoleB.dispKonsole(e, sect, t[5], 100.0) for t in test]
print "Rectangular section"
for i in range(len(res)):
    print va.variance(res[i],ans[i])
#2tavr section s.set_data([[0.5, 0.16, 0.02, 0.014], e.get_a()])
test = [[1, [2.0e5, 0.3, 7.69e4], 1, 3, [50.0, 160.0, 20.0, 14.0], [2.0e4, 19.099, 0.0, 0.0, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 3, [50.0, 160.0, 20.0, 14.0], [2.0e4, 0.0, 19.099, 0.0, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 3, [50.0, 160.0, 20.0, 14.0], [2.0e4, 0.0, 0.0, 1273.24, 0.0, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 3, [50.0, 160.0, 20.0, 14.0], [2.0e4, 0.0, 0.0, 0.0, 1273.24, 214.243]], 
        [1, [2.0e5, 0.3, 7.69e4], 1, 3, [50.0, 160.0, 20.0, 14.0], [2.0e4, 19.099, 19.099, 1273.24, 1273.24, 214.243]], 
       ]
res = [np.array(runcase.runCase(t).T).reshape(-1,).tolist() for t in test] 
e = elastic.elastic()
e.setData(test[0][1])   
e.calc()
sect = section.TwoTavr()
sect.set_data([test[0][4], e.get_a()])

ans = [KonsoleB.dispKonsole(e, sect, t[5], 100.0) for t in test]
print "2tavr section"
for i in range(len(res)):
    print va.variance(res[i],ans[i])

'''

#Vlasov beam
test = [1, [2.0e5, 0.3, 7.69e4], 2, 1, [(10.0 / math.pi)**0.5 ], [2.0e4, 19.099, 0.0, 0.0, 0.0, 214.243]] 
res = np.array(runcase.runCase(test).T).reshape(-1,).tolist()
e = elastic.elastic()
e.setData(test[1])   
e.calc()
sect = section.Circle()
sect.set_data([test[4], e.get_a()])

ans = KonsoleB.dispKonsole(e, sect, test[5], 100.0)
print "Vlasov beam"
print "Circle section"
#print va.variance(res,ans)
print res
print ans
'''
