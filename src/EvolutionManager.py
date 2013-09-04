'''
Created on Jun 15, 2013

@author: dmasad
'''
from time import gmtime, strftime
import random
import csv
from collections import defaultdict
import networkx as nx
from multiprocessing import Process,Queue

from RunManager import *

def weighted_random(item_dict):
    '''
    Randomly choose an item from the dictionary keys,
    with probability weights given in the dictionary values.

    Args:
        item_dict: a dictionary of the form:
            {Item: weight, Item: weight}
            where Item can be any key, and the weights are numeric.
    '''
    total = sum(item_dict.values())
    choice = random.random() * total
    counter = 0
    for key, wgt in item_dict.items():
        if choice < counter + wgt: 
            return key
        else: 
            counter += wgt

class EvolutionManager(object):
    '''
    Class to manage the entire coevolution of network and attacker agents.
    '''


    def __init__(self, Attacker, Defender, network_size, edge_count, fitness,
                 pop_size, generation_count, offspring, mutation_rate, initial_graph, instant_rewire, self_assembly_graph = True,
                 output = False,file_name_appendix="",file_path="",attacker_resources=1,defender_resources=1,attacker_strategies=None,defender_strategies=None,double_strategy=True):
        '''
        Create a new complete coevolution run.
        
        Args:
            Attacker: The Attacker class
            Defender: The Defender class
            network_size: The number of nodes in each network
            edge_count: The number of edges in each network
            pop_size: Number of attackers and defenders in each generation
            offspring: Number of offspring for each pair of agents
            generation_count: The number of generations to run for
            mutation_rate: The rate of mutation
            initial_graph: An external graph to be used as initial graph of attack/rewire
            self_assembly_graph: If True, the build of the graph is done by the defender otherwise a valid graph must be provided (previous parameter)
            instant_rewire: If True, the fitness each round of each run 
                            is not recomputed until the network finishes rewiring.
            output: if output is True, statistics on attacker, defender, and the network are written to disk
            file_name_appendix: the file name (such as attackers or defenders) of the statistics file is concatenated with this string. E.g. if file_nameappendix
                                is 1, the file is called attackers1.csv or defenders1.csv. 
            file_path: optional path that you can specify - the output files are written there. 
            attacker_resources: number of nodes that can be removed by the attacker in each round
            defender_resources: number of nodes that can be rewired by the defender in each round
            
        '''
        self.Attacker = Attacker
        self.Defender = Defender
        self.network_size = network_size
        self.edge_count = edge_count
        self.fitness = fitness
        self.pop_size = pop_size
        self.generation_count = generation_count
        self.offspring = offspring
        self.mutation_rate = mutation_rate
        self.instant_rewire = instant_rewire
        self.output = output
        self.attacker_resources=attacker_resources
        self.defender_resources=defender_resources
        self.file_path = file_path
        self.double_strategy= double_strategy
        self.defender_strategies=defender_strategies
        self.attacker_strategies=attacker_strategies
        
        self.concurrent_runs=8
       
        
        # Create the generation container
        self.current_generation = 0
        self.generations = defaultdict(lambda: {"attackers": [], "defenders": []})
        
        self.current_population = {"attackers": [], "defenders": []}
        
        
        self.currentGraph = initial_graph
        self.self_assembly_graph = self_assembly_graph
        
        self.file_name_appendix=file_name_appendix
        
        open('data.json', mode='w')
        
        
        
        
        # Create generation 0:
        for i in range(pop_size):
            new_attacker = self.Attacker(strategies=self.attacker_strategies,double_strategies=self.double_strategy)
            self.generations[0]["attackers"].append(new_attacker.get_genome())
            new_defender = self.Defender(strategies=self.defender_strategies,double_strategies=self.double_strategy)
            self.generations[0]["defenders"].append(new_defender.get_genome())
        
        # Prepare output files:
        if self.output:
            self.attacker_records_file = open(str(file_path)+"attackers"+str(file_name_appendix)+".csv", "wb")
            self.attacker_writer = csv.writer(self.attacker_records_file)
            self.attacker_writer.writerow(["Generation", "ID", "Fitness"])
            
            self.defender_records_file = open(str(file_path)+"defenders"+str(file_name_appendix)+".csv", "wb")
            self.defender_writer = csv.writer(self.defender_records_file)
            self.defender_writer.writerow(["Generation", "ID", "Fitness"])
            
            self.network_writer_file = open(str(file_path)+"network"+str(file_name_appendix)+".csv", "wb")
            self.network_writer = csv.writer(self.network_writer_file)
            
        
    
    def run(self, verbose=False):
        '''
        Runs a full evolutionary cycle.
        '''
        
        while self.current_generation < self.generation_count:
            if verbose:
                print "Run ", self.file_name_appendix," Generation ",self.current_generation
                print "time: "+strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            self.run_generation()
            self.breed_next_generation()
        
        if self.output:
            try:
                self.attacker_records_file.close()
                self.defender_records_file.close()
            except:
                pass
        
    
    def run_generation(self):
        '''
        Run one generation and get fitnesses.
        
        Pair attacker and defenders at random.
        '''
        
        attackers = range(self.pop_size)
        defenders = range(self.pop_size)
        
        runs = []
        # Prepare runs:
        i=0
        while len(attackers) > 0:
            # Pick the attacker and defender:
            i+=1
            a = attackers.pop(random.randrange(len(attackers)))
            attacker_genome = self.generations[self.current_generation]["attackers"][a]
            attacker = self.Attacker(strategies=self.attacker_strategies,double_strategies=self.double_strategy,genome=attacker_genome)
            
            
            d = defenders.pop(random.randrange(len(defenders)))
            defender_genome = self.generations[self.current_generation]["defenders"][d]
            defender = self.Defender(strategies=self.defender_strategies,double_strategies=self.double_strategy,genome=defender_genome)
            
            # Choose number of rounds at random:
            #rounds = random.randrange(5,16)
            rounds = 20
            
            # Create the Run
            run = RunManager(attacker, defender, rounds, self.fitness,
                             self.network_size, self.edge_count, self.currentGraph,self.current_generation,i, 
                             self.self_assembly_graph, self.instant_rewire,self.attacker_resources,self.defender_resources,self.file_path,self.file_name_appendix)
            
            
            runs.append(run)
        
        self.current_fitness = {"attackers": {}, "defenders": {}}
        # Execute all runs and compute fitness
        # (If parallelizing, put that here.)
        avg_fitness=0
        
        self.diameters= {"attackers": {}, "defenders": {}}
        cnt=0
        runs_ready=[]
        q = Queue()
        
        size_runs=len(runs)
        
     
        
        for ccnt_start in range(self.concurrent_runs):
            p = Process(target=run_function, args=(runs[ccnt_start], q,))
            p.start()
            # ps.append(p)
            print "process " + str(ccnt_start) + " started"
   
             
        
        for ccnt in range(self.concurrent_runs,size_runs):
            r=q.get()
            runs_ready.append(r)
            p = Process(target=run_function, args=(runs[ccnt],q,))
            p.start()
            print "process "+ str(ccnt)+" started"
        
        for ccnt_end in range(self.concurrent_runs):
            r=q.get()  
            runs_ready.append(r)    
 
        for cnt in range(len(runs_ready)):   
            run=runs_ready[cnt]           
            fitness = run.get_current_fitness()
            node_distribution = run.get_node_distribution()
            self.network_writer.writerow([self.current_generation]+node_distribution) 
            k_a=[]
            k_a.append(cnt)
            k_a.extend(run.attacker.get_genome())
            
            k_d=[]
            k_d.append(cnt)
            k_d.extend(run.defender.get_genome())
            
            
            self.current_fitness["attackers"][tuple(k_a)] = fitness
            #print self.current_fitness["attackers"]
            self.current_fitness["defenders"][tuple(k_d)] = (1 - fitness)
            self.diameters["attackers"][tuple(k_a)]=run.get_diameter()
            self.diameters["defenders"][tuple(k_d)]=run.get_diameter()
            
            avg_fitness+=fitness
        
        #print "cnt"+str(cnt)
        #print "len"+str(len(self.current_fitness["attackers"]))
            
        print "avg fitness attacker",avg_fitness/cnt
        print "time: "+strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            
        # File output:
        if self.output:
            i = 0
            for genome, fitness in self.current_fitness["attackers"].items():
                diameter=self.diameters["attackers"][genome]
                l=list(genome)
                l.pop(0)
                row = [self.current_generation, i, fitness,diameter] + l
                self.attacker_writer.writerow(row)
                i += 1
            
           
            
            i = 0
            for genome, fitness in self.current_fitness["defenders"].items():
                diameter=self.diameters["defenders"][genome]
                l=list(genome)
                l.pop(0)
                row = [self.current_generation, i, fitness,diameter] + l
                self.defender_writer.writerow(row)
                i += 1
                
            
         
         
                
            
        
    def breed_next_generation(self):
        '''
        Take the previous generation's fitness and create a new generation.
        '''
        
        self.current_generation += 1
        
        # Breed attackers:
        for breed in ["attackers", "defenders"]:
        
            while len(self.generations[self.current_generation][breed]) < self.pop_size:
                # Pick two parents
                parent1 = list(weighted_random(self.current_fitness[breed]))
                parent2 = list(weighted_random(self.current_fitness[breed]))
                parent1.pop(0)
                parent2.pop(0)
                for i in range(self.offspring):
                    child = self.crossover(parent1, parent2)
                    child = self.mutate(child)
                    self.generations[self.current_generation][breed].append(child)                
    
    
    def load_data(self, attacker_file, defender_file, generation):
        '''
        Load genomes from previous attacker and defender files previously created. 
        '''
        # Load attackers:
        f = open(attacker_file)
        for row in f:
            row = row.split(",")
            try:
                if int(row[0]) != generation: continue
            except:
                continue
            else:
                genome = [float(g) for g in row[3:]]
                self.generations[generation]["attackers"].append(genome)
        f.close()
        
        # Load defenders
        f = open(defender_file)
        for row in f:
            row = row.split(",")
            try:
                if int(row[0]) != generation: continue
            except: 
                continue
            else:
                genome = [float(g) for g in row[3:]]
                self.generations[generation]["defenders"].append(genome)
        f.close()
        
        self.current_generation = generation
            
    
    # -----------------
    # Genetic functions
    # -----------------
       
    def crossover(self, genome1, genome2):
        '''
        Cross over two genomes at a random point.
        '''
        cross_pt = random.randrange(len(genome1))
        return genome1[:cross_pt] + genome2[cross_pt:]
    
    def mutate(self, genome):
        '''
        Mutates a genome at random.
        '''
        new_genome = []
        for gene in genome:
            if random.random() < self.mutation_rate:
                # Mutate:
                gene = random.gauss(gene, 5)
                if gene < 0: gene = 0
                if gene > 100: gene = 100
            new_genome.append(gene)
        return new_genome
            
            
        
