f = {0: 0, 1: 1, 2: 1, 3: 2}

# Same as solution 1 but it stores the fib results into a dict (hashmap)
# to avoid re-computing values n! times (which is quite expensive).
def fib(n: int) -> int:
    if n in f:
        return f[n]
    else:
        v = fib(n - 1) + fib(n - 2)
        f[n] = v
        return v
