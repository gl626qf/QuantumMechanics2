import qutip

def pauli_x():
    return qutip.sigmax()

def pauli_y():
    return qutip.sigmay()

def pauli_z():
    return qutip.sigmaz()

def pauli_plus():
    return (pauli_x() + 1j * pauli_y()) / 2.0

def pauli_minus():
    return (pauli_x() - 1j * pauli_y()) / 2.0
