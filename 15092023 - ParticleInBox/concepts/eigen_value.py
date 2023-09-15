import numpy as np
import qutip
import math

# Make matrix observable



matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues * 1/math.sqrt(2))
print("Eigenvectors:", eigenvectors)


print(eigenvalues * matrix)