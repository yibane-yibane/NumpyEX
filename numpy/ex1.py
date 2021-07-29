import numpy as np


def create_subdivision(from_number=-1.3, to_number=2.5, subdivisions=64):
    return np.linspace(from_number, to_number, subdivisions)


def create_cycling_array(cycle=[1, 2, 3], n=3):
    return np.array(cycle * n)


def create_odd_array(start=1, finish=20, addition=2):
    return np.arange(start, finish, addition)


def framed_one_matrix():
    matrix = np.zeros((10, 10))
    matrix[0:10, 0] = 1
    matrix[0:10, 9] = 1
    matrix[0, 0:10] = 1
    matrix[9, 0:10] = 1

    return matrix


def checkerboard_array():
    checkerboard = np.ones((8, 8))
    checkerboard[1::2, ::2] = 0
    checkerboard[::2, 1::2] = 0

    return checkerboard




if __name__ == '__main__':
    print(create_cycling_array())