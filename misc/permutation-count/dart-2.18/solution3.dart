import 'dart:math';

double _logBase(num x, num base) => log(x) / log(base);
double _log2(num x) => _logBase(x, 2);

/// Original source:
/// - https://www.luschny.de/math/factorial/FastFactorialFunctions.htm.
/// - https://www.luschny.de/math/factorial/csharp/FactorialSplit.cs.html.
int _factorialSplit(int n) {
  if (n < 2) return 1;

  int p = 1;
  int r = 1;
  int currentN = 1;

  int h = 0;
  int shift = 0;
  int high = 1;

  int log2n = _log2(n).floor();

  int product(int n) {
    final int m = n ~/ 2;
    if (m == 0) return currentN += 2;
    if (n == 2) return (currentN += 2) * (currentN += 2);
    return product(n - m) * product(m);
  }

  while (h != n) {
    shift += h;
    h = n >> log2n--;
    int len = high;
    high = (h - 1) | 1;
    len = (high - len) ~/ 2;

    if (len > 0) {
      p *= product(len);
      r *= p;
    }
  }

  return r << shift;
}

int permutationCount(int x) => _factorialSplit(x);
