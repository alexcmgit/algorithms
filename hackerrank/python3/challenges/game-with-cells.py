from math import ceil

(n, m) = map(lambda x: ceil(int(x) / 2), input().split())

print(n * m)
