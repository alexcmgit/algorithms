# Sorry for those who like 4-width but I can't, 2 is the law.

def printf(*values: object): print(*values, end='')

while (line := input()):
  n = int(line)

  if n == 0: break

  for i in range(n):
    for j in range(n):
      current = min(min(i, j), (n - 1) - max(i, j));
      printf(f'{current + 1}'.rjust(3 if j == 0 else 4));
    printf('\n')
  printf('\n')
