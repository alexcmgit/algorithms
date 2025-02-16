class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val lastIndex = nums.size - 1

        val fromStartRes = IntArray(nums.size) { 1 }
        val fromEndRes = IntArray(nums.size) { 1 }

        for (i in 0..lastIndex) {
            fromStartRes[i] = (fromStartRes.elementAtOrNull(i - 1) ?: 1) * nums[i]

            val j = lastIndex - i
            fromEndRes[j] = nums[j] * (fromEndRes.elementAtOrNull(j + 1) ?: 1)
        }

        fromStartRes[lastIndex] = fromStartRes[lastIndex - 1] * nums[lastIndex]
        fromEndRes[0] = fromEndRes[1] * nums[0]
        
        val res = IntArray(nums.size)

        var start = 0
        var end = lastIndex

        while (true) {
            if (start == nums.size) break
            if (end == -1) break
            if (start > end) break

            res[start] = (fromStartRes.elementAtOrNull(start - 1) ?: 1) * (fromEndRes.elementAtOrNull(start + 1) ?: 1)
            res[end] = (fromStartRes.elementAtOrNull(end - 1) ?: 1) * (fromEndRes.elementAtOrNull(end + 1) ?: 1)

            start++
            end--
        }
        
        return res
    }
}