from itertools import islice

import networkx as nx
import numpy as np

def yen(matrix, paths):

    #   matrix:  np.matrix  --> Adjacency matrix
    #   paths=  int    --> number of paths to be returned

    #   returns a list of the paths-number of shortest path in the graph

    G = nx.from_numpy_matrix(matrix)

    def k_shortest_paths(G, source, target, k, weight=None):
        return list(islice(nx.shortest_simple_paths(G, source, target, weight='weight'), k))

    return k_shortest_paths(G, list(G)[0], list(G)[len(list(G))-1], paths)