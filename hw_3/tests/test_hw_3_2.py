import numpy as np
import pytest
from hw_3_2.matrix_mixin import Matrix
 

def test_get_set_and_shape():
    A = np.array([[1, 2], [3, 4]])
    m = Matrix(A)
    assert m.shape == (2, 2)
    assert m.get_item(0, 1) == 2
    m.set_item(0, 1, 10)
    assert m.get_item(0, 1) == 10


def test_str_representation():
    A = np.array([[1, 2], [3, 4]])
    m = Matrix(A)
    expected = np.array2string(A)
    assert str(m) == expected


def test_arithmetic_operations():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    m1 = Matrix(A)
    m2 = Matrix(B)

    add_result = m1 + m2
    expected_add = np.array([[6, 8], [10, 12]])
    np.testing.assert_array_equal(add_result.data, expected_add)

    mul_result = m1 * m2
    expected_mul = np.array([[5, 12], [21, 32]])
    np.testing.assert_array_equal(mul_result.data, expected_mul)

    matmul_result = m1 @ m2
    expected_matmul = A @ B
    np.testing.assert_array_equal(matmul_result.data, expected_matmul)
