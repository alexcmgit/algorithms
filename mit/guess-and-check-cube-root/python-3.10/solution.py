PRECISION = 2

def guess_cube_root_of(x: float, precision: float, start: float | None = None, end: float | None = None):
    y = abs(x)

    start = start or 0
    end = end or y
    mid = start + (end - start) / 2

    error = y - mid ** 3
    exceeded = error < 0

    p = 10 ** precision
    margin = 1 / p

    if abs(error) <= margin:
        return -mid if x < 0 else mid

    if exceeded:
        end = mid
    else:
        start = mid

    return guess_cube_root_of(x, precision, start, end)
