import numpy as np


def ex1_cos_sin_tall_array():
    linspace = np.linspace(0, 1)
    cos = np.cos(linspace)
    sin = np.sin(linspace)

    return np.dstack((cos, sin))


def ex2_sum_rows_and_columns():
    random_matrix = np.random.rand(3, 5)

    entries_sum = random_matrix.sum()
    column_sum = random_matrix.sum(axis=0)
    row_sum = random_matrix.sum(axis=1)

    return entries_sum, row_sum, column_sum


def ex3_sort_matrix_second_column():
    random_matrix = np.random.rand(5, 5)

    return random_matrix[random_matrix[:, 1].argsort()]
