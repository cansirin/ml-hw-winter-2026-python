class NumberList:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        return -1


nl = NumberList()
N = int(input())
for i in range(N):
    nl.insert(int(input()))
X = int(input())
print(nl.search(X))
