oracle = QuantumCircuit(2)
oracle.x(0)         # |01> -> |11>)
oracle.cz(0, 1)     # Phaseninversion durch CZ
oracle.x(0)         # Rücktransformation zu |01)
