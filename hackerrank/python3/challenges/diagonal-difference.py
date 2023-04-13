def diagonalDifference(arr, n):
  mtotal = 0
  stotal = 0

  for i in range(n):
    mtotal += arr[i][i]
    stotal += arr[n - 1 - i][i]

  return abs(mtotal - stotal)

n = int(input())

arr = [
  list(map(int, input().split())) for _ in range(n)
]

print(diagonalDifference(arr, n))
