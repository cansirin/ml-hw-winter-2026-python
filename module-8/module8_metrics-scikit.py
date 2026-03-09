import numpy as np
from sklearn.metrics import precision_score, recall_score


def main():
    N = int(input())

    y_true = np.zeros(N, dtype=int)
    y_pred = np.zeros(N, dtype=int)

    for i in range(N):
        y_true[i] = int(input())
        y_pred[i] = int(input())

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


if __name__ == "__main__":
    main()
