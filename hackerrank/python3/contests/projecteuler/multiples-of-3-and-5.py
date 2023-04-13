import sys

# Sum of a finite arithmetic progression where [r] is the common difference and [n] is the term count
def sum(r: int, n: int):
  # '>> 1' is the same as '/ 2' (replaced because Python just crash due float limitations on Big Ints like 1000000000000000000)
  return (n * (r + n * r)) >> 1

# This problem has two main solution: O(n) and O(1)
# a. O(n) is the 'brute force version' where we verify element by element and sum the values individually through a loop
# b. O(1) is the 'math version' where we use the AP formulas to calculate the sum of the sets in a linear time (no-loops, no brute-force, performance gain)
for _ in range(int(input())):
  n = int(input())
  
  # Exclude the last term (1000 turns 999, 10 turns 9)
  e = n - 1

  # Set of multiples of 3
  s_ca = sum(3, int(e / 3))

  # Set of multiples of 5
  s_cb = sum(5, int(e / 5))

  # Set of multiples of 15
  s_cc = sum(15, int(e / 15))

  # Total set equals to set A + set B but without the duplication of set C (then subtract this one)
  s = s_ca + s_cb - s_cc

  print(int(s))
