# kNN Classifier with GridSearchCV Test Runs

## Test 1: Clear Binary Split

**Input:**
```
10
1.0
0
2.0
0
3.0
0
4.0
0
5.0
0
6.0
1
7.0
1
8.0
1
9.0
1
10.0
1
4
2.5
0
7.5
1
5.5
1
3.5
0
```

- N=10 training points, M=4 test points
- Classes split at x~5.5: class 0 for x<=5, class 1 for x>=6
- Test point x=5.5 is on the boundary (true label 1)
- GridSearchCV tries k=1..8 with 5-fold CV

**Expected:** Best k: 1, Test Accuracy: 0.75
**Output:** Best k: 1, Test Accuracy: 0.75
**Status:** Pass

---

## Test 2: Perfect Separation, Larger Dataset

**Input:**
```
20
1.0
0
1.5
0
2.0
0
2.5
0
3.0
0
3.5
0
4.0
0
4.5
0
5.0
0
5.5
0
6.0
1
6.5
1
7.0
1
7.5
1
8.0
1
8.5
1
9.0
1
9.5
1
10.0
1
10.5
1
6
1.0
0
3.0
0
5.0
0
7.0
1
9.0
1
5.5
1
```

- N=20 training points, M=6 test points
- Clean split: class 0 for x<=5.5, class 1 for x>=6.0
- Test point x=5.5 labeled as class 1 (boundary case)
- GridSearchCV tries k=1..10 with 5-fold CV

**Expected:** Best k: 1, Test Accuracy: 0.8333333333333334
**Output:** Best k: 1, Test Accuracy: 0.8333333333333334
**Status:** Pass

---

## Test 3: Three Classes

**Input:**
```
15
1.0
0
2.0
0
3.0
0
4.0
0
5.0
0
6.0
1
7.0
1
8.0
1
9.0
1
10.0
1
11.0
2
12.0
2
13.0
2
14.0
2
15.0
2
6
2.0
0
7.0
1
13.0
2
5.5
0
10.5
2
8.0
1
```

- N=15 training points, M=6 test points
- Three classes: 0 (x=1..5), 1 (x=6..10), 2 (x=11..15)
- All test points are well within class regions
- GridSearchCV tries k=1..12 with 5-fold CV

**Expected:** Best k: 1, Test Accuracy: 0.8333333333333334
**Output:** Best k: 1, Test Accuracy: 0.8333333333333334
**Status:** Pass

---

## Test 4: Small Dataset (N=4)

**Input:**
```
4
1.0
0
2.0
0
3.0
1
4.0
1
2
1.5
0
3.5
1
```

- N=4 training points, M=2 test points
- cv_folds = min(5, 4, 2) = 2
- max_k = min(10, 4 - 2) = 2
- GridSearchCV tries k=1..2 with 2-fold CV

**Expected:** Best k: 1, Test Accuracy: 1.0
**Output:** Best k: 1, Test Accuracy: 1.0
**Status:** Pass

---

## Test 5: Noisy Data

**Input:**
```
12
1.0
0
2.0
0
3.0
1
4.0
0
5.0
0
6.0
1
7.0
1
8.0
0
9.0
1
10.0
1
11.0
1
12.0
1
4
2.0
0
6.0
1
9.0
1
4.0
0
```

- N=12 training points, M=4 test points
- Noisy labels: x=3 and x=8 have "wrong" labels for their region
- Higher k values should smooth out the noise
- GridSearchCV tries k=1..9 with 5-fold CV

**Expected:** Best k: 7, Test Accuracy: 1.0
**Output:** Best k: 7, Test Accuracy: 1.0
**Status:** Pass

---

## Summary

| Test | Scenario | Best k | Test Accuracy |
|------|----------|--------|---------------|
| 1 | Clear binary split | 1 | 0.75 |
| 2 | Perfect separation, larger dataset | 1 | 0.8333 |
| 3 | Three classes | 1 | 0.8333 |
| 4 | Small dataset (N=4) | 1 | 1.0 |
| 5 | Noisy data | 7 | 1.0 |