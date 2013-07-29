'''
Created on 22.07.2013

@author: jschmidt
'''


import networkx as nx
import matplotlib.pyplot as plt

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




if __name__ == '__main__':
    #stupid defender
    evolution_manager = EvolutionManager(AttackerAgent, Defender, 10, 15,fitness=fitness_function1, pop_size=20, 
                                     generation_count=500,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix="_test_multi",file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)
    evolution_manager.run(True)
