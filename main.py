from tkinter import *
import tkinter.ttk as ttk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection

import descent
import simplex
import genetic
import beeAlgorithm
import particle_swarm

def buildPlot(xGrid, yGrid, zGrid, resCord, resValue, maxValue, function):
    global plot
    global resultText
    global resultChordText
    global functionText
    global resultChordText

    if plot:
        plot.get_tk_widget().destroy()
        resultText.destroy()
        functionText.destroy()
        resultChordText.destroy()

    fig = plt.figure()
    ax_3d = fig.add_subplot(111, projection='3d')
    ax_3d.plot_surface(xGrid, yGrid, zGrid, cmap='inferno')

#    for points in resCord:
#       ax_3d.plot((points[0], points[0]), (points[1], points[1]), (0, maxValue))

    ax_3d.plot((resCord[len(resCord)-1][0], resCord[len(resCord)-1][0]), (resCord[len(resCord)-1][1], resCord[len(resCord)-1][1]), (0, maxValue))

    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    finalCord = resCord[len(resCord)-1]

    functionText = Label(text=f'Function: {function}', font=30)
    functionText.pack()
    resultText = Label(text=f'Result = {resValue}', font=30)
    resultText.pack()
    resultChordText = Label(text=f'Result coordinates: {finalCord}', font=30)
    resultChordText.pack()
    plot = FigureCanvasTkAgg(fig, master=root)
    plot.draw()
    plot.get_tk_widget().pack(side=BOTTOM, fill=NONE)

def generateFastDescent():
    changeSelected(btnDesc)
    fig = plt.figure()
    x = np.arange(-1,1,0.01)
    y = np.arange(-1,1,0.01)

    xgrid, ygrid = np.meshgrid(x,y)
    zgrid = descent.function(xgrid, ygrid)
    res = descent.getFastDescent()

    finalRes = res[len(res)-1]
    results = []
    for i in range(len(res)):
        results.append(descent.function(res[i][0], res[i][1]))

#    print(results)
    maxRes = min(results)
#    print(maxRes)
    function = "2*x^2 + x*y + y^2"

    buildPlot(xgrid, ygrid, zgrid, res, descent.function(finalRes[0], finalRes[1]), 4, function)

def generateSimplexMethod():
    changeSelected(btnSimp)
    fig = plt.figure()
    x = np.arange(-5, 5, 0.01)
    y = np.arange(-5, 5, 0.01)

    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = simplex.plotFunction(xgrid, ygrid)
    res = simplex.getSimplex()

    finalRes = res[len(res)-1][2]
    results = []
    resPoints = []
    for i in range(len(res)):
        results.append(res[i][2])
        resPoints.append( (res[i][0], res[i][1]) )
    maxRes = min(results)
    function = "2*x^2 + 2*x*y + 2*y^2 - 4*x - 6*y"

    buildPlot(xgrid, ygrid, zgrid, resPoints, finalRes, 200, function)

def generateGenAlg():
    changeSelected(btnGenetic)
    fig = plt.figure()
    x = np.arange(-2, 2, 0.5)
    y = np.arange(-1, 3, 0.5)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = genetic.rosenbrockPlot(xgrid, ygrid)
    resPoints, finalRes = genetic.genetic_algorithm(pop_size=100, dim=2, generations=2000)

    function = "(1-x)^2 + 100*(y - x^2)^2"

    buildPlot(xgrid, ygrid, zgrid, resPoints, finalRes, 2500, function)

def generateParticleAlgorithm():
    changeSelected(btnParticle)
    fig = plt.figure()
    x = np.arange(-2,2,0.01)
    y = np.arange(-2,2,0.01)

    xgrid, ygrid = np.meshgrid(x,y)
    zgrid = particle_swarm.rosenbrockPlot(xgrid, ygrid)
    res = particle_swarm.particle_swarm(2)
    finalRes = res[0]
    print(finalRes)
    function = "(1-x)^2 + 100*(y - x^2)^2"

    buildPlot(xgrid, ygrid, zgrid, res, particle_swarm.rosenbrockPlot(finalRes[0], finalRes[1]), 2500, function)

def generateBeeAlgorithm():
    changeSelected(btnBee)
    fig = plt.figure()
    x = np.arange(-2,2,0.01)
    y = np.arange(-2,2,0.01)

    xgrid, ygrid = np.meshgrid(x,y)
    zgrid = beeAlgorithm.rosenbrockPlot(xgrid, ygrid)
    res = beeAlgorithm.beesAlgorithm()

    finalRes = res[0]
    results = []
    for i in range(len(res)):
        results.append(beeAlgorithm.rosenbrockPlot(res[i][0], res[i][1]))

    maxRes = min(results)
#    print(maxRes)
    function = "(1-x)^2 + 100*(y - x^2)^2"

    buildPlot(xgrid, ygrid, zgrid, res, beeAlgorithm.rosenbrockPlot(finalRes[0], finalRes[1]), 2500, function)

def changeSelected(clickedButton):
    global selectedButton
    if selectedButton:
        selectedButton.config(state='enabled')
    selectedButton = clickedButton
    selectedButton.config(state='disabled')


selectedButton = None

root = Tk()
resultChordText = None
resultText = None
functionText = None
plot = None
root.title("Project \"Optimization\" 0.1")

root.geometry("1000x600")

upFrame = ttk.Frame(height=100, padding=[8,10], relief=SOLID)
upFrame.pack(anchor=NW, fill=X)

upFrame.columnconfigure(index=0, weight=1)
upFrame.columnconfigure(index=1, weight=1)
upFrame.columnconfigure(index=2, weight=1)
upFrame.columnconfigure(index=3, weight=1)
upFrame.columnconfigure(index=4, weight=1)

btnDesc = ttk.Button(upFrame, text="Fast descent".upper(), command=generateFastDescent)
btnDesc.grid(row=0, column=0)

btnSimp = ttk.Button(upFrame, text="Simplex method".upper(), command=generateSimplexMethod)
btnSimp.grid(row=0, column=1)

btnGenetic = ttk.Button(upFrame, text="Genetic algorithm".upper(), command=generateGenAlg)
btnGenetic.grid(row=0, column=2)

btnParticle = ttk.Button(upFrame, text="Swarm algorithm".upper(), command=generateParticleAlgorithm)
btnParticle.grid(row=0, column=3)

btnBee = ttk.Button(upFrame, text="Bee Movie".upper(), command=generateBeeAlgorithm)
btnBee.grid(row=0, column=4)

root.mainloop()