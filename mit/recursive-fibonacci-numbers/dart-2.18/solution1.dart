// https://en.wikipedia.org/wiki/Fibonacci_number
// 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
// WARN: This solution can take a looooong time for large [n] values (>= 50).
int fib(int n) {
  if (n == 0) return 0;

  if (n == 1 || n == 2) return 1;

  return fib(n - 2) + fib(n - 1);
}
