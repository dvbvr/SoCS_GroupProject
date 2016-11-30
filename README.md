# Sugarscape
**Group1**

How to format this README.md
[GitHub basic formatting](https://help.github.com/articles/basic-writing-and-formatting-syntax/)

## Agrements:
### 20161118
fieldInfo[xPos][yPos] = [nObstacle, nZombies, nHumans, agentIndexes, ... ]
agentInfos[agentIndex] = agent
PlotEnvironment(fieldInfo, nAgents) 


## Todo:
### 20161118
- [x] plotEnvironment -> Dorian
- [x] firstMain, randomAgent -> Robin 
- [ ] report, theory of simple-reflex agents -> Lars
- [x] theory of learning agents -> Esteban
- [ ] Everyone should play with the code when you recieve the "start coding" SMS. This means making some agents
  - [x] Robin
  - [x] Dorian
  - [ ] Lars
  - [ ] Esteban  
- [ ] [GitHub Basics](https://try.github.io/levels/1/challenges/1)
  - [x] Robin
  - [x] Dorian
  - [ ] Lars
  - [x] Esteban   

### 20161125
GridInfo[x,y] = [AgentType,AgentHealth,SugarAmount]
- [x] new main that includes  -> Robin 
- [ ] Agent --> The new movement -> Robin 
- [x] Agent --> Eating -> Robin
- [x] Agent --> Survival -> Robin
- [ ] Environment
  - [?] Environment --> Dorian, Robin
  - [ ] InitEnvironment() --> initialization of sugar i.e. max-sugar in form of hills --> Dorian
- [ ] PlotEnvironment --> that plots the fieldInfo-> Dorian Esteban
- [ ] fix stuff with sharelatex , report + presentation -> Lars
- [ ] Theory for sugarscape -> Lars 

## 20163011 Research Ants (The third time is the charm!)
#### Dorian
- [x] [(1) Ants Theory and suggestions how to programm it p.59-64](http://www.jgorasia.com/Files/Fall08/CompMod/gorasia08compmod.pdf)

#### Esteban
- [x] [Java browser simulation](http://ccl.northwestern.edu/netlogo/models/run.cgi?Ants.790.569) of the ant foraging system 
- [x] [Java browser simulation](https://web.eecs.utk.edu/~mclennan/Classes/420-527-S13/NetLogo/Ant-Foraging.html) a bit more sofisticated than the one above
- [x] [(2) Article: Ant Foraging Revisited](http://cs.gmu.edu/~eclab/papers/panait04ant.pdf) Contains a pseudo-code
      Method:
      - Pheromones: 
        Two types: one to locate the food, other to locate the nest. 
        These pheromones evaporate, diffuse and can coexist in one spot.
      - Ants
        Two different states: looking for food, looking for the nest
        As they move they follow the trail they need depending on current state, while leaving a trail of the other type of pheromone.
        Depending on the pheromone levels, the ants preferably move to the front positions, if not to the other 5 positions, if not stays quiet.
### To do
- Read the article (1) and (2) see above.
- Lars: make report based on articles, and with the presentation if you have time
- General agreements for programming people:
  - Pheromone1 -> So that the ants find the way home (long lasting)
  - Pheromone2 -> So that the ants find food (transient)
  - Ant -> See above
  - Environment -> Terrain[nestPheromone, foodPheromone, food]



