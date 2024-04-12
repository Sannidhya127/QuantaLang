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


# Define the CNOT gate function
def cnot_gate(control, target):
    # Apply the CNOT gate operation
    if control == 1:
        # If the control qubit is in state |1⟩, flip the state of the target qubit
        target = 1 - target
    # Return the resulting state of the target qubit
    return target


def t_gate(qubit):
    # Define the T gate matrix
    t_matrix = np.array([[1, 0],
                         [0, np.exp(1j * np.pi / 4)]])
    
    # Apply the T gate operation to the qubit
    new_state = np.dot(t_matrix, qubit.state)
    
    # Create and return a new qubit object with the updated state
    return Qubit(new_state)


def swap_gate(qubit1, qubit2):
     # Apply the SWAP gate operation
    new_state = np.zeros(4, dtype=complex)
    new_state[0] = qubit1.alpha * qubit2.alpha
    new_state[1] = qubit1.alpha * qubit2.beta
    new_state[2] = qubit1.beta * qubit2.alpha
    new_state[3] = qubit1.beta * qubit2.beta
    return new_state

def controlled_z_gate(control_qubit, target_qubit):
    # Define the controlled-Z gate matrix
    cz_matrix = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, -1]])
    # Construct the joint state of control and target qubits
    joint_state = np.kron(control_qubit.state, target_qubit.state)
    
    # Apply the controlled-Z gate operation to the joint state
    new_state = np.dot(cz_matrix, joint_state)
    
    # Create and return new qubit objects for control and target qubits with the updated state
    new_control_state = new_state[:2]
    new_target_state = new_state[2:]
    return Qubit(new_control_state), Qubit(new_target_state)


def controlled_u_gate(control_qubit, target_qubit, theta):
    # Define the controlled-U gate matrix
    cu_matrix = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, np.cos(theta), -np.sin(theta)],
                          [0, 0, np.sin(theta), np.cos(theta)]])
    
    # Construct the joint state of control and target qubits
    joint_state = np.kron(control_qubit.state, target_qubit.state)
    
    # Apply the controlled-U gate operation to the joint state
    new_state = np.dot(cu_matrix, joint_state)
    
    # Create and return new qubit objects for control and target qubits with the updated state
    new_control_state = new_state[:2]
    new_target_state = new_state[2:]
    return Qubit(new_control_state), Qubit(new_target_state)

def controlled_y_gate(control_qubit, target_qubit):
    # Define the controlled-Y gate matrix
    cy_matrix = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, -1j],
                          [0, 0, 1j, 0]])
    
    # Construct the joint state of control and target qubits
    joint_state = np.kron(control_qubit.state, target_qubit.state)
    
    # Apply the controlled-Y gate operation to the joint state
    new_state = np.dot(cy_matrix, joint_state)
    
    # Create and return new qubit objects for control and target qubits with the updated state
    new_control_state = new_state[:2]
    new_target_state = new_state[2:]
    return Qubit(new_control_state), Qubit(new_target_state)

# print(pauli_z(Qubit(1, 0)))
# qubit = Qubit(1.5367, 0.45672) # Example qubit in superposition
# print(qubit)
# measurement_outcome = qubit.measure_and_collapse()
# print("Measurement outcome:", measurement_outcome)
# print("Collapsed qubit state:", qubit)
# print(Qubit(1, 0))
# print(hadamard(Qubit(1, 0)))
# uGate = controlled_u_gate(Qubit(0.707,0.707), Qubit(1, 0), np.pi/2)

# print(uGate[0], uGate[1])
