import qutip
import numpy as np


def calculate_dispersion(operator, state):
    # Convert operator and state to numpy arrays
    operator_matrix = operator.data.toarray()
    state_vector = state.data.toarray()

    # Calculate the expectation value of the operator
    expectation = np.vdot(state_vector, operator_matrix @ state_vector)

    # Calculate the expectation value of the squared operator
    expectation_squared = np.vdot(state_vector, operator_matrix @ operator_matrix @ state_vector)

    # Calculate the dispersion using the formula
    dispersion = np.sqrt(expectation_squared - expectation ** 2)

    return dispersion

def calculate_inequality(A, B, state):
    # Calculate dispersion of A
    dispersion_A = calculate_dispersion(A, state)

    # Calculate dispersion of B
    dispersion_B = calculate_dispersion(B, state)

    # Calculate commutator of A and B
    commutator_AB = qutip.commutator(A, B)

    # Calculate norm of the expectation value of commutator
    norm_expectation_commutator = np.linalg.norm(qutip.expect(commutator_AB, state))

    # Calculate the right-hand side of the inequality
    rhs = 0.25 * norm_expectation_commutator ** 2
    lhs = dispersion_A * dispersion_B
    print("RHS: ", rhs)
    print("LHS: ", lhs)

    # Check the inequality
    inequality_satisfied = lhs >= rhs

    return inequality_satisfied


