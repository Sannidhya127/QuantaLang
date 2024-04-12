
import numpy as np
from math import gcd
from numpy.random import randint
from gates import hadamard
from qubit import Qubit

def qft(qubit_state):
    num_qubits = len(qubit_state)
    qubit_state = np.array(qubit_state, dtype=complex)
    transformed_state = np.zeros(num_qubits, dtype=complex)

    for j in range(num_qubits):
        for k in range(num_qubits):
            transformed_state[j] += qubit_state[k] * np.exp(2j * np.pi * j * k / num_qubits)

    return transformed_state / np.sqrt(num_qubits)

# Example usage
qubit_state = [1, 0, 0, 0]  # Initial state |0⟩
transformed_state = qft(qubit_state)
print("Transformed state after applying QFT:", transformed_state)


def controlled_u_gate(a, power, N, control_qubit, target_qubit):
    """
    This function applies a controlled-U gate to a target qubit, controlled by another qubit.
    The U gate is defined as U|y⟩ = |ay mod N⟩.
    """
    # Calculate the result of applying the U gate
    u_result = (a ** power) % N

    # Apply the controlled-U gate
    if control_qubit.measure_and_collapse() == 1:
        target_qubit.set_state(u_result)

def continued_fractions_algorithm(measurements, N):
    fractions = []
    for measurement in measurements:
        fraction = measurement / N
        fractions.append(int(fraction))
        while abs(fraction - int(fraction)) > 1 / (2 * N ** 2):
            if fraction - int(fraction) == 0:  # Prevent division by zero
                break
            fraction = 1 / (fraction - int(fraction))
            fractions.append(int(fraction))
    return fractions
def modular_exponentiation(base, exponent, modulus):
    return pow(base, exponent, modulus)


def quantum_period_finding(a, N, qubits, controlled_u_gate, qft, continued_fractions_algorithm):
    # Prepare the control qubits in a superposition state
    for qubit in qubits:
        hadamard(qubit)

    # Apply the controlled-U gates
    for i, control_qubit in enumerate(qubits):
        # Create a new qubit for the target
        target_qubit = Qubit([1, 0])
        # Apply the controlled-U gate
        controlled_u_gate(a, 2**i, N, control_qubit, target_qubit)

    # Get the state vector of all qubits
    state_vector = state_vector = np.concatenate([qubit.state for qubit in qubits])

    # Apply the quantum Fourier transform to the state vector
    qft(state_vector)

    # Measure the qubits
    measurements = [qubit.measure_and_collapse() for qubit in qubits]

    # Use the continued fractions algorithm to find the period
    r = continued_fractions_algorithm(measurements, N)

    return r

def shors_algorithm(N):
    factors = set()
    if is_prime(N):
        print("Shor's algorithm cannot be applied to a prime number.")
        exit() 
    while len(factors) < 2:
        # Step 2: Choose a random integer 'a' between 2 and N-1
        a = randint(2, N)
        
        # Step 3: Calculate the greatest common divisor of 'a' and 'N'
        gcd_value = gcd(a, N)
        if gcd_value > 1:
            factors.add(gcd_value)
            continue
        
        # Step 4: Use quantum period finding to find the period 'r' of (a^x % N)
        n = N.bit_length()
        qubits = [Qubit(1,0) for _ in range(n)]
        r = quantum_period_finding(a, N, qubits, controlled_u_gate, qft, continued_fractions_algorithm)
        
        # Step 5: Check if 'r' is even and a^(r/2) is not congruent to -1 modulo 'N'
        for i in r:
            if r[i] % 2 == 0:
                x = modular_exponentiation(a, int(r[i]/2), N)
                if x != 1 and x != -1:
                    factors.add(gcd(x - 1, N))

    return factors
# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the algorithm
N = 295636 # Number to factorize
factor = shors_algorithm(N)
if factor != 1:
    print(f"A non-trivial factor of {N} is {factor}")
else:
    print(f"Failed to find a non-trivial factor of {N}")
