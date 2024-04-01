# Quantum Logic Gates


import math
from qubit import *
from var import *
from probe import *
def hadamard(qubit_obj):
    sqrt2 = math.sqrt(2)
    alpha = (qubit_obj.alpha + qubit_obj.beta) / sqrt2
    beta = (qubit_obj.alpha - qubit_obj.beta) / sqrt2
    return Qubit(alpha, beta)

def pauli_x(qubit):
    return Qubit(qubit.beta, qubit.alpha)

def pauli_y(qubit):
    return Qubit(complex(qubit.beta.imag, -qubit.alpha.imag), complex(-qubit.beta.real, qubit.alpha.real))

def pauli_z(qubit):
    return Qubit(complex(qubit.alpha.real, -qubit.beta.imag), complex(-qubit.alpha.imag, qubit.beta.real))


a = probe.sum(3,3,3)
print(a)