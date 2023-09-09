import numpy as np

class SIR:
    def __init__(self, beta, gamma):
        self.beta = beta
        self.gamma = gamma

    def update(self, S, I, R):
        dS = -self.beta * S * I
        dI = self.beta * S * I - self.gamma * I
        dR = self.gamma * I
        return dS, dI, dR