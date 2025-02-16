class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val res = IntArray(nums.size)
        var prev = 1
        
        for ((index, n) in nums.withIndex()) {
            res[index] = prev
            prev = prev * n
        }
        
       prev = 1
        
        for (index in (nums.size - 1) downTo 0) {
            val n = nums[index]
            res[index] = res[index] * prev
            prev = prev * n
        }
        
        return res
    }
}