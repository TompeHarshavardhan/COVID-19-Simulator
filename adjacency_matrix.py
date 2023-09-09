import numpy as np

class AdjacencyMatrix:
    def __init__(self, num_nodes):
        self.matrix = np.zeros((num_nodes, num_nodes))

    def add_edge(self, i, j):
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def remove_edge(self, i, j):
        self.matrix[i][j] = 0
        self.matrix[j][i] = 0

    def get_neighbors(self, node):
        return [i for i, x in enumerate(self.matrix[node]) if x]