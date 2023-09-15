import qutip
import numpy as np
import matplotlib.pyplot as plt

def plot_wavefunction(x_vals, psi_vals, title):
    plt.figure()
    plt.plot(x_vals, np.abs(psi_vals) ** 2)
    plt.xlabel("Position")
    plt.ylabel("Probability Density")
    plt.title(title)
    plt.show()



def harmonic_oscillator_wavefunction(n, n_levels, x_vals, omega):
    basis_states = [qutip.basis(n_levels, i) for i in range(n_levels)]
    psi_vals = np.sum([basis_state[n] * np.exp(-0.5 * omega * x_vals**2) for n, basis_state in enumerate(basis_states)], axis=0)
    return psi_vals


def particle_in_box_wavefunction(n, L, x_vals):
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x_vals / L)
    return psi

def free_particle_wavepacket(x_vals, k0, sigma):
    psi = np.exp(-0.5 * ((x_vals - x0) / sigma)**2 + 1j * k0 * x_vals)
    return psi
