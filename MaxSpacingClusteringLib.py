from UnionFindLib import UnionFind

import numpy as np

def max_spacing_clustering_expl(edges, k):

    # Sort edges in order of length
    edge_order = np.argsort(edges[:, 2])
    edge_nodes = edges[edge_order, :2]
    edge_lengths = edges[edge_order, 2]

    # Rename nodes to start at 0
    node_namebase = edge_nodes.min()
    edge_nodes -= node_namebase

    # Get number of nodes
    n_nodes = edge_nodes.max() + 1

    # Initialize number of clusters to number of nodes
    n_clusters = n_nodes

    # Initialize Union-Find to hold clustering information
    uf = UnionFind(n_nodes)

    i_edge = 0
    while n_clusters > k:

        i_node_a = edge_nodes[i_edge, 0]
        i_node_b = edge_nodes[i_edge, 1]

        if uf.find(i_node_a) != uf.find(i_node_b):  # if adding this edge would not create a cycle, add it
            uf.union(i_node_a, i_node_b)
            n_clusters -= 1

        i_edge += 1

    if len(np.unique(uf.leaders)) != k:  # Check the right number of clusters was created
        raise Exception("The wrong number of clusters was created.")

    # The max spacing of a k-clustering on this dataset is the length of the next shortest edge
    # that would not create a cycle
    found_max_spacing = False
    while not found_max_spacing:

        i_node_a = edge_nodes[i_edge, 0]
        i_node_b = edge_nodes[i_edge, 1]

        if uf.find(i_node_a) != uf.find(i_node_b):  # if adding this edge would not create a cycle
            max_spacing = edge_lengths[i_edge]
            found_max_spacing = True

        i_edge += 1

    return max_spacing

def max_spacing_clustering_impl(nodes, spacing):


    # remove duplicates from list of nodes
    nodes = np.unique(nodes)

    # Get number of nodes
    n_nodes = len(nodes)

    # Initialize number of clusters to number of nodes
    n_clusters = n_nodes

    # get number of bits
    n_bits = int(np.ceil((np.log2(max(nodes)))))

    # Create a numpy array to hold, for each possible value (converted to int) of a node, what the index of that
    # node is in "nodes" (or multiple).
    node_indices = [[] for x in range(2**n_bits)]
    for i_node in range(n_nodes):
        node_indices[nodes[i_node]].append(i_node)

    # Initialize Union-Find to hold clustering information
    uf = UnionFind(n_nodes)

    # As there are too many edges to sort, simply start by going through all edges of length 1, then 2, etc.
    # up to the spacing required minus one.

    for edge_length in range(1, spacing):
        for i_node_a in range(n_nodes):

            if i_node_a%1000==0:
                print("working on node #" + str(i_node_a))

            if edge_length == 1:
                for i_bit_to_flip_1 in range(n_bits):
                    node_b = nodes[i_node_a] ^ (1 << i_bit_to_flip_1)
                    for i_node_b in node_indices[node_b]:
                        if uf.find(i_node_a) != uf.find(i_node_b):  # if adding this edge would not create a cycle,
                            uf.union(i_node_a, i_node_b)
                            n_clusters -= 1

            if edge_length == 2:
                for i_bit_to_flip_1 in range(n_bits):
                    for i_bit_to_flip_2 in [i for i in range(n_bits) if i!=i_bit_to_flip_1]:
                        node_b = nodes[i_node_a] ^ ( (1 << i_bit_to_flip_1) ^ (1 << i_bit_to_flip_2))

                        for i_node_b in node_indices[node_b]:
                            if i_node_b > -1:  # if this node exists
                                if uf.find(i_node_a) != uf.find(i_node_b):  # if adding this edge would not create a cycle,
                                    uf.union(i_node_a, i_node_b)
                                    n_clusters -= 1

    return n_clusters
