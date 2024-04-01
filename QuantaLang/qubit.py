import numpy as np

class Qubit:
    def __init__(self, alpha=1, beta=0):
        self.alpha = alpha
        self.beta = beta
        self.normalize()

    def normalize(self):
        norm = (abs(self.alpha)**2 + abs(self.beta)**2)**0.5
        self.alpha /= norm
        self.beta /= norm

    @property
    def state(self):
        return np.array([self.alpha, self.beta])

    def __str__(self):
        return f"|0⟩: {self.alpha}, |1⟩: {self.beta}"
