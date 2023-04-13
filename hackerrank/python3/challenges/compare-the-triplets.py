ta = [int(e) for e in input().split()]
tb = [int(e) for e in input().split()]

sa = 0
sb = 0

for i in range(3):
  if ta[i] > tb[i]:
    sa += 1
  elif ta[i] < tb[i]:
     sb += 1

print(f'{sa} {sb}')
