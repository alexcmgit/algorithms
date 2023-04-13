class Solution {
  int findKthLargest(List<int> nums, int k) {
    nums.sort((int a, int z) => z - a);
    return nums[k - 1];
  }
}
