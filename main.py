import numpy as np
import matplotlib.pyplot as plt


class Matrix:
    def __init__(self):
        self.amount_of_points = 50
        self.coordinates = None
        self.colors = None

    def create_coordinates(self) -> np.ndarray:
        self.coordinates = np.random.rand(self.amount_of_points, 2) * 100  # Случайные координаты от 0 до 100
        return self.coordinates

    def create_colors(self) -> np.ndarray:
        self.colors = np.random.rand(self.amount_of_points, 3)
        return self.colors


matrix = Matrix()
for color in matrix.create_colors():
    plt.plot(matrix.create_coordinates(), matrix.create_coordinates(), c=color, zorder=-1)
plt.show()
