import numpy as np
import pytest
from hw_3_1.matrix import Matrix


def test_addition():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = Matrix(A) + Matrix(B)
    expected = np.array([[6, 8], [10, 12]])
    np.testing.assert_array_equal(result.data, expected)


def test_elementwise_multiplication():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = Matrix(A) * Matrix(B)
    expected = np.array([[5, 12], [21, 32]])
    np.testing.assert_array_equal(result.data, expected)


def test_matmul():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[2, 0], [1, 2]])
    result = Matrix(A) @ Matrix(B)
    expected = np.array([[4, 4], [10, 8]])
    np.testing.assert_array_equal(result.data, expected)


def test_add_invalid_dimensions():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        _ = Matrix(A) + Matrix(B)
