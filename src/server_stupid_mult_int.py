'''
Created on 22.07.2013

@author: jschmidt
'''


import networkx as nx

import numpy as np
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


nodes=[100]
edges=[150]
pop_size=[200]
generation_count=[500]
offspring=[2]
mutation_rate=[0.05]
attacker_resources=[3]
defender_resources=[3 5 7 9]

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
        def_strat.append(all_def_strat[i])


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


                                     
#stupid defender
if __name__ == '__main__':
    i=(int)(sys.argv[1])
    
    print i
    if(i == 1):
        print "running"+str(i)
        evolution_manager = EvolutionManager(AttackerAgent, Defender, nodes,edges,fitness=fitness_function1, pop_size=pop_size[1], 
                                     generation_count=generation_count[1],offspring=offspring[1], mutation_rate=mutation_rate[1],initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=attacker_resources[1],defender_resources=defender_resources[(i-1)/16+1],
                                     attacker_strategies=att_strat[i%16],defender_strategies=def_strat[i%16],double_strategy=False)
        

    evolution_manager.run(True)  


