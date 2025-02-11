class Solution {
    fun mergeAlternately(word1: String, word2: String): String {
        val cutAt = min(word1.length, word2.length)
        val res = StringBuffer()

        for (i in 0..cutAt - 1) {
            res.append(word1.elementAt(i))
            res.append(word2.elementAt(i))
        }

        res.append(word1.substring(cutAt) + word2.substring(cutAt))

        return res.toString()
    }
}
