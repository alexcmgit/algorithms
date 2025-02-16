class Solution {
    fun reverseWords(s: String): String {
        return s.trim().replace(Regex("\\s{2,}"), " ").split(Regex("\\s")).reversed().joinToString(" ")
    }
}
/**
 * You can edit, run, and share this code.
 * play.kotlinlang.org
 */
fun main() {
    print(Solution().productExceptSelf(intArrayOf(1,2,3,4)))
}

class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val lastIndex = nums.size - 1

        val size = if (nums.size % 2 == 0) nums.size else nums.size - 1

        val fromStartRes = IntArray(nums.size)
        fromStartRes[0] = nums.first()

        val fromEndRes = IntArray(nums.size)
        fromEndRes[lastIndex] = nums.last()

        for (i in 1..lastIndex - 1) {
            fromStartRes[i] = fromStartRes[i - 1] * nums[i]

            val j = lastIndex - i
            fromEndRes[j] = nums[j] * fromEndRes[j + 1]
        }

        val res = IntArray(nums.size)

        var start = 0
        var end = lastIndex

        res[start] = fromEndRes[lastIndex - 1]
        start++
        res[end] = fromStartRes[end - 1]
        end--

        while (true) {
            if (start >= nums.size) break
            if (end <= 0) break
            if (start >= end) break

            res[start] = fromStartRes[start - 1] * fromEndRes[start + 1]
            res[end] = fromStartRes[end - 1] * fromEndRes[end + 1]

            start++
            end++
        }

        return res
    }
}