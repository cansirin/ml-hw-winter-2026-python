# Precision & Recall (Scikit-learn) Test Runs

## Test 1: Mixed (TP=1, FP=1, FN=1, TN=1)

**Input:**
```
4
1
1
1
0
0
1
0
0
```

- N=4
- Points: (1,1), (1,0), (0,1), (0,0) → TP=1, FN=1, FP=1, TN=1
- Precision = TP/(TP+FP) = 1/2 = 0.5
- Recall = TP/(TP+FN) = 1/2 = 0.5

**Expected:** Precision: 0.5, Recall: 0.5
**Output:** Precision: 0.5, Recall: 0.5

---

## Test 2: Perfect Classification

**Input:**
```
3
1
1
1
1
0
0
```

- N=3
- Points: (1,1), (1,1), (0,0) → TP=2, FN=0, FP=0, TN=1
- Precision = 2/2 = 1.0
- Recall = 2/2 = 1.0

**Expected:** Precision: 1.0, Recall: 1.0
**Output:** Precision: 1.0, Recall: 1.0

---

## Test 3: 2 TP, 1 FP, 1 FN

**Input:**
```
5
1
1
1
1
0
1
1
0
0
0
```

- N=5
- Points: (1,1), (1,1), (0,1), (1,0), (0,0) → TP=2, FP=1, FN=1, TN=1
- Precision = 2/3 = 0.6667
- Recall = 2/3 = 0.6667

**Expected:** Precision: 0.6667, Recall: 0.6667
**Output:** Precision: 0.6666666666666666, Recall: 0.6666666666666666

---

## Test 4: All Predicted Positive

**Input:**
```
3
0
1
0
1
1
1
```

- N=3
- Points: (0,1), (0,1), (1,1) → TP=1, FP=2, FN=0, TN=0
- Precision = 1/3 = 0.3333
- Recall = 1/1 = 1.0

**Expected:** Precision: 0.3333, Recall: 1.0
**Output:** Precision: 0.3333333333333333, Recall: 1.0

---

## Test 5: No Predicted Positives

**Input:**
```
3
1
0
1
0
0
0
```

- N=3
- Points: (1,0), (1,0), (0,0) → TP=0, FP=0, FN=2, TN=1
- Precision = 0/0 → 0.0 (undefined, set to 0)
- Recall = 0/2 = 0.0

**Expected:** Precision: 0.0, Recall: 0.0
**Output:** Precision: 0.0, Recall: 0.0

---

## Summary

| Test | Scenario | Precision | Recall |
|------|----------|-----------|--------|
| 1 | Mixed TP/FP/FN/TN | 0.5 | 0.5 |
| 2 | Perfect classification | 1.0 | 1.0 |
| 3 | 2 TP, 1 FP, 1 FN | 0.6667 | 0.6667 |
| 4 | All predicted positive | 0.3333 | 1.0 |
| 5 | No predicted positives | 0.0 | 0.0 |