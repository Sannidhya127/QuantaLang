import numpy as np
from entangle import *
def simulate_decoherence(rho, p):
    """
    Simulate decoherence on a quantum system described by the density matrix rho.
    
    Parameters:
    rho: np.array
        The density matrix of the quantum system.
    p: float
        The probability of decoherence occurring.
        
    Returns:
    rho_decohered: np.array
        The density matrix of the quantum system after decoherence.
    """
    # Get the diagonal elements of the density matrix
    diagonal = np.diag(np.diag(rho))
    
    # Get the off-diagonal elements of the density matrix
    off_diagonal = rho - diagonal
    
    # Introduce decoherence
    rho_decohered = diagonal + (1 - p) * off_diagonal
    
    return rho_decohered

def construct_density_matrix_dual(qubit1, qubit2):
    """
    Construct the density matrix of a two-qubit system.
    
    Parameters:
    qubit1, qubit2: Qubit
        The two qubits.
        
    Returns:
    rho: np.array
        The density matrix of the two-qubit system.
    """
    # Calculate the outer product of the two qubits' state vectors
    rho = np.outer(qubit1.state, qubit2.state.conj())
    
    return rho



# rho_decohered = simulate_decoherence(rho, 0.1)

# Entangle two qubits into a Bell state
qubit1, qubit2 = Entangle.bell_state_entanglement()

# Construct the density matrix of the two-qubit system
rho = construct_density_matrix_dual(qubit1, qubit2)
print("Before decoherence:")
print(rho)

# Simulate decoherence
rho_decohered = simulate_decoherence(rho, 0.1)

# Print the density matrix after decoherence
print("After decoherence:")
print(rho_decohered)