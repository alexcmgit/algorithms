class Solution {
    companion object {
        const val min: Int = -2147483648
        const val max: Int = 2147483647
    }

    fun reverse(x: Int): Int {
        if (x == 0) return 0

        val s = if (x > 0) 1 else -1

        var r = 0
        var n = x

        while (n > 0 || n < 0) {
            val d = n % 10

            // If we add the current [d]igit to the current [r]esult, will it overflow?
            if (s == 1) {
                if (max - d < r) {
                    return 0
                }
            } else {
                if (min - d > r) {
                    return 0
                }
            }

            r = r + d

            if (n > 9 || n < -9) {
                // If we multiply the current [r]esult by 10, will it overflow?
                if (s == 1) {
                    if ((max - r) / 9 >= r) {
                        r = r * 10
                    } else {
                        return 0
                    }
                } else {
                    if ((min - r) / 9 <= r) {
                        r = r * 10
                    } else {
                        return 0
                    }
                }
            }

            n = n / 10
        }

        return r
    }
}
