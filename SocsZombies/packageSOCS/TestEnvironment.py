'''
Created on 20.11.2016

@author: dori
'''
import Agent
import Environment

postion = [1,3]
health = 10

myHumanAgent = Agent.Agent(postion, health)
print(myHumanAgent)
print(myHumanAgent.GetState())
print('--------')
myZombieAgent = Agent.Agent(postion, health, stateOfBeing = 1)
print(myZombieAgent)
print(myZombieAgent.GetState())
print('--------')
myObstacle = Agent.Thing(postion)
print(myObstacle)
testing = myObstacle.GetState()
print(testing)
print('--------')

testPosition = myHumanAgent.GetPosition()
testPositionii = myObstacle.GetPosition()
print(testPosition + testPositionii)
print('--------')

myEnvironment = Environment.TwoDimensionalEnvironment(10,10)
print('--------')
