import numpy as np
from matrix_hash import Matrix, MULT_CACHE
import os


def main():
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

    A.save_to_file("Python_ITMO_DZ/hw_3/hw_3_3/artifacts/A.txt")
    B.save_to_file("Python_ITMO_DZ/hw_3/hw_3_3/artifacts/B.txt")
    C.save_to_file("Python_ITMO_DZ/hw_3/hw_3_3/artifacts/C.txt")
    D.save_to_file("Python_ITMO_DZ/hw_3/hw_3_3/artifacts/D.txt")

    AB = A @ B
    CD = C @ D

    AB.save_to_file("Python_ITMO_DZ/hw_3/hw_3_3/artifacts/AB.txt")
    CD.save_to_file("Python_ITMO_DZ/hw_3/hw_3_3/artifacts/CD.txt")

    with open("Python_ITMO_DZ/hw_3/hw_3_3/artifacts/hash.txt", "w") as f:
        f.write(f"hash(A): {hash(A)}\n")
        f.write(f"hash(C): {hash(C)}\n")
        f.write(f"hash(B): {hash(B)}\n")
        f.write(f"hash(D): {hash(D)}\n")

    print("Результат A @ B:")
    print(AB)
    print("\nРезультат C @ D:")
    print(CD)
    print("\nПроверьте файл hash.txt для сравнения хэшей.")


if __name__ == "__main__":
    main()
