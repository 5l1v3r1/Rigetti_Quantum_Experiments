from pyquil.quilatom import QubitPlaceholder
from pyquil.quil import Program
from pyquil.api import QVMConnection 
from pyquil.gates import CNOT, H,X,Z,MEASURE

s = 14 # 1110

q0 = QubitPlaceholder()
q1 = QubitPlaceholder()
q2 = QubitPlaceholder()
q3 = QubitPlaceholder()
tmp = QubitPlaceholder()

prog = Program(X(tmp),H(q0),H(q1),H(q2),H(q3),H(tmp))

prog += Program(CNOT(q3, tmp),CNOT(q2,tmp),CNOT(q1,tmp))

prog += Program(H(q0),H(q1),H(q2),H(q3),H(tmp))

prog += Program(MEASURE(q0, 0),MEASURE(q1, 1),MEASURE(q2,2 ),MEASURE(q3,3))

print(prog)

qvm = QVMConnection() 
results = qvm.run(prog, classical_addresses=[3,2,1,0], trials=10)

print results
