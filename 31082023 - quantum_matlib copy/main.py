import numpy as np
import qutip
import operators.pauli_operators as pauli_ops
# import operators.harmonic_oscillator_operators as harmonic_ops
# import concepts.wavefunctions as wavefunctions
# import visualizations.plot_utils as plot_utils
import operators.linear_algebra_operators as la_ops
import operators.random_operators as rand_ops
# import concepts.basis_transformation as basis_transformation
# import concepts.unitary_transformation as unitary_transformation
# import concepts.plotting_script as plotting_script
# import concepts.eigen_value as eigen_value
# import exercises.problem1_11 as problem1_11
# import exercises.problem1_13 as problem1_13
# import exercises.qubit_qiskit as qubit_qiskit
import exercises.problem1_14 as problem1_14



def main():

    # Exercise 1.6: 
    # a. tr(XY) = tr(YX)
    # random_matrix_1 = rand_ops.random_hermitian_operator(3)
    # random_matrix_2 = rand_ops.random_hermitian_operator(3)
    # tr1 = la_ops.operator_trace(random_matrix_1 * random_matrix_2)
    # tr2 = la_ops.operator_trace(random_matrix_2 * random_matrix_1)



    # Problem 1.11
    # print(problem1_11.pauli_ops)
    # print(problem1_13)
    # print(qubit_qiskit)
    print(problem1_14)



    # Basis transformation
    # basis_transformation




if __name__ == "__main__":
    main()