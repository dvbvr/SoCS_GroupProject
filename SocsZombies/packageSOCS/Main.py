import numpy as np
import array as ar
from HumanRandom import HumanRandom
from PlotEnvironment import Plot

nbrAgents = 10
nbrHuman = 10
nbrDead = 0
nbrZombies = nbrAgents-nbrHuman
fieldSize = 3
Agents = []

fieldInfo = np.zeros((fieldSize,fieldSize), dtype=object)
for it in range(5):
	for i in range(3):
		for j in range(3):
			fieldInfo[i][j] = [0,0,0]
	#
	
	#initializes the humans on the fields
	for i in range(0,nbrHuman):
		xPos = np.random.random_integers(0,fieldSize-1)
		yPos = np.random.random_integers(0,fieldSize-1)
		Agents.append(HumanRandom(xPos, yPos, 10))
		fieldInfo[xPos][yPos][2] = fieldInfo[xPos][yPos][2] + 1 #one human added
		fieldInfo[xPos][yPos].append(i)
	#
	
	#initializes the zombies on the fields
	for i in range(nbrHuman,nbrAgents):
		xPos = np.random.random_integers(0,fieldSize-1)
		yPos = np.random.random_integers(0,fieldSize-1)
		#Agents.append(ZombieRandom(xPos, yPos, 10))
		fieldInfo[xPos][yPos][1] = fieldInfo[xPos][yPos][1] + 1 #one zombie added
		fieldInfo[xPos][yPos].append(i)
	#
	
	#moves all agents once
	for i in range(0,nbrAgents):
		[pos1,pos2] = Agents[i].Move(fieldInfo)
		info = fieldInfo[pos1[0]][pos1[1]]
		for j in range(3,len(info)):
			if info[j] == i:
				del fieldInfo[pos1[0]][pos1[1]][j]
				break	
		if Agents[i].GetState() == 0:
			fieldInfo[pos1[0]][pos1[1]][2] = fieldInfo[pos1[0]][pos1[1]][2] - 1 #one human removed
			fieldInfo[pos2[0]][pos2[1]][2] = fieldInfo[pos2[0]][pos2[1]][2] + 1 #one human added
		else:
			fieldInfo[pos1[0]][pos1[1]][1] = fieldInfo[pos1[0]][pos1[1]][1] - 1 #one zombie removed
			fieldInfo[pos2[0]][pos2[1]][1] = fieldInfo[pos2[0]][pos2[1]][1] + 1 #one zombie added
		fieldInfo[pos2[0]][pos2[1]].append(i)	
	#
	#Plot.AllFields(Plot ,fieldInfo , 3 , 3) 
	#The above line does one print and is probably the wrong way of using the plot code xD
	#Also the import made on line 4 might be just as bad
