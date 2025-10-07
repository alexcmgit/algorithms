void main() {
  final solution = Solution();

  final testCases = [
    {'x': 121, 'expected': true},          // palindrome
    {'x': -121, 'expected': false},        // negative
    {'x': 10, 'expected': false},          // not palindrome
    {'x': 0, 'expected': true},            // single digit, palindrome
    {'x': 1221, 'expected': true},         // even-length palindrome
    {'x': 12321, 'expected': true},        // odd-length palindrome
    {'x': 1000021, 'expected': false},     // leading zero when reversed
    {'x': 2147447412, 'expected': true},   // large palindrome near int limit
  ];

  for (var i = 0; i < testCases.length; i++) {
    final x = testCases[i]['x'] as int;
    final expected = testCases[i]['expected'] as bool;

    final result = solution.isPalindrome(x);

    print('Test case ${i + 1}:');
    print('Input: x = $x');
    print('Output: $result');
    print('Expected: $expected');
    print(result == expected ? '✅ Passed\n' : '❌ Failed\n');
  }
}
