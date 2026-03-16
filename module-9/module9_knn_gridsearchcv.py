import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


def main():
    N = int(input())

    X_train = np.zeros((N, 1))
    y_train = np.zeros(N, dtype=int)

    for i in range(N):
        X_train[i, 0] = float(input())
        y_train[i] = int(input())

    M = int(input())

    X_test = np.zeros((M, 1))
    y_test = np.zeros(M, dtype=int)

    for i in range(M):
        X_test[i, 0] = float(input())
        y_test[i] = int(input())

    min_class_count = min(np.bincount(y_train))
    cv_folds = min(5, N, min_class_count)
    max_k = min(10, N - (-(-N // cv_folds)))
    param_grid = {"n_neighbors": list(range(1, max_k + 1))}
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv=cv_folds, scoring="accuracy")
    grid_search.fit(X_train, y_train)

    best_k = grid_search.best_params_["n_neighbors"]
    y_pred = grid_search.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    print(f"Best k: {best_k}")
    print(f"Test Accuracy: {test_accuracy}")


if __name__ == "__main__":
    main()
