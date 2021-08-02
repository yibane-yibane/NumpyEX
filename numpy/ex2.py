import numpy as np
import matplotlib.pylab as plt
from scipy import special


def ex1_checkerboard_array():
    vector = [1, 2, 3]
    matrix = np.ones((3, 3))

    vector_vector = np.dot(vector, vector)
    matrix_vector = np.dot(matrix, vector)
    matrix_matrix = np.dot(matrix, matrix)

    print(vector_vector)
    print(matrix_vector)
    print(matrix_matrix)


def ex2_plot_function():
    x_array = np.linspace(-1, 1, 250)
    y_array = x_array**2 * np.sin(1/ x_array**2) + x_array
    plt.plot(x_array, y_array)
    plt.show()


def ex3_plot_function_2():
    x = np.linspace(5, 25)
    y = np.absolute(1 - (1 / (1 + x**2)) / (1 / x**2))
    plt.semilogy(x, y)
    plt.show()


def ex4_gift():
    print(special.pbdv(5, 2))
