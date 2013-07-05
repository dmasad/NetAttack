'''
Created on Jun 15, 2013

@author: dmasad
'''
import random
import csv
from collections import defaultdict

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
                 output = False):
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
        
        # Create the generation container
        self.current_generation = 0
        self.generations = defaultdict(lambda: {"attackers": [], "defenders": []})
        
        self.current_population = {"attackers": [], "defenders": []}
        
        
        self.currentGraph = initial_graph
        self.self_assembly_graph = self_assembly_graph
        
        open('data.txt', mode='w')
        
        
        
        
        # Create generation 0:
        for i in range(pop_size):
            new_attacker = self.Attacker()
            self.generations[0]["attackers"].append(new_attacker.get_genome())
            new_defender = self.Defender()
            self.generations[0]["defenders"].append(new_defender.get_genome())
        
        # Prepare output files:
        if self.output:
            self.attacker_records_file = open("attackers.csv", "wb")
            self.attacker_writer = csv.writer(self.attacker_records_file)
            self.attacker_writer.writerow(["Generation", "ID", "Fitness"])
            
            self.defender_records_file = open("defenders.csv", "wb")
            self.defender_writer = csv.writer(self.defender_records_file)
            self.defender_writer.writerow(["Generation", "ID", "Fitness"])
            
        
    
    def run(self, verbose=False):
        '''
        Runs a full evolutionary cycle.
        '''
        
        while self.current_generation < self.generation_count:
            if verbose:
                print "Running generation", self.current_generation
            self.run_generation()
            self.breed_next_generation()
        
        if self.output:
            self.attacker_records_file.close()
            self.defender_records_file.close()
        
    
    def run_generation(self):
        '''
        Run one generation and get fitnesses.
        
        Pair attacker and defenders at random.
        '''
        
        attackers = range(self.pop_size)
        defenders = range(self.pop_size)
        
        runs = []
        j=0
        # Prepare runs:
        while len(attackers) > 0:
            # Pick the attacker and defender:
            a = attackers.pop(random.randrange(len(attackers)))
            attacker_genome = self.generations[self.current_generation]["attackers"][a]
            attacker = self.Attacker(genome=attacker_genome)
            
            
            d = defenders.pop(random.randrange(len(defenders)))
            defender_genome = self.generations[self.current_generation]["defenders"][d]
            defender = self.Defender(genome=defender_genome)
            
            # Choose number of rounds at random:
            #rounds = random.randrange(5,16)
            rounds = 10
            # Create the Run
            run = RunManager(attacker, defender, rounds, self.fitness,
                             self.network_size, self.edge_count, self.currentGraph, self.self_assembly_graph, self.instant_rewire)
            
            runs.append(run)
        
        self.current_fitness = {"attackers": {}, "defenders": {}}
        # Execute all runs and compute fitness
        # (If parallelizing, put that here.)
        for run in runs:
            
            ##set the parameters required to create the JSON dictionary
            run.jsonParamSet(self.current_generation,j)
            j +=1
            
            fitness = run.run()
            self.current_fitness["attackers"][tuple(run.attacker.get_genome())] = fitness
            self.current_fitness["defenders"][tuple(run.defender.get_genome())] = (1 - fitness)
        
        # File output:
        if self.output:
            i = 0
            for genome, fitness in self.current_fitness["attackers"].items():
                row = [self.current_generation, i, fitness] + list(genome)
                self.attacker_writer.writerow(row)
                i += 1
            
            i = 0
            for genome, fitness in self.current_fitness["defenders"].items():
                row = [self.current_generation, i, fitness] + list(genome)
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
                #print parent1
                #print parent2

                for i in range(self.offspring):
                    child = self.crossover(parent1, parent2)
                    child = self.mutate(child)
                    self.generations[self.current_generation][breed].append(child)           
    
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
    
    