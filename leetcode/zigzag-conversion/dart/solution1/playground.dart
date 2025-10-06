void main() {
  final solution = Solution();

  final testCases = [
    {
      's': 'PAYPALISHIRING',
      'numRows': 3,
      'expected': 'PAHNAPLSIIGYIR',
    },
    {
      's': 'PAYPALISHIRING',
      'numRows': 4,
      'expected': 'PINALSIGYAHRPI',
    },
    {
      's': 'A',
      'numRows': 1,
      'expected': 'A',
    },
  ];

  for (var i = 0; i < testCases.length; i++) {
    final s = testCases[i]['s'] as String;
    final numRows = testCases[i]['numRows'] as int;
    final expected = testCases[i]['expected'] as String;

    final result = solution.convert(s, numRows);

    print('Test case ${i + 1}:');
    print('Input: s = "$s", numRows = $numRows');
    print('Output: "$result"');
    print('Expected: "$expected"');
    print(result == expected ? '✅ Passed\n' : '❌ Failed\n');
  }
}
