import random
import math

def rosenbrockPlot(x,y):
    return (1 - x) ** 2 + 100*((y - x**2)**2)

import numpy as np

def rosenbrock(x):
    return np.sum(100*(x[1:]-x[:-1]**2)**2 + (1-x[:-1])**2)

def particle_swarm(dim, swarm_size=100, max_iter=100, c1=2, c2=2, w=0.7):
    # Инициализация
    swarm_position = np.random.uniform(-5, 5, (swarm_size, dim))
    swarm_velocity = np.random.uniform(-1, 1, (swarm_size, dim))
    pbest_position = swarm_position.copy()
    pbest_cost = np.full(swarm_size, np.inf)
    gbest_position = np.zeros(dim)
    gbest_cost = np.inf

    #обход по итерациям
    for i in range(max_iter):
        #обход по рою
        for j in range(swarm_size):
            #нахождение лучшей частицы
            cost = rosenbrock(swarm_position[j])
            if cost < pbest_cost[j]:
                pbest_cost[j] = cost
                pbest_position[j] = swarm_position[j].copy()
            if cost < gbest_cost:
                gbest_cost = cost
                gbest_position = swarm_position[j].copy()

            #меняем скорость
            r1, r2 = np.random.rand(dim), np.random.rand(dim)
            swarm_velocity[j] = w*swarm_velocity[j] + c1*r1*(pbest_position[j]-swarm_position[j]) + c2*r2*(gbest_position-swarm_position[j])
            swarm_position[j] += swarm_velocity[j]

        w *= 0.99

    res = list()
    res.append(gbest_position)
    return res