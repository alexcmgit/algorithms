class Solution {
    fun reverseVowels(s: String): String {
        val charArray = s.toCharArray()
        val indexesToReplace = mutableListOf<Int>()

        for (index in 0..charArray.size - 1) {
            if (charArray[index] in "aeiouAEIOU") {
                indexesToReplace.add(index)
            }
        }
        
        while (indexesToReplace.size != 0) {
            val from = indexesToReplace.removeFirst()
            val to = indexesToReplace.removeLastOrNull()
            if (to == null) continue
            val swap = charArray[from]
            charArray[from] = charArray[to]
            charArray[to] = swap
        }

        return charArray.joinToString("")
    }
}