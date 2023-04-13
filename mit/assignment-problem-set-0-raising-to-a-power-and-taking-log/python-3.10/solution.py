import math

def square(x: int, y: int) -> int:
    return x ** y

def logBase2(x: int):
    return math.log(x, 2)

def assignment(x: int, y: int):
    return x ** y, math.log(x, 2)

if __name__ == '__main__':
    x = int(input('Type X: '))
    y = int(input('Type Y: '))

    print(*assignment(x, y), sep='\n')
