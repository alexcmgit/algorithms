class Solution {
  List<bool> kidsWithCandies(List<int> candies, int extraCandies) {
    int largest = 0;
    List<bool> ans = List.filled(candies.length, false);

    for (int i = 0; i < candies.length; i++) {
      if (candies[i] > largest) largest = candies[i];
    }

    for (int i = 0; i < candies.length; i++) {
      if (candies[i] + extraCandies >= largest) {
        ans[i] = true;
      }
    }

    return ans;
  }
}
