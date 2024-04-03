# from gates import *
import matplotlib.pyplot as plt
from gates import *
class QCIRCUIT:
    def __init__(self, num_qubits):
        self.qubits = num_qubits
        self.gates = [] 

    def add_gate(self, gate_function):
        self.gates.append(gate_function)

    def execute(self, qubits):
        for gate in self.gates:
            qubits = [gate(qubit) for qubit in qubits]
        return qubits
    def draw_quantum_circuit(self,num_qubits, gates):
        fig, ax = plt.subplots()

        # Set axis limits and ticks
        ax.set_xlim(0, num_qubits + 1)
        ax.set_ylim(0, len(gates) + 1)
        ax.set_xticks(range(1, num_qubits + 1))
        ax.set_yticks(range(1, len(gates) + 1))
        ax.xaxis.tick_top()

        # Draw qubits
        for i in range(1, num_qubits + 1):
            ax.add_patch(plt.Rectangle((i - 0.5, 0.5), 1, len(gates), fill=False, edgecolor='black'))

        # Draw gates
        for idx, gate in enumerate(gates):
            ax.text(0.5, idx + 1, gate, ha='center', va='center')

        # Hide axes
        ax.axis('off')

        plt.show()

# Example usage


# Create a quantum circuit with 3 qubits
# circuit = QCIRCUIT(3)

# # Add gate operations to the circuit
# circuit.add_gate(hadamard)
# circuit.add_gate(pauli_x)
# circuit.add_gate(pauli_y)

# # Define initial qubit states
# qubits = [Qubit(1, 0), Qubit(0, 1), Qubit(1/math.sqrt(2), 1/math.sqrt(2))]

# # Execute the circuit
# final_states = circuit.execute(qubits)

# # Print final states of the qubits
# for idx, qubit in enumerate(final_states):
#     print(f"Qubit {idx + 1}: {qubit}")



# gate_operations = ['H', 'X', 'Y', 'Z', 'CNOT']
# circuit.draw_quantum_circuit(3, gate_operations)