class SingleEvolutionManager(EvolutionManager):
    '''
    Class to manage the evolution of a network against a fixed fitness function.
    '''

    def __init__(self, Defender,
                 network_size, edge_count, fitness,
                 pop_size, generation_count, offspring, mutation_rate,
                 output = False):
        '''
        Create a new complete evolution run.
        
        Args:
            Defender: The Defender class
            network_size: The number of nodes in each network
            edge_count: The number of edges in each network
            pop_size: Number of attackers and defenders in each generation
            offspring: Number of offspring for each pair of agents
            generation_count: The number of generations to run for
            mutation_rate: The rate of mutation
            instant_rewire: If True, the fitness each round of each run 
                            is not recomputed until the network finishes rewiring.
        '''
        self.Defender = Defender
        self.network_size = network_size
        self.edge_count = edge_count
        self.fitness = fitness
        self.pop_size = pop_size
        self.generation_count = generation_count
        self.offspring = offspring
        self.mutation_rate = mutation_rate
        self.output = output
        
        # Create the generation container
        self.current_generation = 0
        self.generations = defaultdict(list)
        
        self.current_population = []
        
        # Create generation 0:
        for i in range(pop_size):
            new_defender = self.Defender()
            self.generations[0].append(new_defender.get_genome())
        
        # Prepare output files:
        if self.output:
            self.defender_records_file = open("defenders" + self.output + ".csv", "wb")
            self.defender_writer = csv.writer(self.defender_records_file)
            self.defender_writer.writerow(["Generation", "ID", "Fitness"])
        

    
    def run_generation(self):
        '''
        Run one generation and get fitnesses.
        
        Pair attacker and defenders at random.
        '''
        self.current_fitness = {}
        
        for genome in self.generations[self.current_generation]:
            # Build the network and evaluate:
            defender = self.Defender(genome)
            # Build the network:
            G = nx.Graph()
            G.add_nodes_from(range(self.network_size))
            for i in range(self.edge_count):
                node = random.choice(G.nodes()) # Pick a random starting node
                new_edge = defender.rewire([node], G)
                G.add_edges_from(new_edge)
            # Measure fitness:
            self.current_fitness[tuple(defender.get_genome())] = self.fitness(G)

        # File output:
        if self.output:
            i = 0
            for genome, fitness in self.current_fitness.items():
                row = [self.current_generation, i, fitness] + list(genome)
                self.defender_writer.writerow(row)
                i += 1
        
    
            
        
    def breed_next_generation(self):
        '''
        Take the previous generation's fitness and create a new generation.
        '''
        
        self.current_generation += 1
        
        # Breed attackers:        
        while len(self.generations[self.current_generation]) < self.pop_size:
            # Pick two parents
            parent1 = list(weighted_random(self.current_fitness))
            parent2 = list(weighted_random(self.current_fitness))
            for i in range(self.offspring):
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                self.generations[self.current_generation].append(child)
     
    
def run_function(run,q):
    run.run()        
    q.put(run)    
        
        
