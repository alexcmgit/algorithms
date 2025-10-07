// Warning: since Dart uses 64-bit signed integers, this solution is not guaranteed to work in all languages.
// TODO: Impl. using a language that has built-in 32-bit signed integer representation.
class Solution {
  int reverse(int x) {
    if (x == 0) return 0;

    const min = 2147483648;
    const max = 2147483647;

    final s = x > 0 ? 1 : -1;
    final m = s == -1 ? min : max;

    int r = 0;
    int n = s == -1 ? x * -1 : x;

    while (n > 0) {
      final d = n % 10;

      // If we add the current [d]igit to the current [r]esult, will it overflow?
      if (m - d < r) {
        return 0;
      }

      r = r + d;

      if (n > 9) {
        // 'If we multiply the current [r]esult by 10, will it overflow?'
        //
        // Can also be implemented as:
        // if (r != 0 && (m - r) / r < 9) {
        //   return 0;
        // }
        // r = r * 10;
        if ((m - r) / 9 >= r) {
          r = r * 10;
        } else {
          return 0;
        }
      }

      n = n ~/ 10;
    }

    r = r * s;

    return r;
  }
}
