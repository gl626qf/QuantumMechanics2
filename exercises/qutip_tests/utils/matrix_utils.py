import numpy as np
import scipy.linalg as la

def random_square_matrix(n):
    return np.random.rand(n, n) + 1j * np.random.rand(n, n)

def random_hermitian_matrix(n):
    return random_square_matrix(n) + random_square_matrix(n).conj().T

def random_unitary_matrix(n):
    return la.expm(1j * random_hermitian_matrix(n))

def random_matrix_rektangular(m, n):
    return np.random.rand(m, n) + 1j * np.random.rand(m, n)
