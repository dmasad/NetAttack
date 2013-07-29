import networkx as nx
import matplotlib.pyplot as plt

import numpy as np
from scipy.interpolate import interp1d

from DefenderAgent import Defender
from DefenderAgent import Defender1
from AttackerAgent import AttackerAgent

from EvolutionManager import EvolutionManager

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

def fitness_function2(graph,penalty=20):
    diameter=0
    if nx.is_connected(graph):
        diameter=nx.average_shortest_path_length(graph)/penalty
    else:
        diameter=1
        
    return diameter

def effective_diameter(graph, q=0.9):
    '''
    Compute the effective diameter for the target percentile q
    Better than diameter for dealing with long tails and disconnected graphs.

    via Leskovec et al.
    '''

    # Build a distance matrix:
    nodes = graph.nodes()
    dist = nx.shortest_path_length(graph)
    distances = []
    for node1 in nodes:
        row = []
        for node2 in nodes:
            if node1 == node2:
                row.append(np.inf)
            elif node2 in dist[node1]:
                row.append(dist[node1][node2])
            else:
                row.append(np.inf)
        distances.append(row)

    distances = np.array(distances)

    g_d = [0] # g(d) in Leskovec et al.
    d = 1

    distances = distances[distances != np.inf]
    total_dyads = distances.size

    while g_d[-1] < q:
        path_counts = len(distances[distances<=d])
        path_frac = path_counts/total_dyads
        g_d.append(path_frac)
        d += 1


    # Interpolate
    d_range = range(d)
    interpolation = interp1d(g_d, d_range, kind='linear')
    eff_d = interpolation(q)
    return float(eff_d)/len(nodes)


#for i in range(5):
i=1
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 30,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=3)
 
evolution_manager.run(True)
i+=1
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 33,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=3)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 36,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=3)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 39,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=3)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 30,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=4)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 33,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=4)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 36,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=4)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 39,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=4)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 30,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=5)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 33,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=5)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 36,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=5)
evolution_manager.run(True)
 
i+=1
 
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 39,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=2,defender_resources=5)
evolution_manager.run(True)
 
i+=1
evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 30,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=4)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 33,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=4)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 36,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=4)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 39,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=4)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 30,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=5)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 33,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=5)
evolution_manager.run(True)


i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 36,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=5)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 39,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=5)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 30,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=6)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 33,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=6)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 36,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=6)
evolution_manager.run(True)

i+=1

evolution_manager = EvolutionManager(AttackerAgent, Defender, 30, 39,fitness=fitness_function1, pop_size=100, 
                                     generation_count=150,offspring=2, mutation_rate=0.2,initial_graph=None,instant_rewire=False,output=True,file_name_appendix=i,file_path="C:/Users/jschmidt/Dropbox/csss2013CoEv/",attacker_resources=3,defender_resources=6)

evolution_manager.run(True)

i+=1


