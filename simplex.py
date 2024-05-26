import numpy as np
import scipy as sp

resPoints = []
glist = []
def function(point):
    x,y = point
    return 2 * pow(x,2) + 2*x*y + 2*pow(y,2) - 4*x - 6*y

def plotFunction(x,y):
    return 2 * np.square(x) + 2 * x * y + 2 * np.square(y) - 4 * x - 6 * y

def callBack(nextPoint):
    global glist
    global resPoints
    g_list = np.ndarray.tolist(nextPoint)
    g_list.append(function(nextPoint))
    resPoints.append(g_list)

def getSimplex():
    global resPoints
    resPoints = []
    b = (0,float("inf"))
    bound = (b, b)
    x0 = (1,1)
    constr = {'type': 'eq', 'fun': function}
    res = sp.optimize.minimize(function, x0, method="SLSQP", bounds=bound, constraints=constr, callback=callBack)
    glist = np.ndarray.tolist(res.x)
    glist.append(res.fun)
    resPoints.append(glist)
    print(resPoints)

    return resPoints