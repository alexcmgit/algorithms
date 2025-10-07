void main() {
  final solution = Solution();

  final testCases = [
    {'s': '42', 'expected': 42},
    {'s': '   -42', 'expected': -42},
    {'s': '1337c0d3', 'expected': 1337},
    {'s': '0-1', 'expected': 0},
    {'s': 'words and 987', 'expected': 0},
    {'s': '-91283472332', 'expected': -2147483648}, // underflow
    {'s': '91283472332', 'expected': 2147483647}, // overflow
    {'s': '+1', 'expected': 1},
    {'s': '+-12', 'expected': 0},
    {'s': '   +0 123', 'expected': 0},
  ];

  for (var i = 0; i < testCases.length; i++) {
    final s = testCases[i]['s'] as String;
    final expected = testCases[i]['expected'] as int;

    final result = solution.myAtoi(s);

    print('Test case ${i + 1}:');
    print('Input: s = "$s"');
    print('Output: $result');
    print('Expected: $expected');
    print(result == expected ? '✅ Passed\n' : '❌ Failed\n');
  }
}
