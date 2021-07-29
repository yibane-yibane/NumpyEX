import numpy as np
import matplotlib.pylab as plt


def plot():
    x = np.arange(-np.pi, np.pi)
    y = np.arange(-np.pi, np.pi)

    x_flat, y_flat = np.meshgrid(x, y)

    plt.contourf(x_flat, y_flat, np.sin(x_flat) * np.sin(y_flat))
    plt.colorbar()
    plt.show()


def matrix_row_plus_column():
    return np.vstack(range(5)) + np.arange(5)


if __name__ == '__main__':
    print(matrix_row_plus_column())
