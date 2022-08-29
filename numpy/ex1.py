import numpy as np
dsa
def ex1_create_subdivision(from_number=-1.3, to_number=2.5, subdivisions=64):
    return np.linspace(from_number, to_number, subdivisions)


def ex2_create_cycling_array(cycle=[1, 2, 3], n=3):
    return np.tile(cycle, n)


def ex3_create_odd_array(start=1, finish=20, addition=2):
    return np.arange(start, finish, addition)


def ex4_framed_one_matrix():
    matrix = np.ones((10,10))
    matrix[1:9, 1:9] = 0

    return matrix


def checkerboard_array():
    checkerboard = np.ones((8, 8))
    checkerboard[1::2, ::2] = 0
    checkerboard[::2, 1::2] = 0

    return checkerboard
jhg
