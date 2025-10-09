class Solution {
    fun maxDiff(n: Int): Int {
        val digits = n.toDigits().toList()
        
        var maxFrom = digits.first()
        val maxTo = 9
        for (d in digits) {
            if (d == 9) continue
            maxFrom = d
            break
        }
        
        var minFrom = digits.first()
        var minTo = 1
        for ((i, d) in digits.withIndex()) {
            if (d == 0) continue
            if (d == 1) continue
            minFrom = d
            if (i != 0) {
                minTo = 0
            }
            break
        }
        
        return digits.map { if (it == maxFrom) maxTo else it }.mountToInt() -
               digits.map { if (it == minFrom) minTo else it }.mountToInt()
    }
}

fun largestPowerOfOrNull(x: Int, base: Int = 10): Int? {
    return try {
        largestPowerOf(x, base)
    } catch (e: Exception) {
        null
    }
}

fun largestPowerOf(x: Int, base: Int = 10): Int {
    val (_, power) = largestExponentAndPowerOf(x, base)
    return power
}

data class ExponentAndPower(val exponent: Int, val power: Int)

fun largestExponentAndPowerOf(x: Int, base: Int = 10): ExponentAndPower {
    var exponent = 0
    var power = 1
    while (power * base <= x) {
        power *= base
        exponent++
    }
    return ExponentAndPower(exponent, power)
}

fun Int.toDigits(radix: Int = 10): Sequence<Int> = sequence {
    var self = this@toDigits.absoluteValue
    var power = largestPowerOfOrNull(self, radix) ?: 1
    do {
        yield(self / power)
        self %= power
        power /= radix
    } while (power > 0)
}

fun Iterable<Int>.mountToInt(radix: Int = 10): Int {
    var mounted = 0
    for (digit in this) {
        mounted *= radix
        mounted += digit.absoluteValue
    }
    return mounted
}
