int _recursiveFactorial(int n) => n == 1 ? n : n * _recursiveFactorial(n - 1);

int permutationCount(int x) => x == 0 ? 1 : _recursiveFactorial(x);
