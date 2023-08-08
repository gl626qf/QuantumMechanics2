from spin_simulation import simulate_spin_measurement, plot_spin_expectations
import numpy as np
import qutip
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sx = qutip.sigmax()
    sy = qutip.sigmay()
    sz = qutip.sigmaz()

    # Define initial state
    initial_state = qutip.basis(2, 0)
    # Define Hamiltonian
    H = 0.5 * (sx + 0.5 * sy)

    # Time points for simulation
    times = np.linspace(0.0, 10.0, 100)

    # Perform simulation
    result = simulate_spin_measurement(initial_state, H, times, [sx, sy, sz])

    # Plot results
    plot_spin_expectations(times, result.expect, [r"$\left<\sigma_x\right>$", r"$\left<\sigma_y\right>$", r"$\left<\sigma_z\right>$"])



    # Evaluating the inequality