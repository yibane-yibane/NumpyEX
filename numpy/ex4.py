import numpy as np


def cos_sin_tall_array():
    linspace = np.linspace(0, 1)
    cos = np.cos(linspace)
    sin = np.sin(linspace)

    return np.dstack((cos, sin))


def sum_rows_and_columns():
    random_matrix = np.random.rand(3, 5)

    entries_sum = random_matrix.sum()
    column_sum = random_matrix.sum(axis=0)
    row_sum = random_matrix.sum(axis=1)

    return entries_sum, row_sum, column_sum


def sort_matrix_second_column():
    random_matrix = np.random.rand(5, 5)

    return random_matrix[random_matrix[:, 1].argsort()]


if __name__ == '__main__':
    print(sort_matrix_second_column())
