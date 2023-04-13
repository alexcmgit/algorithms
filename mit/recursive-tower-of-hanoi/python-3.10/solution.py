def print_move(fr: int, to: int) -> None:
    print(f'Moving from {fr} to {to}')

def tower_of_hanoi(n: int, fr: int, to: int, spare: int) -> None:
    if n == 1:
        print_move(fr, to)
    else:
        tower_of_hanoi(n - 1, fr, spare, to)
        tower_of_hanoi(1, fr, to, spare)
        tower_of_hanoi(n - 1, spare, to, fr)

tower_of_hanoi(3, 0, 1, 2)