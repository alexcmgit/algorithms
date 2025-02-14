class Solution {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        var free = 0

        for ((i, f) in flowerbed.withIndex()) {
            if (flowerbed[i] == 1) continue
            val before = flowerbed.elementAtOrNull(i - 1)
            val after = flowerbed.elementAtOrNull(i + 1)
            if (before == 1 || after == 1) continue
            flowerbed[i] = 1
            free = free + 1
            if (free >= n) return true
        }

        return free >= n
    }
}