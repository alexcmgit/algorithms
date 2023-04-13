def multiples_of_3_and_5_below(n: int) -> int:
    s = 0

    for i in range(3, n, 3):
        # Prefer to avoid stuff like "not i % 3" since 
        # it doesn't make sense at all to someone who doesn't know
        # 0 translates to False, and even who does, 
        # it adds an additional step to understand your code. 
        # 
        # Make it simple and stupid.
        if i % 3 == 0:
            s += i

    for i in range(5, n, 5):
        if i % 5 == 0:
            if i % 3 != 0: 
                s = s + i

    return int(s)
