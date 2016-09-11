from FileReadLib import get_array
from MaxSpacingClusteringLib import max_spacing_clustering

small_edge_set = get_array("clustering1")
large_node_set = get_array("clustering_big")

max_spacing_small = max_spacing_clustering(small_edge_set, 4)

print("Minimal max-spacing 4-k clustering: " + str(max_spacing_small))
