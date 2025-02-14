class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val seen = mutableMapOf<Int, Boolean>()
        for (n in nums) {
            if (seen[n] ?: false) {
                return true
            }
            seen[n] = true
        }
        return false
    }
}