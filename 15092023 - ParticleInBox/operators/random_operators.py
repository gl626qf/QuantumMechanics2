import qutip
import numpy as np

# def random_hermitian_operator(dim):
#     random_matrix = np.random.rand(dim, dim) + 1j * np.random.rand(dim, dim)
#     hermitian_matrix = (random_matrix + random_matrix.conj().T) / 2.0
#     return qutip.Qobj(hermitian_matrix)

def random_hermitian_operator(dim):
    # Generate a random Hermitian operator
    random_hermitian = qutip.rand_herm(dim)

    return random_hermitian



def random_unitary_operator(dim):
    random_matrix = np.random.rand(dim, dim) + 1j * np.random.rand(dim, dim)
    unitary_matrix = qutip.Qobj(random_matrix)
    return unitary_matrix.expm()  # Exponential to get a unitary operator

def random_density_matrix(dim):
    random_matrix = np.random.rand(dim, dim) + 1j * np.random.rand(dim, dim)
    density_matrix = random_matrix @ random_matrix.conj().T
    return qutip.Qobj(density_matrix / np.trace(density_matrix))

def random_projection_operator(dim):
    random_matrix = np.random.rand(dim, dim) + 1j * np.random.rand(dim, dim)
    projection_matrix = random_matrix @ random_matrix.conj().T
    return qutip.Qobj(projection_matrix / np.trace(projection_matrix))
