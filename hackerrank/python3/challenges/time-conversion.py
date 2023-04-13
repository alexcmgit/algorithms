h, m, sf = input().split(':')
s, f = [sf[:2], sf[2:]]

am = f == 'AM'

hh = (int(h) % 12) + (0 if am else 12)

print(f'{hh:02}:{m}:{s}')
