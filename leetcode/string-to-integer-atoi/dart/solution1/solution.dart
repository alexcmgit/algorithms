class Solution {
  int myAtoi(String s) {
    int? n;
    int? g;

    final dr = RegExp(r'[0-9]');
    final ndr = RegExp(r'[^0-9\-+\s]');

    const max = 2147483647;
    const min = -2147483648;

    for (int i = 0; i < s.length; i++) {
      if (ndr.hasMatch(s[i])) break;

      if (n == null && s[i] == ' ') {
        continue;
      }

      if (n == null && s[i] == '-') {
        g = -1;
        n = 0;
        continue;
      }

      if (n == null && s[i] == '+') {
        g = 1;
        n = 0;
        continue;
      }

      if (n == null && dr.hasMatch(s[i])) {
        g = g ?? 1;
        n = _toInt(s[i]) * g;
        continue;
      }

      if (n != null) {
        if (!dr.hasMatch(s[i])) {
          break;
        }

        if (g == 1) {
          if ((max - n) / 9 < n) {
            return max;
          } else {
            n = n * 10;
          }
        } else {
          if ((min - n) / 9 > n) {
            return min;
          } else {
            n = n * 10;
          }
        }

        final d = _toInt(s[i]) * g!;

        if (g == 1) {
          if (max - d < n) {
            return max;
          } else {
            n = n + d;
          }
        } else {
          if (min - d > n) {
            return min;
          } else {
            n = n + d;
          }
        }

        continue;
      }
    }

    return n ?? 0;
  }

  int _toInt(String c) => switch (c) {
    '0' => 0,
    '1' => 1,
    '2' => 2,
    '3' => 3,
    '4' => 4,
    '5' => 5,
    '6' => 6,
    '7' => 7,
    '8' => 8,
    '9' => 9,
    _ => 0,
  };
}
