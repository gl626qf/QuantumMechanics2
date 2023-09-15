import numpy as np
import qutip as qt



pauli_x = qt.sigmax()
pauli_y = qt.sigmay()
pauli_z = qt.sigmaz()


# Describing the S*n matrix 
alpha = 0.4
beta = 0.5
n = np.array([np.cos(beta) * np.sin(alpha), np.sin(beta) * np.sin(alpha), np.cos(beta)])
S = 1/2 * (pauli_x + pauli_y + pauli_z)
Sn = n[0] * pauli_x + n[1] * pauli_y + n[2] * pauli_z
# print(Sn)


# The probability of measuring 1/2 in the S_x direction
print(np.cos(np.pi/4)**2
      )