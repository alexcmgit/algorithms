from functools import reduce

sort = sorted([int(e) for e in input().split()])

print(f'{reduce(lambda t, c: t + c, sort[:len(sort) - 1])}\
 {reduce(lambda t, c: t + c, sort[1:])}')
