import numpy as np
import qutip
import operators.pauli_operators as pauli_ops
import operators.harmonic_oscillator_operators as harmonic_ops
import concepts.wavefunctions as wavefunctions
import visualizations.plot_utils as plot_utils
import operators.linear_algebra_operators as la_ops
import operators.random_operators as rand_ops


def main():
    # # Example using Pauli operators
    # print("Pauli X operator:")
    # print(pauli_ops.pauli_x())

    # # Example using Harmonic Oscillator operators
    # n_levels = 4
    # print(f"Creation operator for {n_levels} energy levels:")
    # print(harmonic_ops.creation_operator(n_levels))

    # # Example using wavefunctions and visualization utilities
    # x_vals = np.linspace(-5, 5, 500)
    # harmonic_psi = wavefunctions.harmonic_oscillator_wavefunction(0, n_levels, x_vals, omega=1.0)
    # plot_utils.plot_wavefunction(x_vals, np.abs(harmonic_psi[0])**2, "Harmonic Oscillator Wavefunction")


    # Exercise 1.6: 
    # a. tr(XY) = tr(YX)
    random_matrix_1 = rand_ops.random_hermitian_operator(3)
    random_matrix_2 = rand_ops.random_hermitian_operator(3)
    tr1 = la_ops.operator_trace(random_matrix_1 * random_matrix_2)
    tr2 = la_ops.operator_trace(random_matrix_2 * random_matrix_1)
    print(tr1 == tr2)




if __name__ == "__main__":
    main()