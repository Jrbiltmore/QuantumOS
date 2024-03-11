# Quantum Sensors/QuantumMagnetometers/quantum_magnetometer_simulation.py

from qiskit import Aer, QuantumCircuit, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def simulate_quantum_magnetometer(phase_shift):
    """
    Simulate a quantum magnetometer using a simple quantum circuit with a phase shift.
    The phase shift represents the effect of a magnetic field on the quantum state.
    
    Parameters:
    - phase_shift (float): Phase shift applied to the qubit, simulating the magnetic field effect.
    
    Returns:
    - dict: Measurement results showing the probability distribution of the qubit states.
    """
    # Create a quantum circuit with 1 qubit and 1 classical bit for measurement
    qc = QuantumCircuit(1, 1)

    # Initialize the qubit in superposition
    qc.h(0)
    
    # Apply the phase shift, simulating the effect of a magnetic field
    qc.u1(phase_shift, 0)  # Deprecated gate, use qc.p(phase_shift, 0) in newer Qiskit versions
    
    # Convert back to computational basis and measure
    qc.h(0)
    qc.measure(0, 0)
    
    # Execute the circuit on the Qasm simulator
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts(qc)
    
    return counts

if __name__ == "__main__":
    # Example phase shift
    phase_shift = 0.5  # Adjust this value to simulate different magnetic field strengths
    
    # Simulate the quantum magnetometer
    measurement_results = simulate_quantum_magnetometer(phase_shift)
    
    # Plot the results
    plot_histogram(measurement_results)
    plt.show()
