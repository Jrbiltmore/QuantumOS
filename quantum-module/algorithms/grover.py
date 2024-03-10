# grover.py

from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram
import numpy as np

def grover_algorithm(n, marked_elements):
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc += oracle(n, marked_elements)
    qc += diffusion(n)
    return qc

def oracle(n, marked_elements):
    qc = QuantumCircuit(n)
    for element in marked_elements:
        qc.x(element)
    qc.h(n-1)
    qc.mct(list(range(n-1)), n-1)
    qc.h(n-1)
    for element in marked_elements:
        qc.x(element)
    return qc

def diffusion(n):
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n-1)
    qc.mct(list(range(n-1)), n-1)
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))
    return qc

def run_grover(n, marked_elements):
    grover_circuit = grover_algorithm(n, marked_elements)
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(grover_circuit, simulator, shots=1).result()
    counts = result.get_counts()
    return counts

# Example usage:
if __name__ == "__main__":
    n = 3  # Number of qubits
    marked_elements = [2]  # Marked elements in the search space

    counts = run_grover(n, marked_elements)
    print("Counts:", counts)
    plot_histogram(counts)
