class Solution {
  bool isPalindrome(int x) {
    if (x == 0) return true;
    if (x < 0) return false;

    int o = x;
    int r = 0;

    const max = 2147483647;
 
    while (x > 0) {
        r = r + (x % 10);
        if (x > 9) {
            if ((max - r) / 9 >= r) {
                r = r * 10;
            } else {
                return false;
            }
        }
        x = x ~/ 10;
    }
    
    return r == o;
  }
}
