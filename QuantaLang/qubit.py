class Qubit:
    def __init__(self,alpha,beta):
        self.alpha = alpha
        self.beta = beta

    

    def neg_valid(self,alpha,beta):
        if self.alpha <0 or self.beta < 0:
            raise ValueError("Probabilty Amplitudes cannot be negative")
        
    def __str__(self):
        return f"Qubit(alpha={self.alpha}, beta={self.beta})"