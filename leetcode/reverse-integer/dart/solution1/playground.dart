void main() {
  final solution = Solution();

  final testCases = [
    {'x': 123, 'expected': 321},
    {'x': -123, 'expected': -321},
    {'x': 120, 'expected': 21},
    {'x': 0, 'expected': 0},
    {'x': 1000, 'expected': 1},
    {'x': 1001, 'expected': 1001},
    {
      'x': 1534236469, // positive overflow
      'expected': 0,
    },
    {
      'x': -2147483412, // valid within 32-bit range
      'expected': -2143847412,
    },
    {
      'x': -1563847412, // negative overflow when reversed
      'expected': 0,
    },
  ];

  for (var i = 0; i < testCases.length; i++) {
    final x = testCases[i]['x'] as int;
    final expected = testCases[i]['expected'] as int;

    final result = solution.reverse(x);

    print('Test case ${i + 1}:');
    print('Input: x = $x');
    print('Output: $result');
    print('Expected: $expected');
    print(result == expected ? '✅ Passed\n' : '❌ Failed\n');
  }
}
