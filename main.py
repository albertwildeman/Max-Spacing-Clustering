from FileReadLib import get_array
from MaxSpacingClusteringLib import max_spacing_clustering_expl
from MaxSpacingClusteringLib import max_spacing_clustering_impl

# Run small case
small_edge_set = get_array("clustering1")
max_spacing_small = max_spacing_clustering_expl(small_edge_set, 4)
print("Minimal max-spacing 4-k clustering: " + str(max_spacing_small))

# Run test for large case
large_node_set = get_array("clustering_testbig")
max_spacing_large = max_spacing_clustering_impl(large_node_set, 2)
print("Max k clusters for spacing 3: " + str(max_spacing_large))

# Run large case
large_node_set = get_array("clustering_big")
max_spacing_large = max_spacing_clustering_impl(large_node_set, 3)
print("Minimal max-spacing 4-k clustering: " + str(max_spacing_large))
