import qutip

#Including hbar
h_bar = 1.0



def pauli_x():
    return h_bar / 2* qutip.sigmax()

def pauli_y():
    return h_bar / 2 * qutip.sigmay()

def pauli_z():
    return h_bar / 2 * qutip.sigmaz()

def pauli_plus():
    return (pauli_x() + 1j * pauli_y()) / 2.0

def pauli_minus():
    return (pauli_x() - 1j * pauli_y()) / 2.0
