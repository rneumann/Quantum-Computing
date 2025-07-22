from qiskit import QuantumCircuit

# Quantenschaltung mit 2 Qubits und 2 klassischen Bits erstellen
grover_circuit = QuantumCircuit(2, 2)

# Hadamard-Gate auf jedes Qubit anwenden
grover_circuit.h([0, 1])
