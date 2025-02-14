class ProductOfNumbers() {
    val nums = mutableListOf<Int>()
    fun add(num: Int) {
        nums.add(num)
    }

    fun getProduct(k: Int): Int {
        if (nums.isEmpty()) return 0
        return nums.drop(nums.size - k).fold(1) { acc, e -> acc * e }
    }

}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */