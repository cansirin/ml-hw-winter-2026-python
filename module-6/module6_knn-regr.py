import numpy as np


class KNNRegression:
    def __init__(self, n):
        self.points = np.empty((0, 2))
        self.n = n

    def insert(self, x, y):
        self.points = np.vstack([self.points, [x, y]])

    def predict(self, x, k):
        if k > self.n:
            raise ValueError(f"k ({k}) must be <= N ({self.n})")
        distances = np.abs(self.points[:, 0] - x)
        nearest_indices = np.argsort(distances)[:k]
        return np.mean(self.points[nearest_indices, 1])


N = int(input())
k = int(input())

knn = KNNRegression(N)
for i in range(N):
    x = float(input())
    y = float(input())
    knn.insert(x, y)

X = float(input())

try:
    result = knn.predict(X, k)
    print(result)
except ValueError as e:
    print(e)
