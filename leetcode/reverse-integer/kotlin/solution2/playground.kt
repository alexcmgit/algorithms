fun main() {
    val solution = Solution()

    val testCases = listOf(
        mapOf("x" to -10, "expected" to -1),
        mapOf("x" to 10, "expected" to 1),
        mapOf("x" to 123, "expected" to 321),
        mapOf("x" to -123, "expected" to -321),
        mapOf("x" to 120, "expected" to 21),
        mapOf("x" to 0, "expected" to 0),
        mapOf("x" to 1534236469, "expected" to 0), // overflow case
        mapOf("x" to -2147483412, "expected" to -2143847412)
    )

    for ((index, test) in testCases.withIndex()) {
        val x = test["x"] as Int
        val expected = test["expected"] as Int

        val result = solution.reverse(x)

        println("Test case ${index + 1}:")
        println("Input: x = $x")
        println("Output: $result")
        println("Expected: $expected")
        if (result == expected) println("✅ Passed\n") else println("❌ Failed\n")
    }
}
