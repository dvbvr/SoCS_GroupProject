#===============================================================================
# External Libraries
#===============================================================================
import numpy as np
import matplotlib.pyplot as plt


#===============================================================================
# Import of our Libraries
#===============================================================================
from SocsSugarscape.packageSOCS.HumanRandom import HumanRandom
from SocsSugarscape.packageSOCS.Plot import Environment
from SocsSugarscape.packageSOCS.InitializationMethods import Initialize


#===============================================================================
# Declare variables
#===============================================================================
nbrHuman = 0
fieldSize = 50
Agents = []
lifeTime = 100
HOME = 1
FOOD = 0
nestPosition = fieldSize//2  #general nest position
maxSugar = 100
carreiSize= 1
collectedSugar = 0
PlotDelay = 0.0005

#===============================================================================
# GRID RESOURCES --> ANTS
#===============================================================================
gridInfo = np.zeros((fieldSize,fieldSize,3))
for i in range(fieldSize):
	for j in range(fieldSize):
		gridInfo[i][j] = [0,0,0] #[PheromeForaging, PheromoneRetHome, SugarAmount]
	#
for i in range(nestPosition-1,nestPosition+2):
	for j in range(nestPosition-1,nestPosition+2):
		gridInfo[i][j][2] = -1
	#	
		
#===========================================================================
# PLOT INFO 
#===========================================================================
plotInfo = np.zeros((fieldSize,fieldSize,3))
for i in range(fieldSize):
	for j in range(fieldSize):
		plotInfo[i][j] = [0,0,0] #[state, health, SugarAmount]
	#
spawn = True
gridInfo[5][5][2] = 1000
plotInfo[5][5][2] = 1000
for it in range(200000):
	gridInfo[5][5][2] = 1000
	plotInfo[5][5][2] = 1000
	#spawn new ant from nest
	#if spawn:
	xPos = np.random.random_integers(nestPosition-1,nestPosition+1)
	yPos = np.random.random_integers(nestPosition-1,nestPosition+1)
	Agents.append(HumanRandom(xPos, yPos, lifeTime))
	nbrHuman += 1
	#spawn = True
	#moves all agents once
	i = 0
	while i < nbrHuman:
		[pos,oldPos,health] = Agents[i].Move(gridInfo)
		plotInfo[oldPos[0]][oldPos[1]][1] = 0 #reset state
		plotInfo[oldPos[0]][oldPos[1]][1] = 0 #reset HP
		if health < 0: #the ant die
			del Agents[i]
			nbrHuman -= 1
		else:
			if gridInfo[pos[0]][pos[1]][2] > 0  and Agents[i].GetState() == FOOD : 
				#to recognise sugar
				Agents[i].ChangeState(HOME)
				plotInfo[pos[0]][pos[1]][2] -= 1
				gridInfo[pos[0]][pos[1]][2] -= 1
			#
			if gridInfo[pos[0]][pos[1]][2] == -1 and Agents[i].GetState() == HOME : 
				#to recognise nest
				Agents[i].ChangeState(FOOD)
				#spawn = False
				collectedSugar += 1
			#
		i += 1
		#
	#
	for i in range(nbrHuman):
		[x,y] = Agents[i].GetPos()
		#if plotInfo[x][y][0] == 0:
		plotInfo[x][y][0] = Agents[i].GetState()
		plotInfo[x][y][1] = Agents[i].GetHealth()
	#
	diffGrid = np.zeros((fieldSize,fieldSize,3))
	#lowers pheromones and food
	#FIX add diffusion'
	diffRate = 0.001
	for i in range(fieldSize):
		for j in range(fieldSize):
			diffGrid[i][j][0] -= gridInfo[i][j][0]*diffRate*4
			diffGrid[i][j][1] -= gridInfo[i][j][1]*diffRate*4*10
			
			diffGrid[(i+1)%fieldSize][(j+1)%fieldSize][0] += gridInfo[i][j][0]*diffRate
			diffGrid[(i+1)%fieldSize][(j+1)%fieldSize][1] += gridInfo[i][j][1]*diffRate*10
			
			diffGrid[(i+1)%fieldSize][(j-1)%fieldSize][0] += gridInfo[i][j][0]*diffRate
			diffGrid[(i+1)%fieldSize][(j-1)%fieldSize][1] += gridInfo[i][j][1]*diffRate*10
			
			diffGrid[(i-1)%fieldSize][(j+1)%fieldSize][0] += gridInfo[i][j][0]*diffRate
			diffGrid[(i-1)%fieldSize][(j+1)%fieldSize][1] += gridInfo[i][j][1]*diffRate*10
			
			diffGrid[(i-1)%fieldSize][(j-1)%fieldSize][0] += gridInfo[i][j][0]*diffRate
			diffGrid[(i-1)%fieldSize][(j-1)%fieldSize][1] += gridInfo[i][j][1]*diffRate*10
			
			
			gridInfo[i][j][0] -= gridInfo[i][j][0]*0.001
			gridInfo[i][j][1] -= gridInfo[i][j][1]*0.01
			if (gridInfo[i][j][2] > 0):
				gridInfo[i][j][2] -= 1
				plotInfo[i][j][2] -= 1
			#
	#
	gridInfo = gridInfo + diffGrid
	plotW8 = 10 # how often to plot, e.i once every "plotW8" iterations
	if it%plotW8 == 5:
		print(collectedSugar/(it+1),'FoodCollected average')
		Environment.Grid(np.copy(plotInfo), fieldSize, PlotDelay)

plt.show()
