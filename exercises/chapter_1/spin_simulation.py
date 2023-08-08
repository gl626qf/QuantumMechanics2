import numpy as np
import qutip
import matplotlib.pyplot as plt

def simulate_spin_measurement(initial_state, hamiltonian, times, operators):
    """
    Simulate spin measurement outcomes using QuTiP.

    Args:
        initial_state (qutip.Qobj): Initial quantum state.
        hamiltonian (qutip.Qobj): Hamiltonian for time evolution.
        times (array_like): Time points for simulation.
        operators (list of qutip.Qobj): List of operators to measure.

    Returns:
        qutip.Result: Simulation results.
    """
    result = qutip.mesolve(hamiltonian, initial_state, times, [], operators)
    return result

def plot_spin_expectations(times, expectations, labels):
    """
    Plot spin expectation values over time.

    Args:
        times (array_like): Time points.
        expectations (list of array_like): List of expectation value arrays.
        labels (list of str): Labels for each expectation value.

    Returns:
        None
    """
    fig, axes = plt.subplots(1, 1)

    for i, (expectation, label) in enumerate(zip(expectations, labels)):
        axes.plot(times, expectation, label=label)

    axes.set_xlabel(r"$t$", fontsize=20)
    axes.legend(loc=2)
    plt.show()

