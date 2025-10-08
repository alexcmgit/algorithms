class Solution {
  static const s = <String>['I', 'V', 'X', 'L', 'C', 'D', 'M'];

  String intToRoman(int n) {
    int i = 0;
    String r = '';

    while (n > 0 && i < s.length) {
      final c = n % 10;

      n = n ~/ 10;

      final (cs, hs, ns) = (
        s.elementAt(i),
        s.elementAtOrNull(i + 1),
        s.elementAtOrNull(i + 2),
      );

      final cr = hs != null && ns != null
          ? switch (c) {
              _ when c <= 3 => '$cs'.times(c),
              _ when c == 4 => '$cs$hs',
              _ when c == 9 => '$cs$ns',
              _ when c >= 5 => '$hs${cs.times(c - 5)}',
              _ => '',
            }
          : cs.times(c);

      r = cr + r;

      i = i + 2;
    }

    return r;
  }
}

extension StringRepeat on String {
  String times(int n) {
    if (n <= 0) return '';
    if (n == 1) return this;

    final buffer = StringBuffer();
    for (var i = 0; i < n; i++) {
      buffer.write(this);
    }
    return buffer.toString();
  }
}
