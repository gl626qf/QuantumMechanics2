from spin_simulation import simulate_spin_measurement, plot_spin_expectations
import uncertainty_relation1
import numpy as np
import qutip
import matplotlib.pyplot as plt
import unittest

if __name__ == "__main__":
    sx = qutip.sigmax()
    sy = qutip.sigmay()
    sz = qutip.sigmaz()



    # Playing around with mesolve

    # # Define initial state
    # initial_state = qutip.basis(2, 0)
    # # Define Hamiltonian
    # H = 0.5 * (sx + 0.5 * sy)

    # # Time points for simulation
    # times = np.linspace(0.0, 10.0, 100)

    # # Perform simulation
    # result = simulate_spin_measurement(initial_state, H, times, [sx, sy, sz])

    # # Plot results
    # plot_spin_expectations(times, result.expect, [r"$\left<\sigma_x\right>$", r"$\left<\sigma_y\right>$", r"$\left<\sigma_z\right>$"])



    # Problem 1.3
    # Define the spin-up state along the x-direction
    # spin_up_x = qutip.basis(2, 0)  # |+x⟩

    # # Check the inequality for A = σ_x and B = σ_y
    # inequality_satisfied = calculate_inequality(sx, sy, spin_up_x)

    # if inequality_satisfied:
    #     print("Inequality is satisfied.")
    # else:
    #     print("Inequality is not satisfied.")


    # Define the spin-up state along the x-direction
    spin_up_x = qutip.basis(2, 0)  # |+x⟩

    # Define the spin-up state along the z-direction
    spin_up_z = qutip.basis(2, 0)  # |+z⟩

    # Calculate and check the inequality for different combinations of operators and states
    print("Inequality for sx and sy:", uncertainty_relation1.calculate_inequality(sx, sy, spin_up_x))
    print("Inequality for sz and sy:", uncertainty_relation1.calculate_inequality(sz, sy, spin_up_x))
    print("Inequality for sx and sz:", uncertainty_relation1.calculate_inequality(sx, sz, spin_up_z))