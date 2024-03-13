from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
# 양자 회로 생성
qc = QuantumCircuit(3)

# Hadamard 게이트 추가
qc.h(0)
qc.cx(0,1)
qc.cx(0,2)
# 회로 시각화
print(qc.draw(output='text'))


# Set the initial state of the simulator to the ground state using from_int
state = Statevector.from_int(0, 2**3)

# Evolve the state by the quantum circuit
state = state.evolve(qc)

#draw using latex
print(state.draw(output='text'))
