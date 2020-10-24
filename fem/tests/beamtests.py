from fem.staff import runcase
import math
#Bernulli beam
#circle section
test1 = [1, [2.0e5, 0.3, 7.69e4], 1, 1, [(10.0 / math.pi)**0.5 ], [2.0e4, 19.099, 19.099, 1273.24, 1273.24, 214.243]]
test1 = [1, [2.0e5, 0.3, 7.69e4], 1, 1, [(10.0 / math.pi)**0.5 ], [2.0e4, 0.0, 0.0, 0.0, 0.0, 0.0]]

print runcase.runCase(test1)
#rectangular section
test2 = [1, [2.0e5, 0.3, 7.69e4], 1, 2, [ 10.0, 1.0 ], [2.0e4, 19.099, 19.099, 1273.24, 1273.24, 214.243]]

