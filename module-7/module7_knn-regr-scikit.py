import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def knn_regression(X_train, y_train, k, x_query):
    if k > len(y_train):
        return None, None
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    prediction = knn.predict([[x_query]])[0]
    variance = np.var(y_train)
    return prediction, variance


def main():
    N = int(input())
    k = int(input())

    X_train = np.zeros((N, 1))
    y_train = np.zeros(N)

    for i in range(N):
        X_train[i, 0] = float(input())
        y_train[i] = float(input())

    X = float(input())

    prediction, variance = knn_regression(X_train, y_train, k, X)
    if prediction is None:
        print(f"Error: k ({k}) must be <= N ({N})")
    else:
        print(prediction)
        print(f"Variance: {variance}")


if __name__ == "__main__":
    main()
