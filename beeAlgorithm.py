from random import random

def rosenbrockPlot(x,y):
    return (1 - x) ** 2 + 100*((y - x**2)**2)

def rosenbrock(point):
    return 100*pow((point[1] - pow(point[0],2)),2) + pow((1-point[0]),2)


scouts = 20
workers = 80
beesCounter = scouts + workers

bestZonesNum = 4
potentialZonesNum = 8

beesInBest = 10
beesInPotential = 5

zoneRange = 0.15
eps = 0.001

xRange = (-2.0,1.5)
yRange = (-1.0, 2.5)

counterOfStagnation = 0
maxStagnation = 10

prevBest = 0

def beesAlgorithm():
    global prevBest
    zones = getZones()
    bestZones = zones[:bestZonesNum]
    potentialZones = zones[bestZonesNum : bestZonesNum+potentialZonesNum]
    points = sendBees(bestZones, potentialZones)
    points.sort(key=rosenbrock)
    prevBest = rosenbrock(points[0])

    while True:
        bestZones = points[:bestZonesNum]
        potentialZones = points[bestZonesNum : bestZonesNum+potentialZonesNum]
        points = sendBees(bestZones, potentialZones)
        points.sort(key=rosenbrock)
        if checkStop(points):
            break

    print(points[0])
    return points


def checkStop(points):
    global prevBest
    global maxStagnation
    global counterOfStagnation

    currentBest = rosenbrock(points[0])
#    print(currentBest)
#    print(counterOfStagnation)
    if abs(currentBest-prevBest) > eps:
        counterOfStagnation = 0
    else:
        counterOfStagnation += 1

    if(counterOfStagnation>=maxStagnation):
        return True
    else:
        prevBest = currentBest
        return False


def getZones():
    zones = []
    for i in range(scouts):
        xRand = (xRange[0]+zoneRange) + random()*(xRange[1]-xRange[0]-zoneRange)
        yRand = (yRange[0]+zoneRange) + random()*(yRange[1]-yRange[0]-zoneRange)
        zones.append((xRand,yRand))

    zones.sort(key=rosenbrock, reverse=True)
    return zones

def sendBees(best, potential):
    res = []
    for i in range(len(best)):
#        print(f'Best zone {i}: {best[i]}\n')
        res.append(best[i])

        for j in range(beesInBest):
            randPoint = getRandomPoint(best[i][0]-zoneRange, best[i][0]+zoneRange, best[i][1]-zoneRange, best[i][1]+zoneRange)
#            print(f'point {j} {randPoint}')
            res.append(randPoint)

    for i in range(len(potential)):
#        print(f'Potential zone {i}: {potential[i]}\n')
        res.append(potential[i])

        for j in range(beesInPotential):
            randPoint = getRandomPoint(potential[i][0]-zoneRange, potential[i][0]+zoneRange, potential[i][1]-zoneRange, potential[i][1]+zoneRange)
#            print(f'point {j} {randPoint}')
            res.append(randPoint)
    return res

def getRandomPoint(xBot, xTop, yBot, yTop):
    xRand = xBot + random()*(xTop-xBot)
    yRand = yBot + random()*(yTop-yBot)

    return (xRand, yRand)

def getValues(points):
    res = []
    for i in range(len(points)):
        res.append(rosenbrock(points[i]))
    return res

beesAlgorithm()
