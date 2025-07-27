%matplotlib inline

import matplotlib.pyplot as plt
from IPython.display import display as dp
from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2


# Oracle für Zielzustand |11⟩
def oracle(circuit):
    circuit.cz(0, 1)  # CZ wirkt auf |11>


# Diffusionsoperator
def diffusion(circuit):
    circuit.h([0, 1])
    circuit.z([0, 1])
    circuit.cz(0, 1)
    circuit.h([0, 1])


# Grover Schaltkreis mit 2 Qubits
grover_circuit = QuantumCircuit(2)

# Superposition
grover_circuit.h([0, 1])
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

# Simulation mit SamplerV2
sampler = SamplerV2()
job = sampler.run([grover_circuit], shots=1024)
result = job.result()
counts = result[0].data.meas.get_counts()

print("Grover-Ergebnis:", counts)

# Visualisierung der Messergebnisse als Histogramm
plot_histogram(counts)
plt.show()