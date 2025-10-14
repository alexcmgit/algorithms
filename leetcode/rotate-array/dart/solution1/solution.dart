class Solution {
  void rotate(List<int> nums, int k, {int? index, int? prevValue}) {
    k = k % nums.length;
    if (k == 0) return;

    int count = 0;
    int start = 0;

    do {
      int current = start;
      int prev = nums[start];

      do {
        int next = (current + k) % nums.length;
        int temp = nums[next];
        nums[next] = prev;
        prev = temp;
        current = next;
        count++;
      } while (start != current);

      start = start + 1;
    } while (count < nums.length);
  }
}
