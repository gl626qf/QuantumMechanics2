import qutip

def creation_operator(n_levels):
    return qutip.create(n_levels)

def annihilation_operator(n_levels):
    return qutip.destroy(n_levels)

def number_operator(n_levels):
    return qutip.num(n_levels)
