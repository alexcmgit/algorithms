class Solution {
    companion object {
        const val v = "aeiouAEIOU"
    }
    fun reverseVowels(s: String): String {
        val arr = s.toCharArray()
        var start = 0
        var end = s.length - 1

        b@while (true) {
            while (true) {
                if (start == arr.size) {
                    break@b
                }
                if (arr[start] in v) {
                    break
                } else {
                    start++
                }
            }
            while (true) {
                if (end == 0) {
                    break@b
                }
                if (arr[end] in v) {
                    break
                } else {
                    end--
                }
            }
            if (start >= end) {
                break@b
            }
            val swap = arr[start]
            arr[start] = arr[end]
            arr[end] = swap
            start++
            end--
        }

        return arr.joinToString("")
    }
}