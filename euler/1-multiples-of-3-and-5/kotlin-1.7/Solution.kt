fun sum(r: Long, n: Long) = (n * (r + n * r)) / 2

fun multiplesOf3And5Below(n: Long): Long {
  val e: Long = n - 1

  val setA: Long = sum(3, e / 3)
  val setB: Long = sum(5, e / 5)

  val setC: Long = sum(15, e / 15)

  return setA + setB - setC
}