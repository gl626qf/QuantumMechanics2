import qutip
import numpy as np

# Create a quantum state
psi = qutip.basis(2, 0)  # Example qubit state |0⟩

# Calculate the norm of the state using the identity operator
state_norm = qutip.expect(qutip.qeye(2), psi)

print("Norm of the state:", state_norm)

# Create a quantum operator
op = qutip.destroy(2)  # Example annihilation operator

# Calculate the Frobenius norm of the operator's matrix
op_matrix = op.full()
op_norm = np.linalg.norm(op_matrix, 'fro')

print("Norm of the operator:", op_norm)
