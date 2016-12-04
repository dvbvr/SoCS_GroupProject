import numpy as np
import array as ar
import time
from HumanRandom import HumanRandom
#from PlotEnvironment import Plot
import matplotlib.pyplot as plt

nbrHuman = 10
fieldSize = 20
Agents = []
lifeTime = 100;
gridInfo = np.zeros((fieldSize,fieldSize,3))
for i in range(fieldSize):
	for j in range(fieldSize):
		gridInfo[i][j] = [0,0,0]
#
#initializes the humans on the fields
for i in range(0,nbrHuman):
	xPos = np.random.random_integers(1,3)
	yPos = np.random.random_integers(1,3)
	Agents.append(HumanRandom(xPos, yPos, lifeTime))
#

for it in range(1000):
	#spawn new ant from nest
	xPos = np.random.random_integers(1,3)
	yPos = np.random.random_integers(1,3)
	Agents.append(HumanRandom(xPos, yPos, lifeTime))
	nbrHuman += 1
	#moves all agents once
	i = 0
	while i < nbrHuman:
		[pos,health,sugar] = Agents[i].Move(gridInfo)
		if health < 0: #ants drop sugar on death
			gridInfo[pos[0]][pos[1]][2] += sugar
			del Agents[i]
			nbrHuman -= 1
		#
	#
	#lowers pheromones and food
	for i in range(fieldSize):
		for j in range(fieldSize):
			gridInfo[i][j][0] -= gridInfo[i][j][0]*0.1
			gridInfo[i][j][1] -= gridInfo[i][j][1]*1
			if (gridInfo[i][j][2] > 0):
				gridInfo[i][j][2] -= 1
			#
	#
	#Plot.AllFields(Plot ,gridInfo , 5 , 5) 
	#The above line does not work, the same goes for the import at row 5
