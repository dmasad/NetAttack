'''
Created on 22.07.2013

@author: jschmidt
'''


import networkx as nx

import numpy as np
import os
import glob
#from scipy.interpolate import interp1d

from DefenderAgent import * 
from AttackerAgent import * 

from EvolutionManager import EvolutionManager
import sys

def fitness_function(graph,penalty=20):
    diameter=0
    if nx.is_connected(graph):
        diameter=nx.diameter(graph)/penalty
    else:
        diameter=1
        
    return diameter

def fitness_function1(graph,penalty=1):
    ret=0
    LCC=nx.connected_component_subgraphs(graph)[0]
    #sp=nx.average_shortest_path_length(LCC)
    
    #relative shortest path length
    #rasp=(float)(sp)/(float)((len(LCC)+1)/3)
    #relative size of largest connected component
    rslcc=(float)(1)-(float)(len(LCC))/(float)(len(graph))
    #print len(LCC)
    #print len(graph)
    #print rslcc
    #print "-"
    #print rasp
    #print "---"
    #print rasp
    #print rslcc
    ret=(float)(rslcc)
    
    return ret

for files in glob.glob("*.txt"):
    os.remove(files)
    

#nodes=[100]
#edges=[150]
#pop_size=[200]
nodes=[20]
edges=[30]
pop_size=[20]

generation_count=[4]
offspring=[2]
mutation_rate=[0.05]
attacker_resources=[3]
defender_resources=[3, 5, 7, 9]

all_att_strat=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()]
all_def_strat=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()]
                                     
att_strat=[]                                      
def_strat=[]
   
#add attackers against single defenders
for i in range(len(all_def_strat)):
        att_strat.append(all_att_strat)
        def_strat.append([(all_def_strat[i])])

#add defenders against single attackers
for i in range(len(all_att_strat)):
        att_strat.append([all_att_strat[i]])
        def_strat.append(all_def_strat)


#add each one against each one
for i in range(len(all_att_strat)):
    for j in range(len(all_def_strat)):
        att_strat.append([(all_att_strat[i])])
        def_strat.append([(all_def_strat[j])])

#add co-evolution case
att_strat.append(all_att_strat)
def_strat.append(all_def_strat)


                                    
print att_strat
print def_strat

resDir="results"

if not os.path.exists(resDir):
    os.makedirs(resDir)

                                     
#stupid defender
if __name__ == '__main__':
    i=(int)(sys.argv[1])
    
    print i
    print "running"+str(i)
    evolution_manager = EvolutionManager(AttackerAgent, Defender, nodes[0],edges[0],fitness=fitness_function1, pop_size=pop_size[0], 
                                     generation_count=generation_count[0],offspring=offspring[0], mutation_rate=mutation_rate[0],initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=attacker_resources[0],defender_resources=defender_resources[(i-1)/16],
                                     attacker_strategies=att_strat[(i-1)%16],defender_strategies=def_strat[(i-1)%16],double_strategy=False)
        
    
    
    evolution_manager.run(True)
    
    for files in glob.glob("*.txt"):
        #print(files)
        os.rename(files,resDir+"/"+files)


