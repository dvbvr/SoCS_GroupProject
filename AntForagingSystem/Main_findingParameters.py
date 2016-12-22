import numpy as np
import array as ar
import time
import os
import matplotlib
import matplotlib.pyplot as plt
from HumanRandom import HumanRandom
import matplotlib.pyplot as plt
from SocsSugarscape.packageSOCS.Plot import Environment


def main():
	os.environ["QT_API"] = "pyside"
	matplotlib.use('Qt5Agg')

	#===============================================================================
	# Function Parameters
	#===============================================================================
	nbrHuman = 0
	fieldSize = 40
	Agents = []
	lifeTime = 200
	HOME = 1
	FOOD = 0
	nestPosition = fieldSize//2  #general nest position

	carreiSize= 1
	collectedSugar = 0
	plotDelay = 0.001 #--> not working right now
	
	maxFoodPheromone = 3.5
	maxHomePheromone = 90

	ITERATIONS = 20000
	# For the Benchmark
	# keep the parameters under or equal to 0.2
	maxFoodAmount = 100
	foodDiff = 0.001
	homeDiff = 0.01
	timesDiff = 1
	
	for nbrBenchIteration in range(1000000):
		
		#===============================================================================
		# Benchmark loop
		#===============================================================================
		npaFood = np.array([])
		npaIterations = np.array([])
# 		foodDiff = foodDiff 
# 		homeDiff = homeDiff + nbrBenchIteration*homeDiff
	
		
		#subPlot1_Home, subPlot2_Food,  pheromoneFigure, pheroHomePlot, pheroFoodPlot = Environment.PheromoneGridFigure(fieldSize, maxFoodPheromone, maxHomePheromone)
		#antsSubPlot, antsFigure, antsPlotFood, antPlotHome, sugarPlot, nestPlot = Environment.AntGridFigure(fieldSize, maxFoodAmount, nestPosition)
	
		#===============================================================================
		# GRID RESOURCES --> ANTS
		#===============================================================================
		gridInfo = np.zeros((fieldSize,fieldSize,3))
		for i in range(fieldSize):
			for j in range(fieldSize):
				gridInfo[i][j] = [0,0,0] #[PheromeForaging, PheromoneRetHome, SugarAmount]
			#
		for i in range(nestPosition-2,nestPosition+3):
			for j in range(nestPosition-2,nestPosition+3):
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
		#
		spawn = 0
		
		#===============================================================================
		# Benchmark
		#===============================================================================
		gridInfo[5][5][2] = maxFoodAmount
		plotInfo[5][5][2] = maxFoodAmount
		
		gridInfo[35][5][2] = maxFoodAmount
		plotInfo[35][5][2] = maxFoodAmount
		
		gridInfo[5][35][2] = maxFoodAmount
		plotInfo[5][35][2] = maxFoodAmount
		
		gridInfo[20][5][2] = maxFoodAmount
		plotInfo[20][5][2] = maxFoodAmount
		
		gridInfo[5][20][2] = maxFoodAmount
		plotInfo[5][20][2] = maxFoodAmount
		
		gridInfo[10][5][2] = maxFoodAmount
		plotInfo[10][5][2] = maxFoodAmount
		
		gridInfo[5][10][2] = maxFoodAmount
		plotInfo[5][10][2] = maxFoodAmount
		
		gridInfo[10][15][2] = maxFoodAmount
		plotInfo[10][15][2] = maxFoodAmount
		
		gridInfo[25][25][2] = maxFoodAmount
		plotInfo[25][25][2] = maxFoodAmount
		
		gridInfo[35][35][2] = maxFoodAmount
		plotInfo[35][35][2] = maxFoodAmount
		
		benchmarkFood = maxFoodAmount*10
		
		
		
		for it in range(ITERATIONS):
			if(it%20000 == 19900):
				xPos = np.random.random_integers(0,fieldSize-1)
				yPos = np.random.random_integers(0,fieldSize-1)
				while gridInfo[xPos][yPos][2] == -1:
					xPos = np.random.random_integers(0,fieldSize-1)
					yPos = np.random.random_integers(0,fieldSize-1)
				gridInfo[xPos][yPos][2] = maxFoodAmount
				plotInfo[xPos][yPos][2] = maxFoodAmount
			#
		
			#spawn new ant from nest
			#if spawn:
			if(it%2 == 0 and spawn == 0):
				xPos = nestPosition
				yPos = nestPosition
				Agents.append(HumanRandom(xPos, yPos, lifeTime))
				nbrHuman += 1
			#
			
			if(spawn > 0):
				spawn -= 1
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
						#print(Agents[i].GetHealth(),'Health Left')
						Agents[i].ChangeState(FOOD)
						spawn += 1
						collectedSugar += 1
					#
				i += 1
			#
			
			for i in range(nbrHuman):
				[x,y] = Agents[i].GetPos()
				#if plotInfo[x][y][0] == 0:
				plotInfo[x][y][0] = Agents[i].GetState()
				plotInfo[x][y][1] = Agents[i].GetHealth()
			#
			
			diffGrid = np.zeros((fieldSize,fieldSize,3))
		
			
				
			
			for i in range(fieldSize):
				for j in range(fieldSize):
					diffGrid[i][j][0] -= gridInfo[i][j][0]*foodDiff*4
					diffGrid[i][j][1] -= gridInfo[i][j][1]*homeDiff*4
					
					diffGrid[(i+1)%fieldSize][(j)%fieldSize][0] += gridInfo[i][j][0]*foodDiff
					diffGrid[(i+1)%fieldSize][(j)%fieldSize][1] += gridInfo[i][j][1]*homeDiff
					
					diffGrid[(i)%fieldSize][(j-1)%fieldSize][0] += gridInfo[i][j][0]*foodDiff
					diffGrid[(i)%fieldSize][(j-1)%fieldSize][1] += gridInfo[i][j][1]*homeDiff
					
					diffGrid[(i-1)%fieldSize][(j)%fieldSize][0] += gridInfo[i][j][0]*foodDiff
					diffGrid[(i-1)%fieldSize][(j)%fieldSize][1] += gridInfo[i][j][1]*homeDiff
					
					diffGrid[(i)%fieldSize][(j+1)%fieldSize][0] += gridInfo[i][j][0]*foodDiff
					diffGrid[(i)%fieldSize][(j+1)%fieldSize][1] += gridInfo[i][j][1]*homeDiff
								
					gridInfo[i][j][0] -= gridInfo[i][j][0]*0.05
					if gridInfo[i][j][0] < 0.1:
						gridInfo[i][j][0] = 0
						diffGrid[i][j][0] = 0
					gridInfo[i][j][1] -= gridInfo[i][j][1]*0.001
					#if (gridInfo[i][j][2] > 0):
					#	gridInfo[i][j][2] -= 1
					#	plotInfo[i][j][2] -= 1
					#
				#
			#for
			
			nbrBenchIteration = nbrBenchIteration +1
			
			gridInfo = gridInfo + diffGrid
			plotW8 = 1 # how often to plot, e.i once every "plotW8" iterations
			if nbrBenchIteration%plotW8 == 0:
				print(collectedSugar/(it+1),'FoodCollected average')
				print(collectedSugar,'total sugar')
				print(it,'iterations')
				print(nbrHuman,'number of ants')
				npaFood = np.append(npaFood, collectedSugar)#
				npaIterations = np.append(npaIterations, it)
				
				#=======================================================================
				# Environment.AntGridPlot(np.copy(plotInfo), fieldSize, plotDelay, 
				# 							antPlotHome, antsPlotFood, sugarPlot, nestPlot,
				# 							antsSubPlot, antsFigure, nestPosition)
				# #
				# Environment.PheromoneGridPlot(pheromoneFigure, subPlot1_Home, subPlot2_Food,
				# 							np.copy(gridInfo), fieldSize, plotDelay,  
				# 							pheroHomePlot, pheroFoodPlot)
				# #
				#=======================================================================
			#
			plotWeigth = 500 # how often to plot, e.i once every "plotW8" iterations
			if nbrBenchIteration%plotWeigth == 1:		
