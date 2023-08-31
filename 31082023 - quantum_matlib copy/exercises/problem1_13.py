import numpy as np



# 2 by 2 matrix
H11 = 1
H12 = 2
H22 = 3
A = np.array([[H11, H12], [H12, H22]])



# Finding eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A)
print("eigenvalues", eigenvalues)
print("Eigenvectors", eigenvectors)


#Testing if diskriminant is positive
diskriminant = (H11 + H22)**2 - 4 * (H11 * H22 - H12**2)
print("diskriminant", diskriminant)


