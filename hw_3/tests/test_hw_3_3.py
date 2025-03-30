import numpy as np
import pytest
from hw_3_3.matrix_hash import Matrix, MULT_CACHE


def test_hash_value():
    A_data = np.array([[1, 2], [3, 4]])
    A = Matrix(A_data)
    expected_hash = int((np.sum(A_data[0]) + A_data.shape[0]) % 10)
    assert hash(A) == expected_hash


def test_caching_mechanism():

    MULT_CACHE.clear()

    A_data = np.array([[1, 2], [3, 4]])
    B_data = np.array([[5, 6], [7, 8]])
    A = Matrix(A_data)
    B = Matrix(B_data)

    result1 = A @ B
    key = (hash(A), hash(B))
    assert key in MULT_CACHE

    result2 = A @ B
    np.testing.assert_array_equal(result1.data, result2.data)


def test_hash_collision_and_different_multiplication_results():
    MULT_CACHE.clear()

    A_data = np.array([[1, 2],
                       [3, 4]])
    C_data = np.array([[0, 3],
                       [3, 4]])

    B_data = np.array([[5, 6],
                       [7, 8]])
    D_data = B_data.copy()

    A = Matrix(A_data)
    B = Matrix(B_data)
    C = Matrix(C_data)
    D = Matrix(D_data)

    assert hash(A) == hash(C)

    AB = A @ B

    MULT_CACHE.clear()

    CD = C @ D

    assert not np.array_equal(
        AB.data, CD.data)
