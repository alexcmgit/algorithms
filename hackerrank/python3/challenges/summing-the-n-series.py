t = int(input())

# I hate this solution. Yes I do, from my heart I HATE IT
# but my proud or whatever is it says 'Don't erase it, you should carry this shame for the rest of your life'
for _ in range(t):
  n = int(input())

  d = 2 # Common difference
  a1 = 1 # First term
  an = a1 + (n - 1) * d # N term of an AP
  sn = (n * (2 * a1 + (n - 1) * d)) >> 1 # Sum of the first N terms of an AP

  # Either it or directly 1000000007, I do not like to put large numbers like that
  # So I tried to re-write as 1e9 + 7
  # But Python said 'no' cause it results in an imprecision (by the + operator)
  # So to fix that I tried to use a bitwise sum operator (|) to sum the bits directly (1e9 | 7)
  # and Python again said 'not today bitch' cause the scientific notation (1e9) converts to a
  # float instead integer like a simple '7'
  # And it results on an exception saying 'really? are you trying to use the bitwise OR operator in a float?'
  # Then I re-wrote again as it is shown below, and I hate this solution, by this entire rabbit hole
  # but even more because after that I saw in the discussions section a guy saying
  # 'the solution is just n ** n % 1000000007' and indeed it is... then I simply smushed myself into the wall and turned off my PC from the plug but my proud do not allow me to use this simplest solution
  print(sn % (int(1e9) | 7))