#			if (collectedSugar == benchmarkFood):
				print(nbrBenchIteration,'Iterations needed for current parameters') 
				#save np arrays for plot
				#npaIterations
				#npaFood
				#foodDiff
				#homeDiff
				#=======================================================================
				# plot benchmark
				#=======================================================================
				figname='FindingParameters_nbrIterations_'+str(len(npaIterations))
				figsizeX =16
				figSizeY = 10                
				figsize=(figsizeX,figSizeY)
				benchFigure = plt.figure(figname,figsize)	
				benchSubPlot = benchFigure.add_subplot(111)     
				benchSubPlot.set_aspect('auto')
				benchSubPlot.set_title('food diffusion='+ str(foodDiff) + ' home diffusion=' + str(homeDiff) + ' focus on pheromone=3',fontsize=30)
				benchSubPlot.set_xlabel('iterations',fontsize=25)
				benchSubPlot.set_ylabel('food amount',fontsize=25)
				benchSubPlot.grid(True,linestyle='-',color='0.75')
				#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~		
				# Y # X
				plt.plot(npaIterations,npaFood, 'o-', ms=7, color='RoyalBlue')
				plt.savefig('BenchmarkPlot/' + figname + '.png')
				plt.savefig('BenchmarkPlot/' + figname + '.eps')
				plt.draw()
				timesDiff = timesDiff + 1
				#break
			#		
		# Benchmark loop
	# Main
	
if __name__ == '__main__':
	main()	
	
	
	
	
	