'''
Created on 22.07.2013

@author: jschmidt
'''


import networkx as nx
import matplotlib.pyplot as plt

import numpy as np
#from scipy.interpolate import interp1d

from DefenderAgent import Defender
from DefenderAgent import Defender1
from AttackerAgent import AttackerAgent

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
#for i in range(5):
run_config_nodes   = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]

run_config_edges   = [40, 45, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60, 40, 45, 50, 55, 60]

run_config_at_res  = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5,5]

run_config_def_res = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,5]

i=(int)(sys.argv[1])
evolution_manager = EvolutionManager(AttackerAgent, Defender, run_config_nodes[i], run_config_edges[i],fitness=fitness_function1, pop_size=100, 
                                     generation_count=300,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=run_config_at_res[i],defender_resources=run_config_def_res[i])
 
evolution_manager.run(True)


