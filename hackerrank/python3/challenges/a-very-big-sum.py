from functools import reduce

_ = int(input().strip())

print(reduce(lambda t, c: t + c, list(map(int, input().rstrip().split()))))
