import numpy as np
 

class SaveToFileMixin:
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


class PrettyPrintMixin:
    def __str__(self):
        return np.array2string(self.data)


class GetSetMixin:
    @property
    def shape(self):
        return self.data.shape

    def get_item(self, i, j):
        return self.data[i, j]

    def set_item(self, i, j, value):
        self.data[i, j] = value


class MatrixArithmeticMixin:
    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError(
                "Для сложения матрицы должны быть одинаковой формы")
        return self.__class__(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError(
                "Для поэлементного умножения матрицы должны быть одинаковой формы")
        return self.__class__(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Неверная размерность для матричного умножения")
        return self.__class__(np.matmul(self.data, other.data))


class Matrix(SaveToFileMixin, PrettyPrintMixin, GetSetMixin, MatrixArithmeticMixin):
    def __init__(self, data):
        if isinstance(data, np.ndarray):
            self.data = data.copy()
        else:
            self.data = np.array(data)
