n = int(input())

def even(x: int): return x % 2 == 0
def odd(x: int): return not even(x)

if odd(n) or (even(n) and n in range(6, 20 + 1)): print('Weird')
else: print('Not Weird')
