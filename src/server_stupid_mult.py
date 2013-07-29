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


#stupid defender
if __name__ == '__main__':
    i=(int)(sys.argv[1])
    print i
    if(i == 1):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 4, 4,fitness=fitness_function1, pop_size=500, 
                                     generation_count=5,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)
        

    if(i == 2):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)
        

    if(i == 3):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)
        


    #stupid attacker
    if(i == 4):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        

    if(i == 5):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        

    if(i == 6):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)

        

        #co-evolution
    if(i == 7):
       evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
       
       
    if(i == 8):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 9):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 10):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 11):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 12):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 13):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 14):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 15):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 16):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=3,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
       
    
    if(i == 17):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 4, 4,fitness=fitness_function1, pop_size=500, 
                                     generation_count=5,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)
        

    if(i == 18):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)
        

    if(i == 19):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)
        


    #stupid attacker
    if(i == 20):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        

    if(i == 21):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        

    if(i == 22):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)

        

        #co-evolution
    if(i == 23):
       evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
       
       
    if(i == 24):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 25):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 26):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 27):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 28):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 29):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 30):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 31):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 32):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=4,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 33):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 4, 4,fitness=fitness_function1, pop_size=500, 
                                     generation_count=5,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)
        

    if(i == 34):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)
        

    if(i == 35):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)
        


    #stupid attacker
    if(i == 36):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        

    if(i == 37):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        

    if(i == 38):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)

        

        #co-evolution
    if(i == 39):
       evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
       
       
    if(i == 40):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 41):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 42):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 43):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 44):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 45):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 46):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 47):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 48):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=5,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 49):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 4, 4,fitness=fitness_function1, pop_size=500, 
                                     generation_count=5,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)
        

    if(i == 50):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)
        

    if(i == 51):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)
        


    #stupid attacker
    if(i == 52):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        

    if(i == 53):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
        

    if(i == 54):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)

        

        #co-evolution
    if(i == 55):
       evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[RandomAttackStrategy(),DegreeAttackStrategy(),BetweennessAttackStrategy()],defender_strategies=[RandomAttachment(),PreferentialAttachment(),BalancedReplenishment()],double_strategy=False)
       
       
    if(i == 56):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 57):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 58):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[BetweennessAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 59):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 60):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 61):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[DegreeAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

           
        
    if(i == 62):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[RandomAttachment()],double_strategy=False)

           
        
    if(i == 63):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[PreferentialAttachment()],double_strategy=False)

           
        
    if(i == 64):
        evolution_manager = EvolutionManager(AttackerAgent, Defender, 100, 150,fitness=fitness_function1, pop_size=500, 
                                     generation_count=1500,offspring=2, mutation_rate=0.05,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="",attacker_resources=3,defender_resources=6,
                                     attacker_strategies=[RandomAttackStrategy()],defender_strategies=[BalancedReplenishment()],double_strategy=False)

    
    evolution_manager.run(True)  


