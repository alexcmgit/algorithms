class Solution {
    fun digitsOf(n: Int): List<Int> {
        var t = n
        val mut = mutableListOf<Int>()
        while (t >= 1) {
            mut.add(t % 10)
            t = t / 10
        }
        return mut.reversed()
    }

    fun mountDigits(digits: List<Int>): Int {
        return digits.joinToString("").toInt()
    }

    fun replaceDigits(digits: List<Int>, from: Int, to: Int): Pair<Boolean, List<Int>> {
        if (digits.first() == from && to == 0) {
            return false to digits
        }

        return true to digits.map { if (it == from) to else it }
    }

    fun minValueReplacing(digits: List<Int>): Int {
        var low = mountDigits(digits)

        for (d in digits) {
            for (rd in 0..9) {
                val (canReplace, replacedDigits) = replaceDigits(digits, from = d, to = rd)

                if (!canReplace) continue

                val replaced = mountDigits(replacedDigits)

                if (replaced < low) low = replaced
            }
        }

        return low
    }

    fun maxValueReplacing(digits: List<Int>): Int {
        var high = mountDigits(digits)

        for (d in digits) {
            for (rd in 0..9) {
                val (canReplace, replacedDigits) = replaceDigits(digits, from = d, to = rd)

                if (!canReplace) continue

                val replaced = mountDigits(replacedDigits)

                if (replaced > high) high = replaced
            }
        }

        return high
    }

    fun maxDiff(num: Int): Int {
        val digits = digitsOf(num)
        return maxValueReplacing(digits) - minValueReplacing(digits)
    }
}