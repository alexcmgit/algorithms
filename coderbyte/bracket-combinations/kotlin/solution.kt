fun fac(n: Int): Int {
  if (n == 0) return 1
  return n * fac(n - 1)
}

// https://en.wikipedia.org/wiki/Catalan_number
fun BracketCombinations(n: Int): Int {
  return fac(2 * n) / (fac(n + 1) * fac(n))
}

fun main() {
  println(BracketCombinations(readLine()))
}
