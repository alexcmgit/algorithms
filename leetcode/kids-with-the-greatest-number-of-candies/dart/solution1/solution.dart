class Solution {
  List<bool> kidsWithCandies(List<int> candies, int extraCandies) {
    final sorted = candies.toList()..sort();
    return candies.map((e) => (e + extraCandies) >= sorted.last).toList();
  }
}
