%matplotlib inline

import matplotlib.pyplot as plt
from IPython.display import display as dp
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator


def initialize_s(qc: QuantumCircuit, qubits: list[int]) -> QuantumCircuit:
    """Anwendung eines Hadamard-Gates auf Qubits im Schaltkreis."""
    for q in qubits:
        qc.h(q)
    return qc


def oracle(circuit: QuantumCircuit) -> None:
    """Oracle für den Zielzustand |11⟩."""
    circuit.cz(0, 1)


def diffusion(circuit: QuantumCircuit) -> None:
    """Diffusionsoperator (U_s)."""
    circuit.h([0, 1])
    circuit.z([0, 1])
    circuit.cz(0, 1)
    circuit.h([0, 1])


# Grover Schaltkreis mit 2 Qubits
grover_circuit = QuantumCircuit(2)

# Superposition
grover_circuit = initialize_s(grover_circuit, [0, 1])
print("Schaltkreis nach Superposition:")
dp(grover_circuit.draw())  # Schaltkreis visualisieren

# Oracle (Zielzustand markieren)
oracle(grover_circuit)
print("Schaltkreis nach Oracle:")
dp(grover_circuit.draw())  # Schaltkreis visualisieren

# Verstärkung
diffusion(grover_circuit)
print("Schaltkreis nach Verstärkung:")
dp(grover_circuit.draw())  # Schaltkreis visualisieren

# Messung
grover_circuit.measure_all()

# Simulation mit AerSimulator
simulator = AerSimulator()
job = simulator.run(grover_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

print("Grover-Ergebnis:", counts)

# Visualisierung der Messergebnisse als Histogramm
plot_histogram(counts)
plt.show()