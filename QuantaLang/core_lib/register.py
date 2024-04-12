import numpy as np
from qubit import Qubit
from gates import hadamard, pauli_x, pauli_y, pauli_z, phase_gate, cnot_gate
class QuantumRegister:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.num_states = 2 ** num_qubits
        initial_state = np.zeros(2, dtype=complex)
        initial_state[0] = 1  # Represents |0⟩ state
        self.state_vector = initial_state
        for _ in range(num_qubits - 1):
            self.state_vector = np.kron(self.state_vector, initial_state)

    def apply_gate(self, gate_function, target_qubit):
        if not callable(gate_function):
            raise ValueError("Gate function must be callable")
        if target_qubit >= self.num_qubits:
            raise ValueError("Target qubit index out of range")
        for i in range(self.num_states):
            binary_str = format(i, f'0{self.num_qubits}b')
            if binary_str[self.num_qubits - 1 - target_qubit] == '1':
                qubit = Qubit(self.state_vector[i])
                new_state = gate_function(qubit)
                if isinstance(new_state.state, np.ndarray):
                    self.state_vector[i] = new_state.state[0]  # Adjust indexing as needed
                else:
                    self.state_vector[i] = new_state.state






    def tensor_product(self, other_register):
        if not isinstance(other_register, QuantumRegister):
            raise TypeError("Input must be a QuantumRegister object")
        new_num_qubits = self.num_qubits + other_register.num_qubits
        new_num_states = self.num_states * other_register.num_states
        new_state_vector = np.kron(self.state_vector, other_register.state_vector)
        return QuantumRegister(new_num_qubits, new_state_vector)

# Define a gate function (for demonstration purposes)


# Create a QuantumRegister object with 2 qubits
# register = QuantumRegister(num_qubits=2)
# # Apply Hadamard gate to the first qubit
# register.apply_gate(hadamard, target_qubit=0)

# # Print the state vector after applying the gate
# print("State vector after applying Hadamard gate to the first qubit:")
# print(register.state_vector)

