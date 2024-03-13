from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
from  qiskit_aer import AerSimulator, Aer

circ = QuantumCircuit(2,2)

circ.h(0)
circ.cx(0,1)
circ.barrier()

circ.x(0)
circ.barrier()

circ.cx(0,1)
circ.h(0)
circ.barrier()
circ.measure([0,1],[0,1])

print(circ.draw(output='text',justify='none'))

aersim = AerSimulator()
simulator = Aer.get_backend('aer_simulator')