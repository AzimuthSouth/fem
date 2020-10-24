def dist(xyz1, xyz2):
    #print "x = {}, y = {}".format(xyz1, xyz2)
    return ((xyz1[0]-xyz2[0])**2 + (xyz1[1]-xyz2[1])**2 + (xyz1[2]-xyz2[2])**2)**0.5

def variance(v1, v2):
    s = 0
    for i in range(len(v1)):
        s+= (v1[i] - v2[i])**2
    return s**0.5 / min(norm(v1), norm(v2)) 

def norm(v):
    n = 0.0
    for i in range(len(v)):
        n += v[i]**2
    return n**0.5
