import numpy as np
 

class Matrix:
    def __init__(self, data):
        if isinstance(data, np.ndarray):
            self.data = data.copy()
        else:
            self.data = np.array(data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError(
                "Для сложения матрицы должны быть одинаковой формы")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError(
                "Для поэлементного умножения матрицы должны быть одинаковой формы")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Неверная размерность для матричного умножения")
        return Matrix(np.matmul(self.data, other.data))

    def __str__(self):
        return str(self.data)

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.data))
