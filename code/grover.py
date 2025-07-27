def diffusion(circuit):
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.h(1)
    circuit.cx(0, 1)
    circuit.h(1)
    circuit.x([0, 1])
    circuit.h([0, 1])


# Grover Circuit
grover_circ = QuantumCircuit(2)
grover_circ.h([0, 1])  # Superposition
oracle(grover_circ)  # Oracle anwenden
diffusion(grover_circ)  # Verstärkung
grover_circ.measure_all()
