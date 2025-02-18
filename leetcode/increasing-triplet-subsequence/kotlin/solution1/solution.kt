class Solution {
    fun increasingTriplet(nums: IntArray): Boolean {
        val tri = IntArray(2)
        var size = 0
        var p: Int? = null
        for (n in nums) {
            if (size == 0) {
                tri[0] = n
                size++
                continue
            }
            
            if (size == 1) {
                if (tri[0] == n) {
                    continue
                }

                if (tri[0] < n) {
                    tri[1] = n
                    size++
                } else {
                    tri[0] = n
                }

                continue
            } 

            if (size == 2) {
                if (tri[1] < n) {
                    return true
                }

                if (tri[1] == n) {
                    continue
                }

                if (tri[0] < n) {
                    tri[1] = n
                    if (p == null) {
                        p = n
                    } else {
                        tri[0] = p
                        p = null
                    }
                }

                if (tri[0] == n) {
                    if (p != null) {
                        if (p < n) {
                            tri[0] = p
                            tri[1] = n
                        }
                    }
                    continue
                }

                if (tri[0] > n) {
                    if (p == null) {
                        p = n
                    } else {
                        tri[0] = p
                        tri[1] = n
                        p = null
                    }
                }
            }
        }
        return false
    }
}
