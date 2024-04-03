import numpy as np
import random

class Qubit:
    def __init__(self, alpha=1, beta=0):
        self.alpha = alpha
        self.beta = beta
        self.normalize()

    def normalize(self):
        norm_squared = abs(self.alpha)**2 + abs(self.beta)**2
        norm = np.sqrt(norm_squared) if norm_squared != 0 else 1  # Ensure non-zero norm
        self.alpha /= norm
        self.beta /= norm


    @property
    def state(self):
        return np.array([self.alpha, self.beta])

    def __str__(self):
        return f"|0⟩: {self.alpha}, |1⟩: {self.beta}"

    # Define a function to perform measurement and state collapse
    def measure_and_collapse(qubit):
        # Calculate the probabilities of measuring |0⟩ and |1⟩ states
        prob_0 = abs(qubit.alpha) ** 2
        prob_1 = abs(qubit.beta) ** 2
        
        # Perform a random measurement based on the probabilities
        outcome = np.random.choice([0, 1], p=[prob_0, prob_1])
        
        # Collapse the qubit state based on the measurement outcome
        if outcome == 0:
            qubit.alpha = 1
            qubit.beta = 0
        else:
            qubit.alpha = 0
            qubit.beta = 1
        
        # Return the measurement outcome
        return outcome

# Example usage

