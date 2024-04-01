# Quantum Logic Gates


import math
from qubit import *
import numpy as np
from var import *
from probe import *
def hadamard(qubit_obj):
    sqrt2 = math.sqrt(2)
    alpha = (qubit_obj.alpha + qubit_obj.beta) / sqrt2
    beta = (qubit_obj.alpha - qubit_obj.beta) / sqrt2
    return Qubit(alpha, beta)

def pauli_x(qubit):
    x_matrix = np.array([[0, 1],
                         [1, 0]])
    new_state = np.dot(x_matrix, qubit.state)
    state_str = f"|0⟩: {new_state[0].real}, |1⟩: {new_state[1].real}"
    
    return Qubit(new_state[0], new_state[1])

def pauli_y(qubit):
    y_matrix = np.array([[0, -1j],
                         [1j, 0]])
    new_state = np.dot(y_matrix, qubit.state)
    state_str = f"|0⟩: {new_state[0].real}, |1⟩: {new_state[1].real}"
    
    return Qubit(new_state[0], new_state[1])
    # return Qubit(complex(qubit.beta.imag, -qubit.alpha.imag), complex(-qubit.beta.real, qubit.alpha.real))

def pauli_z(qubit):
    z_matrix = np.array([[1, 0],
                         [0, -1]])
    new_state = np.dot(z_matrix, qubit.state)
    state_str = f"|0⟩: {new_state[0].real}, |1⟩: {new_state[1].real}"
    
    return Qubit(new_state[0], new_state[1])
    # return Qubit(complex(qubit.alpha.real, -qubit.beta.imag), complex(-qubit.alpha.imag, qubit.beta.real))


def phase_gate(qubit):
    s_matrix = np.array([[1, 0],
                         [0, 1j]])
    new_state = np.dot(s_matrix, qubit.state)
    state_str = f"|0⟩: {new_state[0].real}, |1⟩: {new_state[1].real}"
    
    return Qubit(new_state[0], new_state[1])


def cnot_gate(qubit):
    # Apply the CNOT gate operation
    if qubit.alpha == 1:
        # If the control qubit is |1⟩, flip the state of the target qubit
        new_target_state = 1 - qubit.beta
    else:
        # If the control qubit is |0⟩, leave the target qubit unchanged
        new_target_state = qubit.beta
    
    return new_target_state
# print(pauli_x(Qubit(1, 0)))
# print(pauli_y(Qubit(1, 0)))
# print(pauli_z(Qubit(1, 0)))