def signv(n: str):
  if n == '+':
    return 1
  elif n == '-':
    return -1
  return 0

def solve(eq: str):
  (lh, rh) = map(lambda s: s.strip().split(' '), eq.split('='))

  return process(lh, rh, 0 if any(e == 'x' for e in lh) else 1)

def process(lh: list, rh: list, x: int):
  (ls, rs) = [resolve(lh), resolve(rh)]
  (l, r, fac) = [ls[0], rs[0], ls[1] if x == 0 else rs[1]]

  return (r + -l if x == 0 else l + -r) * fac

def resolve(exp: list):
  (previous, index, sign) = [0, 0, 1]
  
  def next():
      return exp[index + 1]
    
  while index < len(exp):
    csign = signv(exp[index])

    if exp[index] == 'x':
      pass
    elif csign != 0:
      if next() == 'x':
        sign = csign
      elif previous == 0:
        previous += int(f'{exp[index]}{next()}')
      else:
        previous += int(f'{exp[index]}{next()}')
    elif index == 0:
      previous = int(exp[index])

    index += 1

  return [previous, sign]
