'''
Created on Jun 11, 2013

@author: dmasad
'''

import random
import networkx as nx


from networkx.readwrite import json_graph

import copy

import json


class RunManager(object):
    '''
    The object that manages a single run of the model.
    '''

    def __init__(self, attacker, defender, num_iterations, fitness, 
                 node_count, edge_count, initial_graph, generation,identif,self_assembly_graph=True, instant_rewire=False,attacker_resources=1,defender_resources=1,file_path="",file_name_appendix=""):
        '''
        Create a new Run Manager.
        
        Args:
            attacker: An Attacker instance
            defender: Defender instance
            num_iterations: The number of iterations for them to compete for.
            fitness: A function computing the network metric used as fitness.
            node_count: How many nodes the network has.
            edge_count: How many edges the network (initially) has
            initial_graph: An external graph to be used as initial graph of attack/rewire
            self_assembly_graph: If True, the build of the graph is done by the defender otherwise a valid graph must be provided (previous parameter) 
            instant_rewire: If True, the fitness is not recomputed until the 
                            network finishes rewiring.
            attacker_resources: number of nodes that can be removed by the attacker in each round
            defender_resources: number of nodes that can be rewired by the defender in each round
            file_name_appendix: the file name for the json/gephi file is modified with the respective string, if this parameter is set 
            file_path: optional path that you can specify - the jason/gephi output files are written there. 
        '''
        
        self.attacker = attacker
        self.defender = defender
        self.node_count = node_count
        self.initial_edges = edge_count
        self.nodes_lost_edges = None # Nodes with disconnected edges
        self.instant_rewire = instant_rewire
        self.self_assembly_graph = self_assembly_graph
        self.node_distribution =[]
        self.attacker_resources = attacker_resources
        self.defender_resources = defender_resources
        self.removed_nodes = []
        self.file_path=file_path
        self.file_name_appendix=file_name_appendix
        self.current_fitness=0
        
        self.gephi_out=False
    
        self.num_iterations = num_iterations # Number of iterations per round
        
        if self_assembly_graph:
            self.G = nx.Graph()
            self.currentGraph = copy.deepcopy(self.G)
        else:
            self.G = initial_graph
            self.currentGraph = copy.deepcopy(initial_graph)
        
        self.G.add_nodes_from(range(node_count))
        self.fitness = fitness # fitness function
        self.fitness_per_round = []
        self.jsonRunParam = {}
        
        self.currentGeneration =generation
        self.currentId=identif
        
        
        self.initialNetwork = nx.Graph()
        
        
    def run(self):
        '''
        Run the run to completion, and return the network fitness series.
        '''
        if self.self_assembly_graph:
            self.build_initial_network() 
        new_fitness = self.fitness(self.G)
        self.fitness_per_round.append(new_fitness)
        self.round=-1
        self.writeGephi(0)
        
        for self.round in range(self.num_iterations):
            self.attack_network()
            self.currentGraph = self.rewire_network()
            #self.writeRoundByRoundJson(round,self.currentGraph)
            

        
        # Pleaceholder for aggregating fitness per round:
        total_fitness = 0
        for f in self.fitness_per_round:
            total_fitness += f
        total_fitness /= (1.0 * len(self.fitness_per_round))
        self.current_fitness=total_fitness
        return total_fitness
    
    def get_current_fitness(self):
        return self.current_fitness
    
    def build_initial_network(self):
        '''
        The defender initiates the network.
        '''
        for i in range(self.initial_edges):
            node = random.choice(self.G.nodes()) # Pick a random starting node
            new_edge = self.defender.rewire([node], self.G)
            self.G.add_edges_from(new_edge)
            
        self.initialNetwork = copy.deepcopy(self.G)
       
            
    
    def attack_network(self):
        '''
        The attacker picks a node to remove, and its neighbors are stored.
        '''
        self.attacked_nodes=[]
        '''
        No node has lost a neighbor in the beginning, we therefore set the
        respective value in the dictionary to 0 for all nodes
        ''' 
        #(key, value) for (key, value) in sequence
        self.nodes_lost_edges=dict((x,0) for x  in self.G.nodes())
        
        '''
        We attack the network as many times as our resources allow
        In case that a node is removed that lost neighbors,
        we set the number of edges lost to 0
        '''
        for i in range(self.attacker_resources):
            a=self.attacker.which_node_to_attack(self.G)  
            
            lost_neighbors=self.G.neighbors(a)
            for n in lost_neighbors:
                self.nodes_lost_edges[n]=self.nodes_lost_edges[n]+1
            self.nodes_lost_edges[a]=0
            self.G.remove_node(a)
            self.attacked_nodes.append(a)
    
    def rewire_network(self):
            '''
            The defender rewires the network.
            '''
            edges_to_rewire=[]
            rewiring=-1
            self.writeGephi(rewiring)
            
            self.G.add_nodes_from(self.attacked_nodes)
            '''
            first rewire edges of nodes
            that were removed from the network            
            '''
            budget=self.defender_resources
            while budget>0 and len(self.attacked_nodes)>0:
                node_to_rewire=self.attacked_nodes.pop()
                edges_to_rewire=self.defender.rewire([node_to_rewire], self.G)
                self.G.add_edges_from(edges_to_rewire)
                new_fitness = self.fitness(self.G)
                self.fitness_per_round.append(new_fitness)
                budget=budget-1
                rewiring+=1
                self.writeGephi(rewiring)
                
            if budget <= 0:
                return self.G     
                
            '''
            Create a random list from the nodes that lost edges
            in the previous attack
            '''
            list_nodes_lost_edges=[]
            for node,nmb in self.nodes_lost_edges.items():
                for i in range(nmb):
                    list_nodes_lost_edges.append(node)
                    
            random.shuffle(list_nodes_lost_edges)

            while budget>0 and len(list_nodes_lost_edges)>0:
                node_to_rewire=list_nodes_lost_edges.pop()
                edges_to_rewire=self.defender.rewire([node_to_rewire], self.G)
                self.G.add_edges_from(edges_to_rewire)
                new_fitness = self.fitness(self.G)
                self.fitness_per_round.append(new_fitness)
                budget=budget-1
                rewiring+=1
                self.writeGephi(rewiring)
                
            '''
            If there are still some resources left, we start rewiring random nodes from the 
            network
            '''
            
            all_nodes_in_network=self.G.nodes()
            #random.shuffle(all_nodes_in_network)
            while budget>0 and len(all_nodes_in_network)>0:
                node_to_rewire=all_nodes_in_network.pop()
                edges_to_rewire=self.defender.rewire([node_to_rewire], self.G)
                self.G.add_edges_from(edges_to_rewire)
                new_fitness = self.fitness(self.G)
                self.fitness_per_round.append(new_fitness)
                budget=budget-1
                rewiring+=1
                self.writeGephi(rewiring)
           
            return self.G
        
    def writeGephi(self,rewiring):
        '''
        Writes network as single network file to disk
        Format: gephi gexf                
        '''
        if self.gephi_out:
            nx.write_gexf(self.G, str(self.file_path)+'/gephi_output/net_data_g'+str(self.currentGeneration)+"ID"+str(self.currentId)+"R"+str(self.round)+"RW"+str(rewiring)+str(self.file_name_appendix)+".gexf")
            
    def writeRoundByRoundJson (self,round,graph):
        '''
            The function that writes the round-by-round graph to a JSON file
            '''
        toBeDumpedToJsonDict = {}
        currentRoundCopy = copy.deepcopy(round)
        currentGraphCopy = copy.deepcopy(graph)
        graphDict = json_graph.node_link_data(currentGraphCopy)
        s = json.dumps(graphDict)
        toBeDumpedToJsonDict = {'generation': self.currentGeneration, 'id': self.currentId, 'round': currentRoundCopy, 'graph': s}
        with open(str(self.file_path)+'data'+str(self.file_name_appendix)+'.json', mode='a') as jsonfile:
                json.dump(toBeDumpedToJsonDict,jsonfile)
                jsonfile.write("\n")
    
    
    def getNetwok (self):
        return self.G
        
                
                
    def jsonParamSet (self,generation,id):
        '''
            The function sets the values for properties (this function is called by the EvolutionManager)
            '''
        self.currentGeneration = generation
        self.currentId = id
        
    def get_node_distribution(self):
        '''
        This function is used to update the node distribution in the network that is handled
        by this run manager
        The node distribution is printed to disk to be used for the statistical analysis of the network structure        
        '''
        helper=[float(0) for i in range(self.node_count)]
        for i in (self.node_distribution):
            for j in range(self.node_count):
                if j in i:
                    helper[j]+=float(i[j])
        
        for i in range(self.node_count):
            helper[i]/=(float(len(self.node_distribution)+0.00001))
            
        return(helper)
    
    def get_diameter(self):
        '''
        This function returns the diameter of the current network      
        It returns -1 if there is more than one component in the network  
        '''
        return len(self.G.edges())
        