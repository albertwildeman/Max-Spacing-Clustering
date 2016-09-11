import numpy as np

class UnionFind(object):

    def __init__(self, size):
        self.size = size
        self.leaders = np.array(range(size))
        self.cluster_sizes = np.ones(size)

    def union(self, i_point_a, i_point_b):
        if self.cluster_sizes[i_point_b] > self.cluster_sizes[i_point_a]:
            # Set leaders of points that currently have leader of point a to leader of point b
            self.leaders[self.leaders == self.leaders[i_point_a]] = self.leaders[i_point_b]
        else: # opposite case
            # Set leaders of points that currently have leader of point b to leader of point a
            self.leaders[self.leaders == self.leaders[i_point_b]] = self.leaders[i_point_a]

    def find(self, i_point):
        return self.leaders[i_point]
