final Map<int, int> f = <int, int>{0: 0, 1: 1, 2: 1, 3: 2};

// Same as solution 1 but it stores the fib results into a dict (hashmap)
// to avoid re-computing values n! times (which is quite expensive).
int fib(int n) {
  if (f.containsKey(n)) return f[n]!;

  f[n] = fib(n - 2) + fib(n - 1);

  return f[n]!;
}
