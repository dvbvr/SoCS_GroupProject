'''
Created on 21.11.2016

@author: dori
'''

import numpy as np
import matplotlib.pyplot as plt


class Environment:

	def AntGridFigure(fieldSize, maxFoodAmount, nestPosition):    
		'''
		This method has to be called before the looping occours, for a better performance.
		Inspired by:
		http://bastibe.de/2013-05-30-speeding-up-matplotlib.html
		'''
		#=======================================================================
		# The Figure
		#======================================================================= 
		# Define the COLORMAPS for the plots
		# Health:
		#cmapHealth = plt.cm.get_cmap('cool')
		# Sugar:	
		cmapSugar = plt.cm.get_cmap('PiYG_r')#('YlOrRd')#('Blues')#('YlOrRd')
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
		figname='Environment'
		figsizeX =18
		figSizeY = 9                
		figsize=(figsizeX,figSizeY)
		antsFigure = plt.figure(figname,figsize)	
		antsSubPlot = antsFigure.add_subplot(111)     
		antsSubPlot.set_aspect('equal')
		antsSubPlot.set_title('Environment',fontsize=14)
		antsSubPlot.set_xlabel('x',fontsize=12)
		antsSubPlot.set_ylabel('y',fontsize=12)
		#antsSubPlot.grid(True,linestyle='-',color='0.75')
		antsSubPlot.set_xlim(-0.5, fieldSize+0.5-1)
		antsSubPlot.set_ylim(-0.5, fieldSize+0.5-1)     
		plt.axis('off')
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~		
		npaAgentForagingPosY = np.array([0])
		npaAgentForagingPosX = np.array([0])
		npaFoodAmount = np.zeros((fieldSize,fieldSize))
		#
		sugarPlot = antsSubPlot.imshow(npaFoodAmount, interpolation='none', cmap=cmapSugar, vmin=0, vmax=maxFoodAmount)
		antsPlotFood, 	= antsSubPlot.plot(npaAgentForagingPosY,npaAgentForagingPosX, 'p', ms=7, color='violet')
		antPlotHome, 	= antsSubPlot.plot(npaAgentForagingPosY,npaAgentForagingPosX, 'o', ms=10, color='blue')	
		nestPlot, 		= antsSubPlot.plot(nestPosition,nestPosition, 'o', ms=30, color='black')	
		# Legend
		handles, labels = antsSubPlot.get_legend_handles_labels()
		display = (0,1,2)
		# Create custom artists
		#antsSubPlot.legend(scatterpoints=1, bbox_to_anchor=(0,0,-0.05, 1))
		AntsForaging 		= plt.Line2D((0,1),(0,0), color='violet', marker='p')
		AntsReturningHome 	= plt.Line2D((0,1),(0,0), color='blue', marker='o')
		nest				= plt.Line2D((0,1),(0,0), color='black', marker='o')
		#food				= plt.Line2D((0,1),(0,0), color='black', marker='s')
		# Create legend from custom artist/label lists
		antsSubPlot.legend([handle for i,handle in enumerate(handles) if i in display]+[AntsForaging,AntsReturningHome,nest],
							[label for i,label in enumerate(labels) if i in display]+['Ants foraging', 'Ants returning home', 'Nest'],
							numpoints=1, bbox_to_anchor=(0,0,-0.05, 1))

		#
		img = plt.imshow(np.array([[0,1]]), cmap=cmapSugar)
		img.set_visible(False)		
		cbarAmountSugar = plt.colorbar(orientation="vertical")
		cbarAmountSugar.set_label('Amount of food')
		#
		plt.ion()
		plt.pause(0.0001)
		antsFigure.canvas.draw()
		plt.ioff()
		#
		return antsSubPlot, antsFigure, antsPlotFood, antPlotHome, sugarPlot, nestPlot
	#
	
	

	def AntGridPlot(terrainInfo, fieldSize, PlotDelay, 
				antsPlotHome, antsPlotFood, sugarPlot, nestPlot,
				antsSubPlot, antsFigure, nestPosition):    
		#======================================================================
		# Structure of the terrainInfo:
		#======================================================================
		# [agentState, agentHealth, sugarAmount]
		# [agentSate: 	0:foraging 
		#				1:ReturningHome
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
		AGENTSTATE = 0
		AGENTHEALTH = 1
		SUGARAMOUNT = 2
		AGENTFORAGING = 0
		AGENTRETURNINGHOME = 1		
		# AgentForaging position and state        
		npaAgentForagingPosX = np.array([])
		npaAgentForagingPosY = np.array([])
		npaAgentStateFor = np.array([])
		paAgentHealthFor = np.array([])
		# AgentRetHome position and state        
		npaAgentRetHomePosX = np.array([])
		npaAgentRetHomePosY = np.array([])
		npaAgentStateRet = np.array([])
		npaAgentHealthRetHome = np.array([])
		
		#=======================================================================
		# Get Information from terrainInfo,
		#=======================================================================
		for y in range(fieldSize):
			for x in range(fieldSize):
				# If HEALTH than there is a agent
				if terrainInfo[y,x,AGENTHEALTH] >= 1: 					
					# Recognise the foraging agent
					if terrainInfo[y,x,AGENTSTATE] == AGENTFORAGING: 
						npaAgentForagingPosX 	= np.append(npaAgentForagingPosX, np.array([x]))
						npaAgentForagingPosY 	= np.append(npaAgentForagingPosY, np.array([y]))
						npaAgentStateFor 		= np.append(npaAgentStateFor, terrainInfo[x,y,AGENTSTATE])
						paAgentHealthFor 		= np.append(paAgentHealthFor, terrainInfo[x,y,AGENTHEALTH])						
					# Recognise the returning agent
					if terrainInfo[y,x,AGENTSTATE] == AGENTRETURNINGHOME: 
						npaAgentRetHomePosX 	= np.append(npaAgentRetHomePosX, np.array([x]))
						npaAgentRetHomePosY 	= np.append(npaAgentRetHomePosY, np.array([y]))
						npaAgentStateRet 		= np.append(npaAgentStateRet, terrainInfo[x,y,AGENTSTATE])
						npaAgentHealthRetHome 	= np.append(npaAgentHealthRetHome, terrainInfo[x,y,AGENTHEALTH])
					#
				#
			#
		#		
		npaFoodAmount = terrainInfo[:,:,SUGARAMOUNT]
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		#=======================================================================		
		# Plots 
		#=======================================================================
		Environment.UpdatePlot(antsPlotFood, antsPlotHome, sugarPlot, nestPlot, nestPosition,
							antsSubPlot, antsFigure, 
							npaAgentForagingPosX, npaAgentForagingPosY,
							npaAgentRetHomePosX, npaAgentRetHomePosY,
							npaFoodAmount)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#



	def UpdatePlot(antsPlot1, antsPlot2, sugarPlot, nestPlot, nestPosition,
				antsSubPlot, antsFigure, 
				new_dataX1, new_dataY1,
				new_dataX2, new_dataY2,
				new_data3):
		
		sugarPlot.set_data(new_data3)					
		antsPlot1.set_xdata(new_dataX1)
		antsPlot1.set_ydata(new_dataY1)
		antsPlot2.set_xdata(new_dataX2)
		antsPlot2.set_ydata(new_dataY2)	
		nestPlot.set_xdata(nestPosition)
		nestPlot.set_ydata(nestPosition)
		#	
		antsSubPlot.draw_artist(antsSubPlot.patch)
		antsSubPlot.draw_artist(sugarPlot)
		antsSubPlot.draw_artist(nestPlot)
		antsSubPlot.draw_artist(antsPlot1)
		antsSubPlot.draw_artist(antsPlot2)
		#
		antsFigure.canvas.update()
		antsFigure.canvas.flush_events()
	#
	
	
	
	def PheromoneGridFigure(fieldSize, 
						maxFoodPheromone, maxHomePheromone, 
						nestPosition=None):
		#=======================================================================
		# The Figure and the axis 
		# (This has to be outside of the loop for better performance)
		#======================================================================= 
		# Define the COLORMAPS for the plots
		cmapFood = plt.cm.get_cmap('YlOrRd')#('Blues')#('YlOrRd')
		cmapHome = plt.cm.get_cmap('YlGn')#('Blues')#('YlOrRd')   
		#
		figname='Pheromonetypes'
		figsizeX =18
		figSizeY = 9                
		figsize=(figsizeX,figSizeY)
		#
		pheromoneFigure = plt.figure(figname,figsize)	
		#			
		subPlot1_Home = pheromoneFigure.add_subplot(121)        
		subPlot1_Home.set_title('Pheromene home',fontsize=14)
		subPlot1_Home.set_xlabel('x',fontsize=12)
		subPlot1_Home.set_ylabel('y',fontsize=12)
		#subPlot1_Home.grid(True,linestyle='-',color='0.75')
		subPlot1_Home.set_xlim(-0.5, fieldSize+0.5-1)
		subPlot1_Home.set_ylim(-0.5, fieldSize+0.5-1)  
		#
		subPlot2_Food = pheromoneFigure.add_subplot(122)
		subPlot2_Food.set_title('Pheromone food',fontsize=14)
		subPlot2_Food.set_xlabel('x',fontsize=12)
		subPlot2_Food.set_ylabel('y',fontsize=12)
		#subPlot2_Food.grid(True,linestyle='-',color='0.75')
		subPlot2_Food.set_xlim(-0.5, fieldSize+0.5-1)
		subPlot2_Food.set_ylim(-0.5, fieldSize+0.5-1)   
		#
		imshowEmptyArray = np.zeros((fieldSize,fieldSize))  
		#
		pheroHomePlot = subPlot1_Home.imshow(
			                imshowEmptyArray, 
			                interpolation='none', 
			                cmap=cmapHome,
			                vmin=0, vmax=maxHomePheromone)
		#		
		plt.show(block=False)

		pheroFoodPlot = subPlot2_Food.imshow(
			                imshowEmptyArray, 
			                interpolation='none', 
			                cmap=cmapFood,
			                vmin=0, vmax=maxFoodPheromone)
		#       		
		plt.show(block=False)
		return subPlot1_Home, subPlot2_Food, pheromoneFigure, pheroHomePlot, pheroFoodPlot
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
		
		
	def PheromoneGridPlot(pheromoneFigure, subPlot1_Home, subPlot2_Food,
						terrainInfo, fieldSize, PlotDelay,
						pheroHomePlot, pheroFoodPlot,
						nestPosition=None):   
		#=======================================================================
		# Add the data to the axis (Use this code while looping)
		# [Pheromone1, Pheromone2, sugarAmount]
		# get sugar amounts from terrainInfo
		#======================================================================= 
		PHEROMONE_HOME = 1
		PHEROMONE_FOOD = 0	
		#
		npaPHEROMONE_HOME = terrainInfo[:,:,PHEROMONE_HOME]
		#subPlot1_Home.draw_artist(subPlot1_Home.patch)			
		pheroHomePlot.set_data(npaPHEROMONE_HOME)	
		subPlot1_Home.draw_artist(pheroHomePlot)
		#
		npaPHEROMONE_FOOD = terrainInfo[:,:,PHEROMONE_FOOD]	
		#subPlot2_Food.draw_artist(subPlot2_Food.patch)
		pheroFoodPlot.set_data(npaPHEROMONE_FOOD)	
		subPlot2_Food.draw_artist(pheroFoodPlot)
		#
		pheromoneFigure.canvas.update()
		pheromoneFigure.canvas.flush_events()		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#




