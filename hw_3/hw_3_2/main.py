import numpy as np
from matrix_mixin import Matrix
 

def main():
    np.random.seed(0)
    A = np.random.randint(0, 10, (10, 10))
    B = np.random.randint(0, 10, (10, 10))

    matA = Matrix(A)
    matB = Matrix(B)

    result_add = matA + matB
    result_mul = matA * matB
    result_matmul = matA @ matB

    result_add.save_to_file(
        "Python_ITMO_DZ/hw_3/hw_3_2/artifacts/matrix_plus.txt")
    result_mul.save_to_file(
        "Python_ITMO_DZ/hw_3/hw_3_2/artifacts/matrix_mul.txt")
    result_matmul.save_to_file(
        "Python_ITMO_DZ/hw_3/hw_3_2/artifacts/matrix_at.txt")


if __name__ == "__main__":
    main()
