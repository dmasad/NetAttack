from GenomeAgent import Strategy
from GenomeAgent import GenomeAgent
import networkx as nx
import random

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
            
class Weights(object):
    
    def __init__(self,weights,oweights):
        self.weights=weights
        self.oweights=oweights
        
    def get_weights(self):
        return self.weights
    
    def get_oweights(self):
        return self.oweights

class PreferentialAttachment(Strategy):
    '''
    Assign attack weights at random.
    '''
    
    def run(self, graph, all_disconnected_nodes,a1,a2,node=None):
        '''
        Assign weight to node depending on degree
	'''
        weights = {}
        oweights={}
        nmbEdges = len(graph.edges())
                        
        for node in all_disconnected_nodes:
            
            if nmbEdges==0:
                metric=0
            else:
                metric=((float)(graph.degree(node)) / (float)(2*nmbEdges))
            #print "node: ",node," metric: ",d
            weights[node] = a1 * metric
            oweights[node] = a2 * (1-metric)
        
        return Weights(weights,oweights)

class RandomAttachment(Strategy):
    '''
    Assign attack weights at random.
    '''
    
    def run(self, graph, all_disconnected_nodes,a1,a2,node=None):
        '''
        Assign weight to node depending on degree
    '''
        weights = {}
        oweights={}
        
        r=random.random()
        random_weights={}
        sum=0

        #create random weights for all nodes
        for nodes in all_disconnected_nodes:
            r=random.random()
            weights[nodes] = a1*r
            oweights[nodes] =  a2*(1-r)
        
        return Weights(weights,oweights)
    
class AssortativeAttachment(Strategy):
    '''
    Assign attack weights at random.
    '''
    
    def run(self, graph, all_disconnected_nodes,a1,a2,node=None):
        '''
        Assign weight to node depending on degree
    '''
        weights = {}
        oweights={}
        
        
        #calculate maximum and minimum degrees of nodes
        #use it for calculating assortativity
        actD=(float)(graph.degree([node])[node])

        #degrees of all nodes in the network
        nodeDegreesDict=graph.degree()
        nodeDegrees=nodeDegreesDict.values()
        
        
        #maximum degree of all nodes in the network
        maxD=max(nodeDegrees)
        
        #minimum degree of all nodes in the network
        minD=min(nodeDegrees)
        
        #calculate difference between maximum and minimum degree
        #if all nodes are of the same degree,
        #set distance to 1 (division below)
        dist_max_min=(maxD-minD)   
        if(dist_max_min==0):
            dist_max_min=1     
        
        dist_max_min=(float)(dist_max_min)
        
        #calculate similarity of nodes based on their degrees
        for nodes in all_disconnected_nodes:
           
           
            metric=abs((float)(nodeDegreesDict[nodes])-actD) 
            metric= metric / (dist_max_min)               
            weights[nodes]=a1*metric
            oweights[nodes]=a2*(1-metric)
            
        return Weights(weights,oweights)    

class DistanceAttachment(Strategy):
    '''
    Assign attack weights at random.
    '''
    
    def run(self, graph, all_disconnected_nodes,a1,a2,node=None):
        '''
        Assign weight to node depending on degree
    '''
        weights = {}
        oweights={}
        
        
        #calculate maximum and minimum degrees of nodes
        #use it for calculating assortativity
        
        d=len(graph.nodes())
        if nx.is_connected(graph):
            d=nx.diameter(graph)
        
       
        #calculate similarity of nodes based on their degrees
        for nodes in all_disconnected_nodes:
            if nx.has_path(graph,node,nodes):
                metric=nx.shortest_path_length(graph, node, nodes)/(d)
            else:
                metric=1

            weights[nodes]=a1*(1-metric)
            oweights[nodes]=a2*(metric)
            
        return Weights(weights,oweights)   
    
    
class ConnectedAttachment(Strategy):
    '''
    Assign attack weights at random.
    '''
    
    def run(self, graph, all_disconnected_nodes,a1,a2,node=None):
        '''
        Assign weight to node depending on degree
    '''
        weights = {}
        oweights={}
        
        
        #calculate maximum and minimum degrees of nodes
        #use it for calculating assortativity
     
        #calculate similarity of nodes based on their degrees
        for nodes in all_disconnected_nodes:
            if nx.has_path(graph,node,nodes):
                metric=0
            else:
                metric=1

            weights[nodes]=a1*(1-metric)
            oweights[nodes]=a2*(metric)
            
        return Weights(weights,oweights)   


class Defender(object):
    
    def __init__(self,genome=None):
       
        self.strategies = [PreferentialAttachment(),RandomAttachment(),AssortativeAttachment(),DistanceAttachment(),ConnectedAttachment()]
        
        if(genome==None):
            #self.genome=[1,0,0,0,0,0,0,0]
            self.genome=[]
            for i in range(len(self.strategies)*2):
                self.genome.append(random.random()*100)
            #print self.genome
        else:
            self.genome=genome
        
    def get_genome(self):
        return self.genome
    
    
    def rewire(self, nodes, graph):
        '''
        Rewire the nodes in the graph.
        Args:
        nodes: a list of nodes to be rewired.
        graph: the graph within which the nodes are to be rewired.
        '''
        new_edges = []
        
        for node in nodes:
            
            #get connected nodes
            
            connected_nodes=graph.neighbors(node)
            #get all nodes
            all_disconnected_nodes=graph.nodes()
            
            #remove connected nodes from all nodes
            for i in connected_nodes:
                all_disconnected_nodes.remove(i)
            
            all_disconnected_nodes.remove(node)
            
            # Initiate weights
            connect_weights = {}
            for candidate_node in graph.nodes():
                connect_weights[candidate_node] = 0
                # Apply strategies
            i=0
            for strategy in self.strategies:
                strategy_weights = strategy.run(graph, all_disconnected_nodes,self.genome[i],self.genome[i+1],node)
                i+=2
                w=strategy_weights.get_weights()
                wo=strategy_weights.get_oweights()
                try:
                    for candidate_node in w:
                        connect_weights[candidate_node] += w[candidate_node]
                    for candidate_node in wo:
                        connect_weights[candidate_node] += wo[candidate_node]
                except:
                    print "error"
                    # Pick a connection
                    
            wc=True
            #while(wc):
            target_node = weighted_random(connect_weights)
            #    wc=(graph.has_edge(node,target_node) or target_node==node)
                
            new_edges.append((node, target_node))
            #print "Connecting", node, "to", target_node
        
        return new_edges
                

# ------------
# TESTING TOOLS
# -------------



class StupidDefender(Defender):
    '''
    A Defender agent class which only uses Preferential attachement.
    '''
    
    def __init__(self,genome=None):
       
        self.strategies = [PreferentialAttachment()]
        
        if(genome==None):
            #self.genome=[1,0,0,0,0,0,0,0]
            self.genome=[]
            for i in range(len(self.strategies)*2):
                self.genome.append(random.random()*100)
            #print self.genome
        else:
            self.genome=genome
         
                
       
        
