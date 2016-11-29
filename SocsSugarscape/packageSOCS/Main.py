import numpy as np
import array as ar
import time
from HumanRandom import HumanRandom
#from PlotEnvironment import Plot
import matplotlib.pyplot as plt

nbrHuman = 1
fieldSize = 20
Agents = []

gridInfo = np.zeros((fieldSize,fieldSize,3))

for i in range(fieldSize):
	for j in range(fieldSize):
		gridInfo[i][j] = [0,0,3]
#
gridMax = np.copy(gridInfo)
#initializes the humans on the fields
for i in range(0,nbrHuman):
	xPos = np.random.random_integers(0,fieldSize-1)
	yPos = np.random.random_integers(0,fieldSize-1)
	while gridInfo[xPos][yPos][1] > 0: # to find empty place
		xPos = np.random.random_integers(0,fieldSize-1)
		yPos = np.random.random_integers(0,fieldSize-1)
	Agents.append(HumanRandom(xPos, yPos, 10))
	gridInfo[xPos][yPos][0] = 1  #type one human
	gridInfo[xPos][yPos][1] = 10 # 10 starting health
#

for it in range(1000):
	#moves all agents once
	i = 0
	while i < nbrHuman:
		[pos1,pos2,health] = Agents[i].Move(np.copy(gridInfo))
		gridInfo[pos1[0]][pos1[1]][0] = 0 #remove human from old position
		gridInfo[pos1[0]][pos1[1]][1] = 0 #remove human from old position
	
		if health > 0: # only allowed to act if alive AFTER moving
			gridInfo[pos2[0]][pos2[1]][0] = 1 #add human to new position
			health = Agents[i].ChangeHealth(gridInfo[pos1[0]][pos1[1]][2]) #eats all sugar
			gridInfo[pos1[0]][pos1[1]][2] = 0 #no sugar left
			
			if health > 15 and pos1 != pos2:

				health = Agents[i].ChangeHealth(-10)
				gridInfo[pos1[0]][pos1[1]][0] = 1  #type one human
				gridInfo[pos1[0]][pos1[1]][1] = 10 # 10 starting health
				Agents.append(HumanRandom(pos1[0], pos1[1], 10))
				nbrHuman += 1
			#
			
			gridInfo[pos2[0]][pos2[1]][1] = health #the humans current health
		else: #if not alive after moving it gets removed
			del Agents[i]
			i -= 1
			nbrHuman -= 1
		#
		i += 1
	#
	
	for i in range(fieldSize):
		for j in range(fieldSize):
			if gridInfo[i][j][2] < gridMax[i][j][2]:
				gridInfo[i][j][2] += 0.2
	#
	#Plot.AllFields(Plot ,gridInfo , 5 , 5) 
	#The above line does not work, the same goes for the import at row 5
