from FileReadLib import get_array
from MaxSpacingClusteringLib import max_spacing_clustering

small_data = get_array("clustering1")

max_spacing_small = max_spacing_clustering(small_data[1], small_data[0], 4)

print("Minimal max-spacing 4-k clustering: " + str(max_spacing_small))
