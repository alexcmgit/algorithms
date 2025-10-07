// Note: This algorithm simulates 32-bit overflow checks, but Dart uses 64-bit ints,
// so it doesn't actually enforce 32-bit runtime limits.
// TODO: Reimplement in a language with native 32-bit integer support for accurate runtime behavior.
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
        // If we multiply the current [r]esult by 10, will it overflow?
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
