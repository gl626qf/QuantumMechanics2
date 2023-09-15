import matplotlib.pyplot as plt

def plot_wavefunction(x_vals, psi_vals, title, xlabel="Position", ylabel="Probability Density"):
    plt.figure()
    plt.plot(x_vals, psi_vals)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
