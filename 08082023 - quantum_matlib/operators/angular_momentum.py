import qutip

def angular_momentum_matrices(j):
    jx = qutip.jmat(j, 'x')
    jy = qutip.jmat(j, 'y')
    jz = qutip.jmat(j, 'z')
    return jx, jy, jz

def angular_momentum_raising_operator(j):
    return qutip.jmat(j, '+')

def angular_momentum_lowering_operator(j):
    return qutip.jmat(j, '-')
