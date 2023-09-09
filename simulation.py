import numpy as np
from SIR_algorithm import SIR
from priority_queue import PriorityQueue
from graph import Graph

class Simulation:
    def __init__(self):
        self.SIR = SIR(0.1, 0.01)
        self.queue = PriorityQueue()
        self.graph = Graph(1000)

    def run(self):
        S, I, R = 999, 1, 0
        self.queue.put(0, 0)
        while not self.queue.empty():
            current = self.queue.get()
            for neighbor in self.graph.get_neighbors(current):
                if np.random.rand() < self.SIR.beta:
                    self.queue.put(neighbor, 1)
            S, I, R = self.SIR.update(S, I, R)
            print('S: {}, I: {}, R: {}'.format(S, I, R))