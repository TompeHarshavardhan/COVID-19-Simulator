import numpy as np

class Graph:
    def __init__(self, num_nodes):
        self.adj_matrix = np.zeros((num_nodes, num_nodes))

    def add_edge(self, i, j):
        self.adj_matrix[i, j] = 1
        self.adj_matrix[j, i] = 1

    def remove_edge(self, i, j):
        self.adj_matrix[i, j] = 0
        self.adj_matrix[j, i] = 0

    def get_neighbors(self, node):
        return np.where(self.adj_matrix[node] == 1)[0]