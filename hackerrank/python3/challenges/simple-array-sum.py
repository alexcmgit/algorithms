from functools import reduce

_ = input()

print(reduce(lambda t, c: t + c, map(int, input().split())))
