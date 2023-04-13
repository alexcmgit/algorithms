import kotlin.math.abs
import kotlin.math.pow
import kotlin.math.sqrt

class Solution {
    fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> =
        points.apply { sortBy { (x, y) -> sqrt(abs(x).toDouble().pow(2) + abs(y).toDouble().pow(2)) } }
            .copyOfRange(0, k)
}
