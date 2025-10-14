void main() {
  // Helper to print test results
  void runTest(List<int> nums, int k, List<int> expected) {
    print('Original: $nums, k: $k');
    Solution().rotate(nums, k); // using only nums and k
    print('Rotated : $nums');
    print('Expected: $expected');
    print(nums.toString() == expected.toString() ? '✅ Passed\n' : '❌ Failed\n');
  }

  // Negative numbers and mix

  runTest([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2]);
  runTest([1, 2, 3, 4, 5, 6], 3, [4, 5, 6, 1, 2, 3]);

  runTest([-1, -100, 3, 99], 3, [-100, 3, 99, -1]);

  runTest([-1, -100, 3, 99], 2, [3, 99, -1, -100]);

  runTest([-1, -2, -3, -4, -5], 2, [-4, -5, -1, -2, -3]);

  runTest([1, 2], 1, [2, 1]); // k = 1, small array
  runTest([1, 2], 0, [1, 2]); // k = 0, small array
  runTest([1, 2], 2, [1, 2]); // k = array.length, rotation equals length

  runTest([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]);

  // Edge cases
  runTest([1], 0, [1]); // single element, k = 0
  runTest([1], 1, [1]); // single element, k = 1

  // Large k values
  runTest([1, 2, 3], 4, [3, 1, 2]); // k > length (same as k=1)
  runTest([1, 2, 3], 100000, [3, 1, 2]); // k >> length (same as k=1)

  // Already rotated fully
  runTest([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]); // rotation equals length

  // Two elements, k = 1
  runTest([7, 8], 1, [8, 7]);
}
