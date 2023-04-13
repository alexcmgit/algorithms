PRECISION = 4.0

def deduce_square_root_of(x: float, guess: float | None = None):
    g = guess or x / 4
    r = g ** 2

    margin = pow(10, PRECISION)

    if abs(r - x) <= 1 / margin:
        return ((g * margin) // 1) / margin

    return deduce_square_root_of(x, (g + x / g) / 2)
