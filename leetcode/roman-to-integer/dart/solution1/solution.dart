class Solution {
  int romanToInt(String s) {
    int t = 0;
    int v = 0;

    const m = <String?, int>{
      null: 0,
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
    };

    for (int i = 0; i < s.length; i++) {
      String c = s.charAt(i + 0);
      String? n = s.charAtOrNull(i + 1);

      v = v + m[c]!;

      if (m[n]! > m[c]!) {
        v = m[n]! - v;
        i = i + 1;
      }

      t = t + v;
      v = 0;
    }

    return t;
  }
}

extension on String {
  String? charAtOrNull(int index) {
    return index >= length || index < 0 ? null : charAt(index);
  }

  String charAt(int index) {
    return this[index];
  }
}
