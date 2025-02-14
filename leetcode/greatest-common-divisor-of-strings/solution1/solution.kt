class Solution {
    fun gcdOfStrings(str1: String, str2: String): String {
        var div: String = when {
            str1.length == str2.length -> str1
            str1.length > str2.length -> str2
            else -> str1
        }

        var res: String? = null

        while (true) {
            if (str1.replace(div, "") == "" && str2.replace(div, "") == "") {
                res = div
                break
            }
            div = div.substring(0, div.length - 1)
            if (div.isEmpty()) {
                break
            }
        }

        return res ?: ""
    }
}
