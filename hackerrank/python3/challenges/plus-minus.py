n = int(input())
ratios = [0, 0, 0]

def add(i: int): ratios[i] += 1

for e in map(lambda e: int(e), input().split()): add(0 if e > 0 else 1 if e < 0 else 2)
for r in ratios: print(f'{(r / n):.6f}')
