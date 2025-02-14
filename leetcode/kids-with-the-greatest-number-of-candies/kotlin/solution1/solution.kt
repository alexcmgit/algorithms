class Solution {
    fun kidsWithCandies(candies: IntArray, extraCandies: Int): List<Boolean> {
        val greatest = candies.sorted().last()
        return candies.map { (it + extraCandies) >= greatest }
    }
}