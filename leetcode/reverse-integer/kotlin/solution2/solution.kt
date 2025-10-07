class Solution {
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
