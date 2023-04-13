from math import factorial as fac

# Order matter? No | Repetition allowed? No
# See https://www.freecodecamp.org/news/content/images/2020/04/Permutations3.png
for _ in range(int(input())):
  n, r = [int(input()), 2]
    
  if n < r: print('0' if n == 1 else '1')
  else: print(fac(n) // (fac(r) * fac(n - r)))
