from gates import *

class Entangle:
    def __init__(self) -> None:
        self._entangled = False

    def __str__(self) -> str:
        return f"Entangled: {self._entangled}"
    
    def BellState(self,q1,q2):
        # Apply Hadamard gate to q1
        self.q1 = hadamard(q1)
        # Apply CNOT gate with q1 as control and q2 as target
        self.q2 = cnot_gate(q1, q2)
        # Return the entangled qubits
        return q1, q2
    
    def EPRPair(self,q1, q2):
        # Apply Hadamard gate to q1
        self.q1 = hadamard(q1)
        # Apply CNOT gate with q1 as control and q2 as target
        self.q2 = cnot_gate(q1, q2)
        # Return the entangled qubits
        return self.q1, self.q2
    
    def Entangle_GHZ(self,qubits):
        # Apply Hadamard gate to the first qubit
        qubits[0] = hadamard(qubits[0])
        # Apply a series of CNOT gates to entangle all qubits
        for i in range(len(qubits) - 1):
            qubits[i + 1] = cnot_gate(qubits[i], qubits[i + 1])
        # Return the entangled qubits
        for i in qubits:
            return i

    def Entangle_W(self,qubits):
        # Apply Hadamard gate to the first qubit
        qubits[0] = hadamard(qubits[0])
        # Apply a series of CNOT gates to entangle all qubits
        for i in range(len(qubits) - 1):
            qubits[i + 1] = cnot_gate(qubits[i], qubits[i + 1])
        # Apply a final Hadamard gate to the last qubit
        qubits[-1] = hadamard(qubits[-1])
        # Return the entangled qubits
        for i in qubits:
            return i