class Solution {
  int maxDiff(int n) {
    final digits = n.toDigits().toList();

    int maxFrom = digits.first;
    const maxTo = 9;

    for (final d in digits) {
      if (d == 9) continue;

      maxFrom = d;
      break;
    }

    int minFrom = digits.first;
    int minTo = 1;

    for (final (i, d) in digits.indexed) {
      if (d == 0) continue;
      if (d == 1) continue;

      minFrom = d;

      if (i != 0) {
        minTo = 0;
      }

      break;
    }

    return digits.map((e) => e == maxFrom ? maxTo : e).mountToInt() -
        digits.map((e) => e == minFrom ? minTo : e).mountToInt();
  }
}

int? largestPowerOfOrNull(int x, {int base = 10}) {
  try {
    return largestPowerOf(x, base: base);
  } on Exception {
    return null;
  }
}

int largestPowerOf(int x, {int base = 10}) {
  final (_, power) = largestExponentAndPowerOf(x, base: base);
  return power;
}

(int exponent, int power) largestExponentAndPowerOf(int x, {int base = 10}) {
  int exponent = 0;
  int power = 1;

  while (power * base <= x) {
    power = power * base;
    exponent = exponent + 1;
  }

  return (exponent, power);
}

extension DigitOperations on int {
  Iterable<int> toDigits({int radix = 10}) sync* {
    int self = abs();

    int power = largestPowerOfOrNull(self, base: radix) ?? 1;

    do {
      yield self ~/ power;
      self = self % power;
      power = power ~/ radix;
    } while (power > 0);
  }
}

extension DigitOperationsIterable<T extends Iterable<int>> on T {
  int mountToInt({int radix = 10}) {
    int mounted = 0;

    for (final digit in this) {
      mounted = mounted * radix;
      mounted = mounted + digit.abs();
    }

    return mounted;
  }
}
