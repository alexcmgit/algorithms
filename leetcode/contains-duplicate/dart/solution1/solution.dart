class Solution {
  bool containsDuplicate(List<int> nums) {
    final m = <int, bool>{};

    for(final n in nums) {
        if (m[n] ?? false) return true;
        m[n] = true;
    }

    return false;
  }
}