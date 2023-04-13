n = int(input())

points = [[*map(int, input().split())] for _ in range(0, n)]

dx = set(map(lambda p: p[0], points))
dy = set(map(lambda p: p[1], points))

print('YES' if len(dx) == 1 or len(dy) == 1 else 'NO')
