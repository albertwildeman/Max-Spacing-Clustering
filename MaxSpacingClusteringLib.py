from UnionFindLib import UnionFind

import numpy as np

def max_spacing_clustering(edges, n_nodes, k):

    print("subtract 1 from node numbers?")

    # Sort edges in order of length
    edge_order = np.argsort(edges[:, 2])
    edge_nodes = edges[edge_order, :2]
    edge_lengths = edges[edge_order, 2]

    # Initialize Union-Find to hold clustering information
    uf = UnionFind[n_nodes]

    for i_edge in range(n_nodes-k):


        if uf.find(i_edge_a) == uf.find(i_edge_b): # if adding this edge would not create a cycle, add it
            pass



    return 0