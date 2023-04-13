def sumdigits(x: int):
  s = 0

  while (x != 0):
    s = s + int(x % 10)
    x = x // 10

  return s

n = int(input())
sum = [n, sumdigits(n)]

for k in range(n // 2, 0, -1):
  if n % k == 0:
    c = sumdigits(k)
    if c >= sum[1]:
      sum = [k, c]

print(sum[0])
