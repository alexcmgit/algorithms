class Solution {
    companion object {
        const val min: Int = -2147483648
        const val max: Int = 2147483647
    }

    fun reverse(x: Int): Int {
        val t = if (x < 0) x * -1 else x
        val p = if (x < 0) "-" else ""
        val r = t.toString().split("").reversed().joinToString("")

        return try {
            (p + r).toInt()
        } catch (e: NumberFormatException) {
            0
        }
    }
}
