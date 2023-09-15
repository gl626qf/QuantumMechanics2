import qutip
import numpy as np
import matplotlib.pyplot as plt

# Create a position basis
x_vals = np.linspace(-5, 5, 500)

# Create a quantum state in the position basis
psi_position = qutip.basis(500, 250)

# Calculate the wavefunction values at each position
wavefunction_vals_position = psi_position.full()

# Transform the state to momentum basis
momentum_basis = qutip.momentum(500)
psi_momentum = psi_position.transform(momentum_basis.dag())
wavefunction_vals_momentum = psi_momentum.full()

# Calculate the probability densities from the wavefunction values
prob_density_position = np.abs(wavefunction_vals_position) ** 2
prob_density_momentum = np.abs(wavefunction_vals_momentum) ** 2

# Plot the probability densities
plt.plot(x_vals, prob_density_position, label="Position Basis")
plt.plot(x_vals, prob_density_momentum, label="Momentum Basis")
plt.xlabel("Position / Momentum")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
