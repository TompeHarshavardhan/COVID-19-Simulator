import numpy as np

def generate_random_people(num_people):
    return np.random.randint(0, 2, size=num_people)

def create_network(graph, num_people):
    for i in range(num_people):
        for j in range(i+1, num_people):
            if np.random.rand() < 0.1:
                graph.add_edge(i, j)