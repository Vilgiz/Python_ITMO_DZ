import numpy as np

MULT_CACHE = {}


class HashMixin:
    def __hash__(self):
        # берём сумму элементов первой строки + число строк, затем по модулю 10.
        return int((np.sum(self.data[0]) + self.data.shape[0]) % 10)


class MatrixCacheMixin:
    def __matmul__(self, other):
        key = (hash(self), hash(other))
        if key in MULT_CACHE:
            print(f"Используется кэшированный результат для ключа {key}")
            return MULT_CACHE[key]
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Неверная размерность для матричного умножения")
        result = Matrix(np.matmul(self.data, other.data))
        MULT_CACHE[key] = result
        return result


class Matrix(HashMixin, MatrixCacheMixin):
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

    def __str__(self):
        return np.array2string(self.data)

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.data))
