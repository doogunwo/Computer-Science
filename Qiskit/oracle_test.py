from qiskit import Aer, execute, QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import GroverOperator

# 오라클을 구현하는 함수
def oracle(qc):
    qc.cz(0, 1)  # 원하는 상태를 표시하기 위한 조건부 Z 게이트

# 확산 변환을 구현하는 함수
def diffusion(qc):
    qc.h([0, 1])
    qc.z([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])

# 회로 초기화
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr, cr)

# 초기 상태 준비 (모든 가능한 상태의 중첩)
qc.h([0, 1])

# 그로버의 알고리즘: 오라클과 확산 변환 반복
oracle(qc)
diffusion(qc)

# 결과 측정
qc.measure(qr, cr)

# 시뮬레이션 실행
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts(qc)

# 결과 출력
print(counts)
plot_histogram(counts)
