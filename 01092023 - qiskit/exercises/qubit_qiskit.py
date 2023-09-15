import numpy as np
import qutip as qt

#NEED TO INSTALL QISKIT!!!



pauli_x = qt.sigmax()
pauli_y = qt.sigmay()
pauli_z = qt.sigmaz()
I = qt.qeye(2)


#Defining constant, needs to be changed
mu = 2
B = 4
D = 1




# Construct the hamiltonian
H = mu * I + np.sqrt(B**2 + D**2) * (B / np.sqrt(B**2 + D**2) * pauli_x + D / np.sqrt(B**2 + D**2) * pauli_z)

print(pauli_z)
print(H)


# The eigenvalues of the hamiltonian
eigenvalues, eigenvectors = np.linalg.eig(H)