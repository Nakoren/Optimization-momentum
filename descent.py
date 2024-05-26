import math
import numpy as np

MaxIter = 10
eps1 = 0.1
eps2 = 0.15
tValues = (0.24,0.546,0.24)
baseStep = 0.2

def getVectDistance(vect):
    return math.sqrt(math.pow(vect[0],2) + math.pow(vect[1],2))

def function(x,y):
    return 2 * np.square(x) + x*y + np.square(y)

def derivationX(x,y):
    return 4*x + y

def derivationY(x,y):
    return 2*y + x

def getGradient(point):
    x,y = point
    res = (derivationX(x,y), derivationY(x,y))
    return res

def getStep(point,grad):
    return 0


def getFastDescent():
    k=0
    resValues = [(0.5,1)]
    grad = getGradient(resValues[k])
    gradDist = getVectDistance(grad)
    while (k<=MaxIter and gradDist>=eps1):
        curT = tValues[k]
        step = (grad[0] * curT, grad[1] * curT)
        
        print(resValues[k])
        print(curT)
        print(grad)
        print(gradDist)
        print()
        
        nextValue = (resValues[k][0]-step[0], resValues[k][1] - step[1])
        resValues.append(nextValue)
        k+=1
        grad = getGradient(resValues[k])
        gradDist = getVectDistance(grad)
        
        resDiff = (resValues[k][0] - resValues[k-1][0],resValues[k][1] - resValues[k-1][1])
        if (getVectDistance(resDiff)<eps2): 
            break

    return resValues