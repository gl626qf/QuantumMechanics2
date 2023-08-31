# import qutip
# import numpy as np
# import matplotlib.pyplot as plt

# # Define position and momentum bases
# position_basis = qutip.basis(50, 25)  # 50-dimensional position basis
# momentum_basis = qutip.basis(50, 0)   # 50-dimensional momentum basis

# # Define a quantum state in the position basis
# psi_position = qutip.basis(50, 10)  # State located at position 10

# # Transform state to momentum basis
# psi_momentum = psi_position.transform(momentum_basis)

# # Calculate expectation values in both bases
# expectation_position = qutip.expect(qutip.position(50), psi_position)
# expectation_momentum = qutip.expect(qutip.momentum(50), psi_momentum)

# # Print results
# print("Expectation value in position basis:", expectation_position)
# print("Expectation value in momentum basis:", expectation_momentum)

import qutip

# N = 5
# m = 4
# n = 3

# MAKE THIS IN THE main.py

# Define the original and target bases
original_basis = qutip.basis(N, m)  # Original basis state |m⟩
target_basis = qutip.basis(N, n)    # Target basis state |n⟩

# Create a state in the original basis
state_original = original_basis

# Calculate the transformation matrix elements
transformation_matrix_elements = qutip.qeye(N)
# .matrix_element(target_basis.dag(), original_basis)

print(transformation_matrix_elements)
# # Construct the transformed state vector
state_transformed = sum(transformation_matrix_elements[i, j] * target_basis[i] for i, j in enumerate(range(N)))

print("Original state in original basis:", state_original)
print("Transformed state in target basis:", state_transformed)
