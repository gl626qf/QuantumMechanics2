import numpy as np
import qutip
import operators.pauli_operators as pauli_ops

# print(pauli_ops.pauli_x())


# Make S vector containing Pauli matrices
S_x = pauli_ops.pauli_x()
S_y = pauli_ops.pauli_y()
S_z = pauli_ops.pauli_z()

# print(S_x)
# print(S_y)
# print(S_z)

S = np.array([S_x, S_y, S_z])
# print(S)


# Make n vector
alpha = 0.5
beta = 0.2
n = np.array([np.cos(alpha) * np.sin(beta), np.sin(alpha) * np.sin(beta), np.cos(beta)])
# print(n)


def eigenket_solution(alpha, beta):
    # up = qutip.basis(1, 0)
    up = np.array([1, 0])
    # down = qutip.basis(0, 1)
    down = np.array([0, 1])
    return np.cos(beta/2) * up + np.sin(beta/2) * np.exp(-1j * alpha) * down










# S is vector of matrices, n is vector of numbers
# Making matrix multiplication of S and n
# for i in range(3):
#     # np.dot(S[i], n[i])
#     S_times_n = np.dot(S[i], n[i])
#     # print(S_times_n)
#     # print("The x,y,z S{i} * n{i}".format(i=i))


#     print(S_times_n @ eigenket_solution(alpha, beta))


#     #Testing if the eigenket_solution function works
#     print(1/2  * eigenket_solution(alpha, beta))

#     print("")

    


# print(eigenket_solution(alpha, beta))

#Now we want to make a function that takes in a vector n and returns the eigenket


#Making matrix by hand S*n
S_hand = np.array([[np.cos(beta), np.exp(-1j * alpha) * np.sin(beta)], 
                   [np.exp(-1j * alpha) * np.sin(beta), -np.cos(beta)]])

# print(S_hand)

#Finding the eigenket
h_bar = 1
eigen_value = h_bar/2


# print(np.linalg.eig(S_hand))
# eigenket = np.linalg.eig(S_hand)

# print(eigenket)
# print(S_hand @ eigenket[][0])


# Making identity matrix with eigen_values
identity_matrix = np.identity(2)
identity_matrix[0][0] = eigen_value
identity_matrix[1][1] = eigen_value
# print(identity_matrix)

S_hand_identity = S_hand - identity_matrix
# print(S_hand_identity)

v = np.array([np.cos(beta / 2), np.sin(beta / 2) * np.exp(-1j * alpha)])
# print(v)

print(S_hand_identity @ v)