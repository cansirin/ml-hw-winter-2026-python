from module5_mod import NumberList

nl = NumberList()
N = int(input())
for i in range(N):
    nl.insert(int(input()))
X = int(input())
print(nl.search(X))
