class Solution {
  int maxProfit(List<int> prices) {
    if (prices.length == 1) return 0;

    int min = prices.first;

    int p = 0;

    for (int i = 1; i < prices.length; i++) {
        int c = prices[i];

        if (c <= min) {
            min = c;
            continue;
        }

        if (c - min > p) {
            p = c - min;
        }
    }

    return p;
  }
}
