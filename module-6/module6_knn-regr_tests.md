# k-NN Regression Test Runs

## Test 1: k=1 (Nearest Neighbor)

**Input:**
```
3
1
1
10
2
20
3
30
1.5
```

- N=3, k=1
- Points: (1,10), (2,20), (3,30)
- Query X=1.5
- Nearest: x=1 (distance 0.5) → y=10

**Expected:** 10.0
**Output:** 10.0
**Status:** Pass

---

## Test 2: k=3 (Average All Points)

**Input:**
```
3
3
1
10
2
20
3
30
2
```

- N=3, k=3
- Points: (1,10), (2,20), (3,30)
- Query X=2
- All 3 neighbors: y values 10, 20, 30 → mean = 20.0

**Expected:** 20.0
**Output:** 20.0
**Status:** Pass

---

## Test 3: k=2 with 4 Points

**Input:**
```
4
2
1
10
3
30
5
50
7
70
4
```

- N=4, k=2
- Points: (1,10), (3,30), (5,50), (7,70)
- Query X=4
- 2 nearest: x=3 (distance 1, y=30), x=5 (distance 1, y=50) → mean = 40.0

**Expected:** 40.0
**Output:** 40.0
**Status:** Pass

---

## Test 4: Error Case (k > N)

**Input:**
```
2
5
1
10
2
20
1.5
```

- N=2, k=5
- k > N → should print error

**Expected:** Error message
**Output:** k (5) must be <= N (2)
**Status:** Pass

---

## Test 5: Float Coordinates

**Input:**
```
3
2
1.5
2.3
3.7
4.1
5.2
6.8
3.5
```

- N=3, k=2
- Points: (1.5, 2.3), (3.7, 4.1), (5.2, 6.8)
- Query X=3.5
- Distances: x=1.5 → 2.0, x=3.7 → 0.2, x=5.2 → 1.7
- 2 nearest: x=3.7 (y=4.1), x=5.2 (y=6.8) → mean = 5.45

**Expected:** 5.45
**Output:** 5.449999999999999
**Status:** Pass

---

## Summary

| Test | Scenario | Expected | Output | Status |
|------|----------|----------|--------|--------|
| 1 | k=1, nearest neighbor | 10.0 | 10.0 | Pass |
| 2 | k=3, average all points | 20.0 | 20.0 | Pass |
| 3 | k=2, four points | 40.0 | 40.0 | Pass |
| 4 | k > N, error case | error msg | k (5) must be <= N (2) | Pass |
| 5 | Float coordinates, k=2 | 5.45 | 5.449999999999999 | Pass |

All 5 tests passed.
