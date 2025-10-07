class Solution {
    companion object {
        const val max = 2147483647
    }

    fun isPalindrome(o: Int): Boolean {
        if (o == 0) return true
        if (o < 0) return false

        var x = o
        var r = 0

        while (x > 0) {
            r = r + (x % 10)
            if (x > 9) {
                // This check optimizes cases where the palindrome causes an integer overflow
                if ((max - r) / 9 >= r) {
                    r = r * 10
                } else {
                    return false
                }
            }
            x = x / 10
        }

        return r == o
    }
}
