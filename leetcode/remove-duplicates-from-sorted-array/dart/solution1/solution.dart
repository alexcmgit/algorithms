class Solution {
  int removeDuplicates(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      if (nums.elementAt(i) == nums.elementAtOrNull(i + 1)) {
        nums.removeAt(i--);
      }
    }
    
    return nums.length;
  }
}
