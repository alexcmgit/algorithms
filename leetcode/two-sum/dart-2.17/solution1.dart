class Solution {
  List<int> twoSum(List<int> nums, int target) {
    for (int i = 0; i < nums.length; i++) {
      final int current = nums[i];
      final int j = nums.lastIndexOf(target - current);

      if (j != -1 && j != i) {
        return <int>[i, j];
      }
    }
    return <int>[];
  }
}
