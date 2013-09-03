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



#stupid defender
if __name__ == '__main__':
    i=(int)(sys.argv[1])
    
    print "running"+str(i)
    if(i == 1):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100,150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        
    if(i == 2):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100,150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
      
    if(i == 3):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100,150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment(),BalancedReplenishment()],double_strategy=False)
      
    if(i == 4):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100,150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment()],double_strategy=False)


    if(i == 5):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 6):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 7):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 8):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 9):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 10):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 11):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 12):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 13):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=200, 
                                     generation_count=500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
       


    evolution_manager.run(True)  


