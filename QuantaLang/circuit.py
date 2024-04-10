# from gates import *
import matplotlib.pyplot as plt
from gates import *
class QCIRCUIT:
    def __init__(self, num_qubits):
        self.qubits = num_qubits
        self.gates = []

    def add_gate(self, gate_function, input_type):
        self.gates.append((gate_function, input_type))

    def execute(self, initial_qubits):
        qubits = initial_qubits
        for gate, input_type in self.gates:
            if input_type == int:
                # Handle gates that take an integer as input
                qubits = [gate(i) for i in range(len(qubits))]
            else:
                # Handle gates that take a Qubit object as input
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
num_qubits = 3
num_gates = 5

# Create an instance of the QCIRCUIT class
circuit = QCIRCUIT(num_qubits)

# Add gates to the circuit
# Create initial qubits (in |0⟩ state)
initial_qubits = [Qubit(1, 0) for _ in range(num_qubits)]

for _ in range(num_gates):
    gate_idx = np.random.randint(3)  # Randomly select a gate index
    if gate_idx == 0:
        circuit.add_gate(hadamard, Qubit)  # Add Hadamard gate
    elif gate_idx == 1:
        target_qubit_idx = np.random.randint(num_qubits)  # Randomly select target qubit index
        target_qubit = initial_qubits[target_qubit_idx]  # Retrieve the qubit object
        circuit.add_gate(lambda qubit: pauli_x(qubit), Qubit)  # Add Pauli-X gate
    else:
        control_qubit = np.random.randint(num_qubits - 1)  # Randomly select control qubit
        target_qubit = np.random.randint(control_qubit + 1, num_qubits)  # Randomly select target qubit
        circuit.add_gate(lambda qubit: cnot_gate(control_qubit, target_qubit), Qubit)  # Add CNOT gate

# Execute the circuit
final_qubits = circuit.execute(initial_qubits)

# Print the final state of the qubits
for idx, qubit in enumerate(final_qubits):
    print(f"Qubit {idx + 1}: {qubit}")

# Draw the quantum circuit
circuit.draw_quantum_circuit(num_qubits, ["Hadamard", "Pauli-X", "CNOT"] * num_gates)


# gate_operations = ['H', 'X', 'Y', 'Z', 'CNOT']
# circuit.draw_quantum_circuit(3, gate_operations)