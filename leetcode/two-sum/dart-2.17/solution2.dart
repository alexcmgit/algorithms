// Nested loop -> O(n²).
class Solution {
  List<int> twoSum(List<int> nums, int target) {
    for (int i = 0; i < nums.length; i++) {
      for (int j = 0; j < nums.length; j++) {
        if (j == i) continue;

        if (nums[i] + nums[j] == target) {
          return <int>[i, j];
        }
      }
    }
    return <int>[];
  }
}
