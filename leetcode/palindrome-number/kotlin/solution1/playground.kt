fun main() {
    val solution = Solution()

    val testCases = listOf(
        Pair(121, true),           // palindrome
        Pair(-121, false),         // negative
        Pair(10, false),           // not palindrome
        Pair(0, true),             // single digit
        Pair(1221, true),          // even-length palindrome
        Pair(12321, true),         // odd-length palindrome
        Pair(1000021, false),      // leading zero when reversed
        Pair(2147447412, true)     // large palindrome near int limit
    )

    for ((index, testCase) in testCases.withIndex()) {
        val (x, expected) = testCase
        val result = solution.isPalindrome(x)

        println("Test case ${index + 1}:")
        println("Input: x = $x")
        println("Output: $result")
        println("Expected: $expected")
        println(if (result == expected) "✅ Passed\n" else "❌ Failed\n")
    }
}
