numbers = []
N = int(input())
for i in range(N):
    numbers.append(int(input()))
X = int(input())
if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)
